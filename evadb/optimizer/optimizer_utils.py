# coding=utf-8
# Copyright 2018-2023 EvaDB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import typing
from typing import List, Tuple

if typing.TYPE_CHECKING:
    from evadb.optimizer.optimizer_context import OptimizerContext

from evadb.catalog.catalog_utils import get_table_primary_columns
from evadb.catalog.models.column_catalog import ColumnCatalogEntry
from evadb.catalog.models.function_io_catalog import FunctionIOCatalogEntry
from evadb.catalog.models.function_metadata_catalog import FunctionMetadataCatalogEntry
from evadb.constants import CACHEABLE_FUNCTIONS, DEFAULT_FUNCTION_EXPRESSION_COST
from evadb.expression.abstract_expression import AbstractExpression, ExpressionType
from evadb.expression.constant_value_expression import ConstantValueExpression
from evadb.expression.expression_utils import (
    conjunction_list_to_expression_tree,
    contains_single_column,
    get_columns_in_predicate,
    is_simple_predicate,
    to_conjunction_list,
)
from evadb.expression.function_expression import (
    FunctionExpression,
    FunctionExpressionCache,
)
from evadb.expression.tuple_value_expression import TupleValueExpression
from evadb.parser.alias import Alias
from evadb.parser.create_statement import ColumnDefinition
from evadb.utils.kv_cache import DiskKVCache


def column_definition_to_function_io(col_list: List[ColumnDefinition], is_input: bool):
    """Create the FunctionIOCatalogEntry object for each column definition provided

    Arguments:
        col_list(List[ColumnDefinition]): parsed input/output definitions
        is_input(bool): true if input else false
    """
    if isinstance(col_list, ColumnDefinition):
        col_list = [col_list]

    result_list = []
    for col in col_list:
        assert col is not None, "Empty column definition while creating function io"
        result_list.append(
            FunctionIOCatalogEntry(
                col.name,
                col.type,
                col.cci.nullable,
                array_type=col.array_type,
                array_dimensions=col.dimension,
                is_input=is_input,
            )
        )
    return result_list


def metadata_definition_to_function_metadata(metadata_list: List[Tuple[str, str]]):
    """Create the FunctionMetadataCatalogEntry object for each metadata definition provided

    Arguments:
        col_list(List[Tuple[str, str]]): parsed metadata definitions
    """
    result_list = []
    for metadata in metadata_list:
        result_list.append(
            FunctionMetadataCatalogEntry(
                metadata[0],
                metadata[1],
            )
        )
    return result_list


def extract_equi_join_keys(
    join_predicate: AbstractExpression,
    left_table_aliases: List[Alias],
    right_table_aliases: List[Alias],
) -> Tuple[List[AbstractExpression], List[AbstractExpression]]:
    pred_list = to_conjunction_list(join_predicate)
    left_join_keys = []
    right_join_keys = []
    left_table_alias_strs = [
        left_table_alias.alias_name for left_table_alias in left_table_aliases
    ]
    right_table_alias_strs = [
        right_table_alias.alias_name for right_table_alias in right_table_aliases
    ]

    for pred in pred_list:
        if pred.etype == ExpressionType.COMPARE_EQUAL:
            left_child = pred.children[0]
            right_child = pred.children[1]
            # only extract if both are TupleValueExpression
            if (
                left_child.etype == ExpressionType.TUPLE_VALUE
                and right_child.etype == ExpressionType.TUPLE_VALUE
            ):
                if (
                    left_child.table_alias in left_table_alias_strs
                    and right_child.table_alias in right_table_alias_strs
                ):
                    left_join_keys.append(left_child)
                    right_join_keys.append(right_child)
                elif (
                    left_child.table_alias in right_table_alias_strs
                    and right_child.table_alias in left_table_alias_strs
                ):
                    left_join_keys.append(right_child)
                    right_join_keys.append(left_child)

    return (left_join_keys, right_join_keys)


def extract_pushdown_predicate(
    predicate: AbstractExpression, column_alias: str
) -> Tuple[AbstractExpression, AbstractExpression]:
    """Decompose the predicate into pushdown predicate and remaining predicate

    Args:
        predicate (AbstractExpression): predicate that needs to be decomposed
        column (str): column_alias to extract predicate
    Returns:
        Tuple[AbstractExpression, AbstractExpression]: (pushdown predicate,
        remaining predicate)
    """
    if predicate is None:
        return None, None

    if contains_single_column(predicate, column_alias):
        if is_simple_predicate(predicate):
            return predicate, None

    pushdown_preds = []
    rem_pred = []
    pred_list = to_conjunction_list(predicate)
    for pred in pred_list:
        if contains_single_column(pred, column_alias) and is_simple_predicate(pred):
            pushdown_preds.append(pred)
        else:
            rem_pred.append(pred)

    return (
        conjunction_list_to_expression_tree(pushdown_preds),
        conjunction_list_to_expression_tree(rem_pred),
    )


def extract_pushdown_predicate_for_alias(
    predicate: AbstractExpression, aliases: List[Alias]
):
    """Extract predicate that can be pushed down based on the input aliases.

    Atomic predicates on the table columns that are the subset of the input aliases are
    considered as candidates for pushdown.

    Args:
        predicate (AbstractExpression): input predicate
        aliases (List[str]): aliases for which predicate can be pushed
    """
    if predicate is None:
        return None, None

    pred_list = to_conjunction_list(predicate)
    pushdown_preds = []
    rem_pred = []
    aliases = [alias.alias_name for alias in aliases]
    for pred in pred_list:
        column_aliases = get_columns_in_predicate(pred)
        table_aliases = set([col.split(".")[0] for col in column_aliases])
        if table_aliases.issubset(set(aliases)):
            pushdown_preds.append(pred)
        else:
            rem_pred.append(pred)
    return (
        conjunction_list_to_expression_tree(pushdown_preds),
        conjunction_list_to_expression_tree(rem_pred),
    )


def optimize_cache_key_for_tuple_value_expression(
    context: "OptimizerContext", tv_expr: TupleValueExpression
):
    catalog = context.db.catalog()
    col_catalog_obj = tv_expr.col_object

    # Optimized cache key for TupleValueExpression.
    new_keys = []

    if isinstance(col_catalog_obj, ColumnCatalogEntry):
        table_obj = catalog.get_table_catalog_entry(col_catalog_obj.table_name)
        for col in get_table_primary_columns(table_obj):
            new_obj = catalog.get_column_catalog_entry(table_obj, col.name)
            new_keys.append(
                TupleValueExpression(
                    name=col.name,
                    table_alias=tv_expr.table_alias,
                    col_object=new_obj,
                    col_alias=f"{tv_expr.table_alias}.{col.name}",
                )
            )
        return new_keys

    return [tv_expr]


def optimize_cache_key_for_constant_value_expression(
    context: "OptimizerContext", cv_expr: ConstantValueExpression
):
    # No need to additional optimization for constant value expression.
    return [cv_expr]


def optimize_cache_key(context: "OptimizerContext", expr: FunctionExpression):
    """Optimize the cache key

    It tries to reduce the caching overhead by replacing the caching key with
    logically equivalent key. For instance, frame data can be replaced with frame id.

    Args:
        expr (FunctionExpression): expression to optimize the caching key for.

    Example:
        Yolo(data) -> return id

    Todo: Optimize complex expression
        FaceDet(Crop(data, bbox)) -> return

    """
    keys = expr.children

    optimize_key_mapping_f = {
        TupleValueExpression: optimize_cache_key_for_tuple_value_expression,
        ConstantValueExpression: optimize_cache_key_for_constant_value_expression,
    }

    optimized_keys = []
    for key in keys:
        if type(key) not in optimize_key_mapping_f:
            raise RuntimeError(f"Optimize cache key of {type(key)} is not implemented")
        optimized_keys += optimize_key_mapping_f[type(key)](context, key)

    return optimized_keys


def enable_cache_init(
    context: "OptimizerContext", func_expr: FunctionExpression
) -> FunctionExpressionCache:
    optimized_key = optimize_cache_key(context, func_expr)
    if optimized_key == func_expr.children:
        optimized_key = [None]

    catalog = context.db.catalog()
    name = func_expr.signature()
    cache_entry = catalog.get_function_cache_catalog_entry_by_name(name)
    if not cache_entry:
        cache_entry = catalog.insert_function_cache_catalog_entry(func_expr)

    cache = FunctionExpressionCache(
        key=tuple(optimized_key), store=DiskKVCache(cache_entry.cache_path)
    )
    return cache


def enable_cache(
    context: "OptimizerContext", func_expr: FunctionExpression
) -> FunctionExpression:
    """Enables cache for a function expression.

    The cache key is optimized by replacing it with logical equivalent expressions.
    A cache entry is inserted in the catalog corresponding to the expression.

    Args:
        context (OptimizerContext): associated optimizer context
        func_expr (FunctionExpression): The function expression to enable cache for.

    Returns:
        FunctionExpression: The function expression with cache enabled.
    """
    cache = enable_cache_init(context, func_expr)
    return func_expr.copy().enable_cache(cache)


def enable_cache_on_expression_tree(
    context: "OptimizerContext", expr_tree: AbstractExpression
):
    func_exprs = list(expr_tree.find_all(FunctionExpression))
    func_exprs = list(
        filter(lambda expr: check_expr_validity_for_cache(expr), func_exprs)
    )
    for expr in func_exprs:
        cache = enable_cache_init(context, expr)
        expr.enable_cache(cache)


def check_expr_validity_for_cache(expr: FunctionExpression):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    valid = expr.name in CACHEABLE_FUNCTIONS and not expr.has_cache()
    if len(expr.children) == 1:
        # Normal function that only takes one parameter.
        valid &= isinstance(expr.children[0], TupleValueExpression)
    elif len(expr.children) == 2:
        # LLM-based function that takes two parameters.
        valid &= isinstance(expr.children[0], ConstantValueExpression) and isinstance(
            expr.children[1], TupleValueExpression
        )
    return valid
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    return (
        expr.name in CACHEABLE_FUNCTIONS
        and not expr.has_cache()
        and len(expr.children) <= 1
        and isinstance(expr.children[0], TupleValueExpression)
    )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main


def get_expression_execution_cost(
    context: "OptimizerContext", expr: AbstractExpression
) -> float:
    """
    This function computes the estimated cost of executing the given abstract expression
    based on the statistics in the catalog. The function assumes that all the
    expression, except for the FunctionExpression, have a cost of zero.
    For FunctionExpression, it checks the catalog for relevant statistics; if none are
    available, it uses a default cost of DEFAULT_FUNCTION_EXPRESSION_COST.

    Args:
        context (OptimizerContext): the associated optimizer context
        expr (AbstractExpression): The AbstractExpression object whose cost
        needs to be computed.

    Returns:
        float: The estimated cost of executing the function expression.
    """
    total_cost = 0
    # iterate over all the function expression and accumulate the cost
    for child_expr in expr.find_all(FunctionExpression):
        cost_entry = context.db.catalog().get_function_cost_catalog_entry(
            child_expr.name
        )
        if cost_entry:
            total_cost += cost_entry.cost
        else:
            total_cost += DEFAULT_FUNCTION_EXPRESSION_COST
    return total_cost
