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
from typing import Callable, Dict, List, Tuple, Union

from thefuzz import process

from evadb.binder.binder_utils import (
    BinderError,
    check_data_source_and_table_are_valid,
    create_table_catalog_entry_for_data_source,
)
from evadb.catalog.catalog_type import TableType
from evadb.catalog.models.column_catalog import ColumnCatalogEntry
from evadb.catalog.models.function_io_catalog import FunctionIOCatalogEntry
from evadb.catalog.models.table_catalog import TableCatalogEntry
from evadb.expression.function_expression import FunctionExpression
from evadb.expression.tuple_value_expression import TupleValueExpression
from evadb.third_party.databases.interface import get_database_handler
from evadb.utils.logging_manager import logger

CatalogColumnType = Union[ColumnCatalogEntry, FunctionIOCatalogEntry]


class StatementBinderContext:
    """
    This context is used to store information that is useful during the process of binding a statement (such as a SELECT statement) to the catalog. It stores the following information:

    Args:
        `_table_alias_map`: Maintains a mapping from table_alias to corresponding
        catalog table entry
        `_derived_table_alias_map`: Maintains a mapping from derived table aliases,
        such as subqueries or function expressions, to column alias maps for all the
        corresponding projected columns. For example, in the following queries, the
        `_derived_table_alias_map` attribute would contain:

        `Select * FROM (SELECT id1, id2 FROM table) AS A` :
            `{A: {id1: table.col1, id2: table.col2}}`
        `Select * FROM video LATERAL JOIN func AS T(a, b)` :
            `{T: {a: func.obj1, b:func.obj2}}`
    """

    def __init__(self, catalog: Callable):
        self._catalog = catalog
        self._table_alias_map: Dict[str, TableCatalogEntry] = dict()
        self._derived_table_alias_map: Dict[str, Dict[str, CatalogColumnType]] = dict()
        self._retrieve_audio = False
        self._retrieve_video = False

    def _check_duplicate_alias(self, alias: str):
        """
        Sanity check: no duplicate alias in table and derived_table
        Arguments:
            alias (str): name of the alias

        Exception:
            Raise exception if found duplication
        """
        if alias in self._derived_table_alias_map or alias in self._table_alias_map:
            err_msg = f"Found duplicate alias {alias}"
            logger.error(err_msg)
            raise BinderError(err_msg)

    def add_table_alias(self, alias: str, database_name: str, table_name: str):
        """
        Add a alias -> table_name mapping
        Arguments:
            alias (str): name of alias
            table_name (str): name of the table
        """
        self._check_duplicate_alias(alias)

        if database_name is not None:
            check_data_source_and_table_are_valid(
                self._catalog(), database_name, table_name
            )

            db_catalog_entry = self._catalog().get_database_catalog_entry(database_name)
            with get_database_handler(
                db_catalog_entry.engine, **db_catalog_entry.params
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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
=======
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
            ) as handler:
                # Assemble columns.
                response = handler.get_columns(table_name)
                if response.error is not None:
                    raise BinderError(response.error)
                column_df = response.data
                table_obj = create_table_catalog_entry_for_data_source(
                    table_name, database_name, column_df
                )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            ) as handler:
                # Assemble columns.
                response = handler.get_columns(table_name)
                if response.error is not None:
                    raise BinderError(response.error)
                column_df = response.data
                table_obj = create_table_catalog_entry_for_data_source(
                    table_name, database_name, column_df
                )
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
            )
            handler.connect()

            # Assemble columns.
            column_df = handler.get_columns(table_name).data
            table_obj = create_table_catalog_entry_for_data_source(
                table_name, column_df
            )
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-master
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
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            ) as handler:
                # Assemble columns.
                response = handler.get_columns(table_name)
                if response.error is not None:
                    raise BinderError(response.error)
                column_df = response.data
                table_obj = create_table_catalog_entry_for_data_source(
                    table_name, database_name, column_df
                )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> eva-source
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
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
            ) as handler:
                # Assemble columns.
                response = handler.get_columns(table_name)
                if response.error is not None:
                    raise BinderError(response.error)
                column_df = response.data
                table_obj = create_table_catalog_entry_for_data_source(
                    table_name, database_name, column_df
                )
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
            ) as handler:
                # Assemble columns.
                response = handler.get_columns(table_name)
                if response.error is not None:
                    raise BinderError(response.error)
                column_df = response.data
                table_obj = create_table_catalog_entry_for_data_source(
                    table_name, database_name, column_df
                )
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
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        else:
            table_obj = self._catalog().get_table_catalog_entry(table_name)

        self._table_alias_map[alias] = table_obj

    def add_derived_table_alias(
        self,
        alias: str,
        target_list: List[
            Union[TupleValueExpression, FunctionExpression, FunctionIOCatalogEntry]
        ],
    ):
        """
        Add a alias -> derived table column mapping
        Arguments:
            alias (str): name of alias
            target_list: list of TupleValueExpression or FunctionExpression or FunctionIOCatalogEntry
        """
        self._check_duplicate_alias(alias)
        col_alias_map = {}
        for expr in target_list:
            if isinstance(expr, FunctionExpression):
                for obj in expr.output_objs:
                    col_alias_map[obj.name] = obj
            elif isinstance(expr, TupleValueExpression):
                col_alias_map[expr.name] = expr.col_object
            else:
                continue

        self._derived_table_alias_map[alias] = col_alias_map

    def get_binded_column(
        self, col_name: str, alias: str = None
    ) -> Tuple[str, CatalogColumnType]:
        """
        Find the binded column object
        Arguments:
            col_name (str): column name
            alias (str): alias name

        Returns:
            A tuple of alias and column object
        """

        # binder is case insensitive
        col_name = col_name.lower()

        def raise_error():
            all_columns = sorted(
                list(set([col for _, col in self._get_all_alias_and_col_name()]))
            )
            res = process.extractOne(col_name, all_columns)
            if res is not None:
                guess_column, _ = res
<<<<<<< HEAD
                err_msg = f"Cannot find column {col_name}. Did you mean {guess_column}? The feasible columns are {all_columns}."
            else:
                err_msg = (
                    f"Cannot find column {col_name}. There are no feasible columns."
=======
                err_msg = f"Cannnot find column {col_name}. Did you mean {guess_column}? The feasible columns are {all_columns}."
            else:
                err_msg = (
                    f"Cannnot find column {col_name}. There are no feasible columns."
>>>>>>> c9e64bc8 (Improve the error message when there is a typo in the column name in the query.  (#1267))
                )
            logger.error(err_msg)
            raise BinderError(err_msg)

        if not alias:
            alias, col_obj = self._search_all_alias_maps(col_name)
        else:
            # search in all alias maps
            col_obj = self._check_table_alias_map(alias, col_name)
            if not col_obj:
                col_obj = self._check_derived_table_alias_map(alias, col_name)

        if col_obj:
            return alias, col_obj

        raise_error()

    def _check_table_alias_map(self, alias, col_name) -> ColumnCatalogEntry:
        """
        Find the column object in table alias map
        Arguments:
            col_name (str): column name
            alias (str): alias name

        Returns:
            column object
        """
        table_obj = self._table_alias_map.get(alias, None)
        if table_obj is not None:
            if table_obj.table_type == TableType.NATIVE_DATA:
                for column_catalog_entry in table_obj.columns:
                    if column_catalog_entry.name == col_name:
                        return column_catalog_entry
            else:
                return self._catalog().get_column_catalog_entry(table_obj, col_name)

    def _check_derived_table_alias_map(self, alias, col_name) -> CatalogColumnType:
        """
        Find the column object in derived table alias map
        Arguments:
            col_name (str): column name
            alias (str): alias name

        Returns:
            column object
        """
        col_objs_map = self._derived_table_alias_map.get(alias, None)
        if col_objs_map is None:
            return None

        for name, obj in col_objs_map.items():
            if name == col_name:
                return obj

    def _get_all_alias_and_col_name(self) -> List[Tuple[str, str]]:
        """
        Return all alias and column objects mapping in the current context
        Returns:
            a list of tuple of alias name, column name
        """
        alias_cols = []
        for alias, table_obj in self._table_alias_map.items():
            alias_cols += list([(alias, col.name) for col in table_obj.columns])
        for alias, col_objs_map in self._derived_table_alias_map.items():
            alias_cols += list([(alias, col_name) for col_name in col_objs_map])
        return alias_cols

    def _search_all_alias_maps(self, col_name: str) -> Tuple[str, CatalogColumnType]:
        """
        Search the alias and column object using column name
        Arguments:
            col_name (str): column name

        Returns:
            A tuple of alias and column object.
        """
        num_alias_matches = 0
        alias_match = None
        match_obj = None
        for alias in self._table_alias_map:
            col_obj = self._check_table_alias_map(alias, col_name)
            if col_obj:
                match_obj = col_obj
                num_alias_matches += 1
                alias_match = alias

        for alias in self._derived_table_alias_map:
            col_obj = self._check_derived_table_alias_map(alias, col_name)
            if col_obj:
                match_obj = col_obj
                num_alias_matches += 1
                alias_match = alias

        if num_alias_matches > 1:
            err_msg = f"Ambiguous Column name {col_name}"
            logger.error(err_msg)
            raise BinderError(err_msg)

        return alias_match, match_obj

    def enable_audio_retrieval(self):
        self._retrieve_audio = True

    def is_retrieve_audio(self):
        return self._retrieve_audio

    def enable_video_retrieval(self):
        self._retrieve_video = True

    def is_retrieve_video(self):
        return self._retrieve_video
