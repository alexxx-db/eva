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

from lark import Tree

from evadb.catalog.catalog_type import ColumnType, NdArrayType, VectorStoreType
from evadb.expression.tuple_value_expression import TupleValueExpression
from evadb.parser.create_index_statement import CreateIndexStatement
from evadb.parser.create_statement import (
    ColConstraintInfo,
    ColumnDefinition,
    CreateDatabaseStatement,
    CreateJobStatement,
    CreateTableStatement,
)
from evadb.parser.table_ref import TableRef
from evadb.parser.types import ColumnConstraintEnum


##################################################################
# CREATE STATEMENTS
##################################################################
class CreateTable:
    def create_table(self, tree):
        table_info = None
        if_not_exists = False
        create_definitions = []
        query = None

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "if_not_exists":
                    if_not_exists = True
                elif child.data == "table_name":
                    table_info = self.visit(child)
                elif child.data == "create_definitions":
                    create_definitions = self.visit(child)
                elif child.data == "simple_select":
                    query = self.visit(child)

        create_stmt = CreateTableStatement(
            table_info, if_not_exists, create_definitions, query=query
        )
        return create_stmt

    def create_definitions(self, tree):
        column_definitions = []
        for child in tree.children:
            if isinstance(child, Tree):
                create_definition = None
                if child.data == "column_declaration":
                    create_definition = self.visit(child)
                column_definitions.append(create_definition)

        return column_definitions

    def column_declaration(self, tree):
        column_name = None
        data_type = None
        array_type = None
        dimensions = None
        column_constraint_information = None

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "uid":
                    column_name = self.visit(child)
                elif child.data == "column_definition":
                    (
                        data_type,
                        array_type,
                        dimensions,
                        column_constraint_information,
                    ) = self.visit(child)

        if column_name is not None:
            return ColumnDefinition(
                column_name,
                data_type,
                array_type,
                dimensions,
                column_constraint_information,
            )

    def column_definition(self, tree):
        data_type = None
        array_type = None
        dimensions = None
        column_constraint_information = ColConstraintInfo()
        not_null_set = False

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data.endswith("data_type"):
                    data_type, array_type, dimensions = self.visit(child)
                elif child.data.endswith("column_constraint"):
                    return_type = self.visit(child)
                    if return_type == ColumnConstraintEnum.UNIQUE:
                        column_constraint_information.unique = True
                        column_constraint_information.nullable = False
                        not_null_set = True
                    elif return_type == ColumnConstraintEnum.NOTNULL:
                        column_constraint_information.nullable = False
                        not_null_set = True

        if not not_null_set:
            column_constraint_information.nullable = True

        return data_type, array_type, dimensions, column_constraint_information

    def unique_key_column_constraint(self, tree):
        return ColumnConstraintEnum.UNIQUE

    def null_column_constraint(self, tree):
        return ColumnConstraintEnum.NOTNULL

    def simple_data_type(self, tree):
        data_type = None
        array_type = None
        dimensions = []

        token = tree.children[0]
        if str.upper(token) == "BOOLEAN":
            data_type = ColumnType.BOOLEAN

        return data_type, array_type, dimensions

    def integer_data_type(self, tree):
        data_type = None
        array_type = None
        dimensions = []

        token = tree.children[0]
        if str.upper(token) == "INTEGER":
            data_type = ColumnType.INTEGER

        return data_type, array_type, dimensions

    def dimension_data_type(self, tree):
        data_type = None
        array_type = None
        dimensions = []

        token = tree.children[0]
        if str.upper(token) == "FLOAT":
            data_type = ColumnType.FLOAT
        elif str.upper(token) == "TEXT":
            data_type = ColumnType.TEXT

        if len(tree.children) > 1:
            dimensions = self.visit(tree.children[1])

        return data_type, array_type, dimensions

    def array_data_type(self, tree):
        data_type = ColumnType.NDARRAY
        array_type = NdArrayType.ANYTYPE
        dimensions = None

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "array_type":
                    array_type = self.visit(child)
                elif child.data == "length_dimension_list":
                    dimensions = self.visit(child)

        return data_type, array_type, dimensions

    def any_data_type(self, tree):
        return ColumnType.ANY, None, []

    def array_type(self, tree):
        array_type = None

        token = tree.children[0]
        if str.upper(token) == "INT8":
            array_type = NdArrayType.INT8
        elif str.upper(token) == "UINT8":
            array_type = NdArrayType.UINT8
        elif str.upper(token) == "INT16":
            array_type = NdArrayType.INT16
        elif str.upper(token) == "INT32":
            array_type = NdArrayType.INT32
        elif str.upper(token) == "INT64":
            array_type = NdArrayType.INT64
        elif str.upper(token) == "UNICODE":
            array_type = NdArrayType.UNICODE
        elif str.upper(token) == "BOOLEAN":
            array_type = NdArrayType.BOOL
        elif str.upper(token) == "FLOAT32":
            array_type = NdArrayType.FLOAT32
        elif str.upper(token) == "FLOAT64":
            array_type = NdArrayType.FLOAT64
        elif str.upper(token) == "DECIMAL":
            array_type = NdArrayType.DECIMAL
        elif str.upper(token) == "STR":
            array_type = NdArrayType.STR
        elif str.upper(token) == "DATETIME":
            array_type = NdArrayType.DATETIME
        elif str.upper(token) == "ANYTYPE":
            array_type = NdArrayType.ANYTYPE
        return array_type

    def dimension_helper(self, tree):
        dimensions = []
        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "decimal_literal":
                    decimal = self.visit(child)
                    dimensions.append(decimal)
        return tuple(dimensions)

    def length_one_dimension(self, tree):
        dimensions = self.dimension_helper(tree)
        return dimensions

    def length_two_dimension(self, tree):
        dimensions = self.dimension_helper(tree)
        return dimensions

    def length_dimension_list(self, tree):
        dimensions = self.dimension_helper(tree)
        return dimensions


# INDEX CREATION
class CreateIndex:
    def create_index(self, tree):
        index_name = None
        if_not_exists = False
        table_name = None
        vector_store_type = None
        index_elem = None

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "uid":
                    index_name = self.visit(child)
                if child.data == "if_not_exists":
                    if_not_exists = True
                elif child.data == "table_name":
                    table_name = self.visit(child)
                    table_ref = TableRef(table_name)
                elif child.data == "vector_store_type":
                    vector_store_type = self.visit(child)
                elif child.data == "index_elem":
                    index_elem = self.visit(child)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        # Projection list of child of index creation.
        project_expr_list = []

        # Parse either a single function call or column list.
        if not isinstance(index_elem, list):
            project_expr_list += [index_elem]
<<<<<<< HEAD
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
        # Projection list of child of index creation.
        project_expr_list = []

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        # Parse either a single function call or column list.
        if not isinstance(index_elem, list):
<<<<<<< HEAD
            function = index_elem
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
            project_expr_list += [index_elem]
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
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
=======
=======
        # Projection list of child of index creation.
        project_expr_list = []

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        # Parse either a single function call or column list.
        if not isinstance(index_elem, list):
<<<<<<< HEAD
            function = index_elem
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
            project_expr_list += [index_elem]
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
=======
        # Projection list of child of index creation.
        project_expr_list = []

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        # Parse either a single function call or column list.
        if not isinstance(index_elem, list):
<<<<<<< HEAD
            function = index_elem
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
            project_expr_list += [index_elem]
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
=======
=======
        # Projection list of child of index creation.
        project_expr_list = []

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        # Parse either a single function call or column list.
        if not isinstance(index_elem, list):
<<<<<<< HEAD
            function = index_elem
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
            project_expr_list += [index_elem]
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

            # Traverse to the tuple value expression.
            while not isinstance(index_elem, TupleValueExpression):
                index_elem = index_elem.children[0]
            index_elem = [index_elem]
        else:
            project_expr_list += index_elem

        # Add tv_expr for projected columns.
        col_list = []
        for tv_expr in index_elem:
            col_list += [ColumnDefinition(tv_expr.name, None, None, None)]

        return CreateIndexStatement(
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
<<<<<<< HEAD
=======
=======
=======
>>>>>>> a6ef863c (feat: create index from projection (#1244))
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
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> a6ef863c (feat: create index from projection (#1244))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
<<<<<<< HEAD
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
>>>>>>> a6ef863c (feat: create index from projection (#1244))
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            index_name,
            if_not_exists,
            table_ref,
            col_list,
            vector_store_type,
            project_expr_list,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            index_name, if_not_exists, table_ref, col_list, vector_store_type, function
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
            index_name,
            if_not_exists,
            table_ref,
            col_list,
            vector_store_type,
            project_expr_list,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
>>>>>>> georgia-tech-db-main
=======
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
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
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
            index_name, if_not_exists, table_ref, col_list, vector_store_type, function
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
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
            index_name,
            if_not_exists,
            table_ref,
            col_list,
            vector_store_type,
            project_expr_list,
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
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> a6ef863c (feat: create index from projection (#1244))
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
=======
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
            index_name, if_not_exists, table_ref, col_list, vector_store_type, function
=======
            index_name, table_ref, col_list, vector_store_type, function
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
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
            index_name,
            if_not_exists,
            table_ref,
            col_list,
            vector_store_type,
            project_expr_list,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        )

    def vector_store_type(self, tree):
        vector_store_type = None
        token = tree.children[1]

        if str.upper(token) == "FAISS":
            vector_store_type = VectorStoreType.FAISS
        elif str.upper(token) == "QDRANT":
            vector_store_type = VectorStoreType.QDRANT
        elif str.upper(token) == "PINECONE":
            vector_store_type = VectorStoreType.PINECONE
        elif str.upper(token) == "PGVECTOR":
            vector_store_type = VectorStoreType.PGVECTOR
        elif str.upper(token) == "CHROMADB":
            vector_store_type = VectorStoreType.CHROMADB
<<<<<<< HEAD
        elif str.upper(token) == "MILVUS":
            vector_store_type = VectorStoreType.MILVUS
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        return vector_store_type


class CreateDatabase:
    def create_database(self, tree):
        database_name = None
        if_not_exists = False
        engine = None
        param_dict = {}

        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "if_not_exists":
                    if_not_exists = True
                elif child.data == "uid":
                    database_name = self.visit(child)
                elif child.data == "create_database_engine_clause":
                    engine, param_dict = self.visit(child)

        create_stmt = CreateDatabaseStatement(
            database_name, if_not_exists, engine, param_dict
        )
        return create_stmt

    def create_database_engine_clause(self, tree):
        engine = None
        param_dict = {}
        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "string_literal":
                    engine = self.visit(child).value
                elif child.data == "colon_param_dict":
                    param_dict = self.visit(child)

        return engine, param_dict


class CreateJob:
    def create_job(self, tree):
        job_name = None
        queries = []
        start_time = None
        end_time = None
        repeat_interval = None
        repeat_period = None
        if_not_exists = False
        for child in tree.children:
            if isinstance(child, Tree):
                if child.data == "if_not_exists":
                    if_not_exists = True
                if child.data == "uid":
                    job_name = self.visit(child)
                if child.data == "job_sql_statements":
                    queries = self.visit(child)
                elif child.data == "start_time":
                    start_time = self.visit(child)
                elif child.data == "end_time":
                    end_time = self.visit(child)
                elif child.data == "repeat_clause":
                    repeat_interval, repeat_period = self.visit(child)

        create_job = CreateJobStatement(
            job_name,
            queries,
            if_not_exists,
            start_time,
            end_time,
            repeat_interval,
            repeat_period,
        )

        return create_job

    def start_time(self, tree):
        return self.visit(tree.children[1]).value

    def end_time(self, tree):
        return self.visit(tree.children[1]).value

    def repeat_clause(self, tree):
        return self.visit(tree.children[1]), self.visit(tree.children[2])
