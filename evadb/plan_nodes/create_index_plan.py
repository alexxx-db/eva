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
from typing import List

from evadb.catalog.catalog_type import VectorStoreType
from evadb.expression.abstract_expression import AbstractExpression
from evadb.expression.function_expression import FunctionExpression
from evadb.parser.create_statement import ColumnDefinition
from evadb.parser.table_ref import TableRef
from evadb.plan_nodes.abstract_plan import AbstractPlan
from evadb.plan_nodes.types import PlanOprType


class CreateIndexPlan(AbstractPlan):
    def __init__(
        self,
        name: str,
        if_not_exists: bool,
        table_ref: TableRef,
        col_list: List[ColumnDefinition],
        vector_store_type: VectorStoreType,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
        project_expr_list: List[AbstractExpression],
        index_def: str,
=======
        function: FunctionExpression = None,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
        project_expr_list: List[AbstractExpression],
        index_def: str,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
        project_expr_list: List[AbstractExpression],
        index_def: str,
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
    ):
        super().__init__(PlanOprType.CREATE_INDEX)
        self._name = name
        self._if_not_exists = if_not_exists
        self._table_ref = table_ref
        self._col_list = col_list
        self._vector_store_type = vector_store_type
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
        self._project_expr_list = project_expr_list
        self._index_def = index_def
=======
        self._function = function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
        self._project_expr_list = project_expr_list
        self._index_def = index_def
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
        self._project_expr_list = project_expr_list
        self._index_def = index_def
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)

    @property
    def name(self):
        return self._name

    @property
    def if_not_exists(self):
        return self._if_not_exists

    @property
    def table_ref(self):
        return self._table_ref

    @property
    def col_list(self):
        return self._col_list

    @property
    def vector_store_type(self):
        return self._vector_store_type

    @property
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
    def project_expr_list(self):
        return self._project_expr_list

    @property
    def index_def(self):
        return self._index_def
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
    def function(self):
        return self._function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)

    def __str__(self):
        function_expr = None
        for project_expr in self._project_expr_list:
            if isinstance(project_expr, FunctionExpression):
                function_expr = project_expr

        return "CreateIndexPlan(name={}, \
            table_ref={}, \
            col_list={}, \
            vector_store_type={}, \
            {})".format(
            self._name,
            self._table_ref,
            tuple(self._col_list),
            self._vector_store_type,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
            "" if function_expr is None else "function={}".format(function_expr),
=======
            "" if not self._function else "function={}".format(self._function),
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
            "" if function_expr is None else "function={}".format(function_expr),
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
            "" if function_expr is None else "function={}".format(function_expr),
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
            "" if function_expr is None else "function={}".format(function_expr),
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
        )

    def __hash__(self) -> int:
        return hash(
            (
                super().__hash__(),
                self.name,
                self.if_not_exists,
                self.table_ref,
                tuple(self.col_list),
                self.vector_store_type,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
                tuple(self.project_expr_list),
                self.index_def,
=======
                self.function,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
                tuple(self.project_expr_list),
                self.index_def,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
                tuple(self.project_expr_list),
                self.index_def,
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
            )
        )
