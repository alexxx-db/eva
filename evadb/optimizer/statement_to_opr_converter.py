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
from evadb.binder.binder_utils import get_bound_func_expr_outputs_as_tuple_value_expr
from evadb.expression.abstract_expression import AbstractExpression
from evadb.expression.function_expression import FunctionExpression
from evadb.optimizer.operators import (
    LogicalCreate,
    LogicalCreateFunction,
    LogicalCreateIndex,
    LogicalDelete,
    LogicalDropObject,
    LogicalExplain,
    LogicalExtractObject,
    LogicalFilter,
    LogicalFunctionScan,
    LogicalGet,
    LogicalGroupBy,
    LogicalInsert,
    LogicalJoin,
    LogicalLimit,
    LogicalLoadData,
    LogicalOrderBy,
    LogicalProject,
    LogicalQueryDerivedGet,
    LogicalRename,
    LogicalSample,
    LogicalShow,
    LogicalUnion,
)
from evadb.optimizer.optimizer_utils import (
    column_definition_to_function_io,
    metadata_definition_to_function_metadata,
)
from evadb.parser.create_function_statement import CreateFunctionStatement
from evadb.parser.create_index_statement import CreateIndexStatement
from evadb.parser.create_statement import CreateTableStatement
from evadb.parser.delete_statement import DeleteTableStatement
from evadb.parser.drop_object_statement import DropObjectStatement
from evadb.parser.explain_statement import ExplainStatement
from evadb.parser.insert_statement import InsertTableStatement
from evadb.parser.load_statement import LoadDataStatement
from evadb.parser.rename_statement import RenameTableStatement
from evadb.parser.select_statement import SelectStatement
from evadb.parser.show_statement import ShowStatement
from evadb.parser.statement import AbstractStatement
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
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
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
=======
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
from evadb.parser.table_ref import TableRef
from evadb.parser.types import FunctionType
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
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
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.parser.table_ref import JoinNode, TableRef, TableValuedExpression
from evadb.parser.types import FunctionType, JoinType
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
from evadb.parser.table_ref import TableRef
from evadb.parser.types import FunctionType
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
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
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.utils.logging_manager import logger


class StatementToPlanConverter:
    def __init__(self):
        self._plan = None

    def visit_table_ref(self, table_ref: TableRef):
        """Bind table ref object and convert to LogicalGet, LogicalJoin,
            LogicalFunctionScan, or LogicalQueryDerivedGet

        Arguments:
            table {TableRef} - - [Input table ref object created by the parser]
        """
        if table_ref.is_table_atom():
            # Table
            catalog_entry = table_ref.table.table_obj
            self._plan = LogicalGet(
                table_ref,
                catalog_entry,
                table_ref.alias,
                chunk_params=table_ref.chunk_params,
            )

        elif table_ref.is_table_valued_expr():
            tve = table_ref.table_valued_expr
            if tve.func_expr.name.lower() == str(FunctionType.EXTRACT_OBJECT).lower():
                self._plan = LogicalExtractObject(
                    detector=tve.func_expr.children[1],
                    tracker=tve.func_expr.children[2],
                    alias=table_ref.alias,
                    do_unnest=tve.do_unnest,
                )
            else:
                self._plan = LogicalFunctionScan(
                    func_expr=tve.func_expr,
                    alias=table_ref.alias,
                    do_unnest=tve.do_unnest,
                )

        elif table_ref.is_select():
            # NestedQuery
            self.visit_select(table_ref.select_statement)
            child_plan = self._plan
            self._plan = LogicalQueryDerivedGet(table_ref.alias)
            self._plan.append_child(child_plan)

        elif table_ref.is_join():
            join_node = table_ref.join_node
            join_plan = LogicalJoin(
                join_type=join_node.join_type,
                join_predicate=join_node.predicate,
            )
            self.visit_table_ref(join_node.left)
            join_plan.append_child(self._plan)
            self.visit_table_ref(join_node.right)
            join_plan.append_child(self._plan)
            self._plan = join_plan

        if table_ref.sample_freq:
            self._visit_sample(table_ref.sample_freq, table_ref.sample_type)

    def visit_select(self, statement: SelectStatement):
        """converter for select statement

        Arguments:
            statement {SelectStatement} - - [input select statement]
        """

        # order of evaluation
        # from, where, group by, select, order by, limit, union

        # if there is a table_ref, order by clause and no group by clause, we move all # the function expressions out of projection list to table valued expression.
        # This is done to handle the
        # https://github.com/georgia-tech-db/evadb/issues/1147
        # and https://github.com/georgia-tech-db/evadb/issues/1130.
        # It is a bit ugly but a complete fix would require modifying the binder

        col_with_func_exprs = []

        if statement.orderby_list and statement.groupby_clause is None:
            projection_cols = []
            for col in statement.target_list:
                if isinstance(col, FunctionExpression):
                    col_with_func_exprs.append(col)
                    # append the TupleValueExpression for the FunctionExpression
                    projection_cols.extend(
                        get_bound_func_expr_outputs_as_tuple_value_expr(col)
                    )
                else:
                    projection_cols.append(col)

            # update target list with projection cols
            statement.target_list = projection_cols

        table_ref = statement.from_table
        if not table_ref and col_with_func_exprs:
            # if there is no table source, we add a projection node with all the
            # function expressions
            self._visit_projection(col_with_func_exprs)
        else:
            # add col_with_func_exprs to TableValuedExpressions
            for col in col_with_func_exprs:
                tve = TableValuedExpression(col)
                if table_ref:
                    table_ref = TableRef(
                        JoinNode(
                            table_ref,
                            TableRef(tve, alias=col.alias),
                            join_type=JoinType.LATERAL_JOIN,
                        )
                    )

            statement.from_table = table_ref

        if table_ref is not None:
            self.visit_table_ref(table_ref)

            # Filter Operator
            predicate = statement.where_clause
            if predicate is not None:
                self._visit_select_predicate(predicate)

            # TODO ACTION: Group By

            if statement.groupby_clause is not None:
                self._visit_groupby(statement.groupby_clause)

        if statement.orderby_list is not None:
            self._visit_orderby(statement.orderby_list)

        if statement.limit_count is not None:
            self._visit_limit(statement.limit_count)

        if statement.target_list is not None:
            self._visit_projection(statement.target_list)

        # union
        if statement.union_link is not None:
            self._visit_union(statement.union_link, statement.union_all)

    def _visit_sample(self, sample_freq, sample_type):
        sample_opr = LogicalSample(sample_freq, sample_type)
        sample_opr.append_child(self._plan)
        self._plan = sample_opr

    def _visit_groupby(self, groupby_clause):
        groupby_opr = LogicalGroupBy(groupby_clause)
        groupby_opr.append_child(self._plan)
        self._plan = groupby_opr

    def _visit_orderby(self, orderby_list):
        # orderby_list structure: List[(TupleValueExpression, EnumInt), ...]
        orderby_opr = LogicalOrderBy(orderby_list)
        orderby_opr.append_child(self._plan)
        self._plan = orderby_opr

    def _visit_limit(self, limit_count):
        limit_opr = LogicalLimit(limit_count)
        limit_opr.append_child(self._plan)
        self._plan = limit_opr

    def _visit_union(self, target, all):
        left_child_plan = self._plan
        self.visit_select(target)
        right_child_plan = self._plan
        self._plan = LogicalUnion(all=all)
        self._plan.append_child(left_child_plan)
        self._plan.append_child(right_child_plan)

    def _visit_projection(self, select_columns):
        projection_opr = LogicalProject(select_columns)
        if self._plan is not None:
            projection_opr.append_child(self._plan)
        self._plan = projection_opr

    def _visit_select_predicate(self, predicate: AbstractExpression):
        filter_opr = LogicalFilter(predicate)
        filter_opr.append_child(self._plan)
        self._plan = filter_opr

    def visit_insert(self, statement: AbstractStatement):
        """Converter for parsed insert statement

        Arguments:
            statement {AbstractStatement} - - [input insert statement]
        """
        # not removing previous commented code
        insert_data_opr = LogicalInsert(
            statement.table_ref,
            statement.column_list,
            statement.value_list,
        )
        self._plan = insert_data_opr

        """
        table_ref = statement.table
        table_metainfo = bind_dataset(table_ref.table)
        if table_metainfo is None:
            # Create a new metadata object
            table_metainfo = create_video_metadata(table_ref.table.table_name)

        # populate self._column_map
        self._populate_column_map(table_metainfo)

        # Bind column_list
        bind_columns_expr(statement.column_list, self._column_map)

        # Nothing to be done for values as we add support for other variants of
        # insert we will handle them
        value_list = statement.value_list

        # Ready to create Logical node
        insert_opr = LogicalInsert(
            table_ref, table_metainfo, statement.column_list, value_list)
        self._plan = insert_opr
        """

    def visit_create(self, statement: AbstractStatement):
        """Converter for parsed insert Statement

        Arguments:
            statement {AbstractStatement} - - [Create statement]
        """
        table_info = statement.table_info
        if table_info is None:
            logger.error("Missing Table Name In Create Statement")

        create_opr = LogicalCreate(
            table_info, statement.column_list, statement.if_not_exists
        )

        if statement.query is not None:
            self.visit_select(statement.query)
            create_opr.append_child(self._plan)
        self._plan = create_opr

    def visit_rename(self, statement: RenameTableStatement):
        """Converter for parsed rename statement
        Arguments:
            statement(RenameTableStatement): [Rename statement]
        """
        rename_opr = LogicalRename(statement.old_table_ref, statement.new_table_name)
        self._plan = rename_opr

    def visit_create_function(self, statement: CreateFunctionStatement):
        """Converter for parsed create function statement

        Arguments:
            statement {CreateFunctionStatement} - - CreateFunctionStatement
        """
        annotated_inputs = column_definition_to_function_io(statement.inputs, True)
        annotated_outputs = column_definition_to_function_io(statement.outputs, False)
        annotated_metadata = metadata_definition_to_function_metadata(
            statement.metadata
        )

        create_function_opr = LogicalCreateFunction(
            statement.name,
            statement.or_replace,
            statement.if_not_exists,
            annotated_inputs,
            annotated_outputs,
            statement.impl_path,
            statement.function_type,
            annotated_metadata,
        )

        if statement.query is not None:
            self.visit_select(statement.query)
            create_function_opr.append_child(self._plan)

        self._plan = create_function_opr

    def visit_drop_object(self, statement: DropObjectStatement):
        self._plan = LogicalDropObject(
            statement.object_type, statement.name, statement.if_exists
        )

    def visit_load_data(self, statement: LoadDataStatement):
        """Converter for parsed load data statement
        Arguments:
            statement(LoadDataStatement): [Load data statement]
        """
        load_data_opr = LogicalLoadData(
            statement.table_info,
            statement.path,
            statement.column_list,
            statement.file_options,
        )
        self._plan = load_data_opr

    def visit_show(self, statement: ShowStatement):
        show_opr = LogicalShow(statement.show_type, statement.show_val)
        self._plan = show_opr

    def visit_explain(self, statement: ExplainStatement):
        explain_opr = LogicalExplain([self.visit(statement.explainable_stmt)])
        self._plan = explain_opr

    def visit_create_index(self, statement: CreateIndexStatement):
        create_index_opr = LogicalCreateIndex(
            statement.name,
            statement.if_not_exists,
            statement.table_ref,
            statement.col_list,
            statement.vector_store_type,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            statement.project_expr_list,
            statement.index_def,
=======
            statement.function,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
            statement.project_expr_list,
            statement.index_def,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
            statement.project_expr_list,
            statement.index_def,
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        )
        self._plan = create_index_opr

    def visit_delete(self, statement: DeleteTableStatement):
        delete_opr = LogicalDelete(
            statement.table_ref,
            statement.where_clause,
        )
        self._plan = delete_opr

    def visit(self, statement: AbstractStatement):
        """Based on the instance of the statement the corresponding
           visit is called.
           The logic is hidden from client.

        Arguments:
            statement {AbstractStatement} - - [Input statement]
        """
        if isinstance(statement, SelectStatement):
            self.visit_select(statement)
        elif isinstance(statement, InsertTableStatement):
            self.visit_insert(statement)
        elif isinstance(statement, CreateTableStatement):
            self.visit_create(statement)
        elif isinstance(statement, RenameTableStatement):
            self.visit_rename(statement)
        elif isinstance(statement, CreateFunctionStatement):
            self.visit_create_function(statement)
        elif isinstance(statement, DropObjectStatement):
            self.visit_drop_object(statement)
        elif isinstance(statement, LoadDataStatement):
            self.visit_load_data(statement)
        elif isinstance(statement, ShowStatement):
            self.visit_show(statement)
        elif isinstance(statement, ExplainStatement):
            self.visit_explain(statement)
        elif isinstance(statement, CreateIndexStatement):
            self.visit_create_index(statement)
        elif isinstance(statement, DeleteTableStatement):
            self.visit_delete(statement)
        return self._plan

    @property
    def plan(self):
        return self._plan
