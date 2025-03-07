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
from pathlib import Path

import pandas as pd

from evadb.catalog.catalog_type import VectorStoreType
from evadb.catalog.sql_config import ROW_NUM_COLUMN
from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.executor.executor_utils import ExecutorError, handle_vector_store_params
from evadb.expression.function_expression import FunctionExpression
from evadb.models.storage.batch import Batch
from evadb.plan_nodes.create_index_plan import CreateIndexPlan
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
from evadb.storage.storage_engine import StorageEngine
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
>>>>>>> a6ef863c (feat: create index from projection (#1244))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 277161e7 (feat: create index from projection (#1244))
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
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.third_party.databases.interface import get_database_handler
from evadb.third_party.vector_stores.types import FeaturePayload
from evadb.third_party.vector_stores.utils import VectorStoreFactory
from evadb.utils.logging_manager import logger


class CreateIndexExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: CreateIndexPlan):
        super().__init__(db, node)

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
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        self.name = self.node.name
        self.if_not_exists = self.node.if_not_exists
        self.table_ref = self.node.table_ref
        self.col_list = self.node.col_list
        self.vector_store_type = self.node.vector_store_type
        self.project_expr_list = self.node.project_expr_list
        self.index_def = self.node.index_def

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
    def exec(self, *args, **kwargs):
        # Vector type specific creation.
        if self.vector_store_type == VectorStoreType.PGVECTOR:
=======
    def exec(self, *args, **kwargs):
        # Vector type specific creation.
        if self.node.vector_store_type == VectorStoreType.PGVECTOR:
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
    def exec(self, *args, **kwargs):
        # Vector type specific creation.
        if self.vector_store_type == VectorStoreType.PGVECTOR:
>>>>>>> da04707f (feat: insertion update index (#1246))
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            self._create_native_index()
        else:
            self._create_evadb_index()

        yield Batch(
            pd.DataFrame([f"Index {self.name} successfully added to the database."])
        )

    # Create index through the native storage engine.
    def _create_native_index(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
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
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        table = self.table_ref.table
=======
        table = self.node.table_ref.table
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
        table = self.table_ref.table
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
        table = self.table_ref.table
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        db_catalog_entry = self.catalog().get_database_catalog_entry(
            table.database_name
        )

        with get_database_handler(
            db_catalog_entry.engine, **db_catalog_entry.params
        ) as handler:
            # As other libraries, we default to HNSW and L2 distance.
            resp = handler.execute_native_query(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
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
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                f"""CREATE INDEX {self.name} ON {table.table_name}
                    USING hnsw ({self.col_list[0].name} vector_l2_ops)"""
=======
                f"""CREATE INDEX {self.node.name} ON {table.table_name}
                    USING hnsw ({self.node.col_list[0].name} vector_l2_ops)"""
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
                f"""CREATE INDEX {self.name} ON {table.table_name}
                    USING hnsw ({self.col_list[0].name} vector_l2_ops)"""
>>>>>>> da04707f (feat: insertion update index (#1246))
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            )
            if resp.error is not None:
                raise ExecutorError(
                    f"Native engine create index encounters error: {resp.error}"
                )

    # On-disk saving path for EvaDB index.
    def _get_evadb_index_save_path(self) -> Path:
<<<<<<< HEAD
        index_dir = Path(self.db.catalog().get_configuration_catalog_value("index_dir"))
=======
        index_dir = Path(self.config.get_value("storage", "index_dir"))
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        if not index_dir.exists():
            index_dir.mkdir(parents=True, exist_ok=True)
        return str(
            index_dir / Path("{}_{}.index".format(self.vector_store_type, self.name))
        )

    # Create EvaDB index.
    def _create_evadb_index(self):
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
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        # Find function expression.
        function_expression, function_expression_signature = None, None
        for project_expr in self.project_expr_list:
            if isinstance(project_expr, FunctionExpression):
                function_expression = project_expr
                function_expression_signature = project_expr.signature()
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
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
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
        if self.catalog().get_index_catalog_entry_by_name(self.node.name):
            msg = f"Index {self.node.name} already exists."
            if self.node.if_not_exists:
                logger.warn(msg)
                return
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
            else:
                logger.error(msg)
                raise ExecutorError(msg)

        index = None
        index_path = self._get_evadb_index_save_path()

        try:
            # Get feature tables.
            feat_catalog_entry = self.node.table_ref.table.table_obj
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

        # Get feature tables.
        feat_tb_catalog_entry = self.table_ref.table.table_obj

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Get feature column.
        feat_col_name = self.col_list[0].name
        feat_col_catalog_entry = [
            col for col in feat_tb_catalog_entry.columns if col.name == feat_col_name
        ][0]

        if function_expression is not None:
            feat_col_name = function_expression.output_objs[0].name

        index_catalog_entry = self.catalog().get_index_catalog_entry_by_name(self.name)
        index_path = self._get_evadb_index_save_path()

        if index_catalog_entry is not None:
            msg = f"Index {self.name} already exists."
            if self.if_not_exists:
                if (
                    index_catalog_entry.feat_column == feat_col_catalog_entry
                    and index_catalog_entry.function_signature
                    == function_expression_signature
                    and index_catalog_entry.type == self.node.vector_store_type
                ):
                    # Only update index if everything matches.
                    logger.warn(msg + " It will be updated on existing table.")
                    index = VectorStoreFactory.init_vector_store(
                        self.vector_store_type,
                        self.name,
                        **handle_vector_store_params(
                            self.vector_store_type, index_path
                        ),
                    )
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
            storage_engine = StorageEngine.factory(self.db, feat_catalog_entry)
            for input_batch in storage_engine.read(feat_catalog_entry):
                if self.node.function:
                    # Create index through function expression.
                    # Function(input column) -> 2 dimension feature vector.
                    input_batch.modify_column_alias(feat_catalog_entry.name.lower())
                    feat_batch = self.node.function.evaluate(input_batch)
                    feat_batch.drop_column_alias()
                    input_batch.drop_column_alias()
                    feat = feat_batch.column_as_numpy_array("features")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
                else:
                    # Skip index update if CREATE INDEX runs on a different index.
                    logger.warn(msg)
                    return
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
            else:
                logger.error(msg)
                raise ExecutorError(msg)
        else:
            index = None

<<<<<<< HEAD
        try:
<<<<<<< HEAD
<<<<<<< HEAD
            # Get feature tables.
            feat_catalog_entry = self.node.table_ref.table.table_obj
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

        # Get feature tables.
        feat_tb_catalog_entry = self.table_ref.table.table_obj

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
        # Get feature column.
        feat_col_name = self.col_list[0].name
        feat_col_catalog_entry = [
            col for col in feat_tb_catalog_entry.columns if col.name == feat_col_name
        ][0]

        if function_expression is not None:
            feat_col_name = function_expression.output_objs[0].name

        index_catalog_entry = self.catalog().get_index_catalog_entry_by_name(self.name)
        index_path = self._get_evadb_index_save_path()

        if index_catalog_entry is not None:
            msg = f"Index {self.name} already exists."
            if self.if_not_exists:
                if (
                    index_catalog_entry.feat_column == feat_col_catalog_entry
                    and index_catalog_entry.function_signature
                    == function_expression_signature
                    and index_catalog_entry.type == self.node.vector_store_type
                ):
                    # Only update index if everything matches.
                    logger.warn(msg + " It will be updated on existing table.")
                    index = VectorStoreFactory.init_vector_store(
                        self.vector_store_type,
                        self.name,
                        **handle_vector_store_params(
                            self.vector_store_type, index_path
                        ),
                    )
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
<<<<<<< HEAD
            storage_engine = StorageEngine.factory(self.db, feat_catalog_entry)
            for input_batch in storage_engine.read(feat_catalog_entry):
                if self.node.function:
                    # Create index through function expression.
                    # Function(input column) -> 2 dimension feature vector.
                    input_batch.modify_column_alias(feat_catalog_entry.name.lower())
                    feat_batch = self.node.function.evaluate(input_batch)
                    feat_batch.drop_column_alias()
                    input_batch.drop_column_alias()
                    feat = feat_batch.column_as_numpy_array("features")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
                else:
                    # Skip index update if CREATE INDEX runs on a different index.
                    logger.warn(msg)
                    return
>>>>>>> da04707f (feat: insertion update index (#1246))
            else:
                logger.error(msg)
                raise ExecutorError(msg)
        else:
            index = None

<<<<<<< HEAD
        try:
<<<<<<< HEAD
<<<<<<< HEAD
            # Get feature tables.
            feat_catalog_entry = self.node.table_ref.table.table_obj
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

        # Get feature tables.
        feat_tb_catalog_entry = self.table_ref.table.table_obj

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Get feature column.
        feat_col_name = self.col_list[0].name
        feat_col_catalog_entry = [
            col for col in feat_tb_catalog_entry.columns if col.name == feat_col_name
        ][0]

        if function_expression is not None:
            feat_col_name = function_expression.output_objs[0].name

        index_catalog_entry = self.catalog().get_index_catalog_entry_by_name(self.name)
        index_path = self._get_evadb_index_save_path()

        if index_catalog_entry is not None:
            msg = f"Index {self.name} already exists."
            if self.if_not_exists:
                if (
                    index_catalog_entry.feat_column == feat_col_catalog_entry
                    and index_catalog_entry.function_signature
                    == function_expression_signature
                    and index_catalog_entry.type == self.node.vector_store_type
                ):
                    # Only update index if everything matches.
                    logger.warn(msg + " It will be updated on existing table.")
                    index = VectorStoreFactory.init_vector_store(
                        self.vector_store_type,
                        self.name,
                        **handle_vector_store_params(
                            self.vector_store_type, index_path, self.catalog
                        ),
                    )
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
=======
<<<<<<< HEAD
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a3f66ab5 (feat: insertion update index (#1246))
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
            storage_engine = StorageEngine.factory(self.db, feat_catalog_entry)
            for input_batch in storage_engine.read(feat_catalog_entry):
                if self.node.function:
                    # Create index through function expression.
                    # Function(input column) -> 2 dimension feature vector.
                    input_batch.modify_column_alias(feat_catalog_entry.name.lower())
                    feat_batch = self.node.function.evaluate(input_batch)
                    feat_batch.drop_column_alias()
                    input_batch.drop_column_alias()
                    feat = feat_batch.column_as_numpy_array("features")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
                else:
                    # Skip index update if CREATE INDEX runs on a different index.
                    logger.warn(msg)
                    return
            else:
                logger.error(msg)
                raise ExecutorError(msg)
        else:
            index = None

<<<<<<< HEAD
        try:
            # Add features to index.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a3f66ab5 (feat: insertion update index (#1246))
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)

        # Get feature tables.
        feat_tb_catalog_entry = self.table_ref.table.table_obj
>>>>>>> eva-source

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Get feature column.
        feat_col_name = self.col_list[0].name
        feat_col_catalog_entry = [
            col for col in feat_tb_catalog_entry.columns if col.name == feat_col_name
        ][0]

        if function_expression is not None:
            feat_col_name = function_expression.output_objs[0].name

        index_catalog_entry = self.catalog().get_index_catalog_entry_by_name(self.name)
        index_path = self._get_evadb_index_save_path()

        if index_catalog_entry is not None:
            msg = f"Index {self.name} already exists."
            if self.if_not_exists:
                if (
                    index_catalog_entry.feat_column == feat_col_catalog_entry
                    and index_catalog_entry.function_signature
                    == function_expression_signature
                    and index_catalog_entry.type == self.node.vector_store_type
                ):
                    # Only update index if everything matches.
                    logger.warn(msg + " It will be updated on existing table.")
                    index = VectorStoreFactory.init_vector_store(
                        self.vector_store_type,
                        self.name,
                        **handle_vector_store_params(
                            self.vector_store_type, index_path
                        ),
                    )
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
            # Add features to index.
<<<<<<< HEAD
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
=======
>>>>>>> a3f66ab5 (feat: insertion update index (#1246))
>>>>>>> da04707f (feat: insertion update index (#1246))
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6ef863c (feat: create index from projection (#1244))
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
>>>>>>> georgia-tech-db-main
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
<<<<<<< HEAD
            storage_engine = StorageEngine.factory(self.db, feat_catalog_entry)
            for input_batch in storage_engine.read(feat_catalog_entry):
                if self.node.function:
                    # Create index through function expression.
                    # Function(input column) -> 2 dimension feature vector.
                    input_batch.modify_column_alias(feat_catalog_entry.name.lower())
                    feat_batch = self.node.function.evaluate(input_batch)
                    feat_batch.drop_column_alias()
                    input_batch.drop_column_alias()
                    feat = feat_batch.column_as_numpy_array("features")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
                else:
                    # Skip index update if CREATE INDEX runs on a different index.
                    logger.warn(msg)
                    return
>>>>>>> da04707f (feat: insertion update index (#1246))
            else:
                logger.error(msg)
                raise ExecutorError(msg)
        else:
            index = None

<<<<<<< HEAD
=======
<<<<<<< HEAD
        try:
<<<<<<< HEAD
<<<<<<< HEAD
            # Get feature tables.
            feat_catalog_entry = self.node.table_ref.table.table_obj
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

        # Get feature tables.
        feat_tb_catalog_entry = self.table_ref.table.table_obj

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Get feature column.
        feat_col_name = self.col_list[0].name
        feat_col_catalog_entry = [
            col for col in feat_tb_catalog_entry.columns if col.name == feat_col_name
        ][0]

        if function_expression is not None:
            feat_col_name = function_expression.output_objs[0].name

        index_catalog_entry = self.catalog().get_index_catalog_entry_by_name(self.name)
        index_path = self._get_evadb_index_save_path()

        if index_catalog_entry is not None:
            msg = f"Index {self.name} already exists."
            if self.if_not_exists:
                if (
                    index_catalog_entry.feat_column == feat_col_catalog_entry
                    and index_catalog_entry.function_signature
                    == function_expression_signature
                    and index_catalog_entry.type == self.node.vector_store_type
                ):
                    # Only update index if everything matches.
                    logger.warn(msg + " It will be updated on existing table.")
                    index = VectorStoreFactory.init_vector_store(
                        self.vector_store_type,
                        self.name,
                        **handle_vector_store_params(
                            self.vector_store_type, index_path
                        ),
                    )
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
=======
<<<<<<< HEAD
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a3f66ab5 (feat: insertion update index (#1246))
=======
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

            # Add features to index.
            # TODO: batch size is hardcoded for now.
            input_dim = -1
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
            storage_engine = StorageEngine.factory(self.db, feat_catalog_entry)
            for input_batch in storage_engine.read(feat_catalog_entry):
                if self.node.function:
                    # Create index through function expression.
                    # Function(input column) -> 2 dimension feature vector.
                    input_batch.modify_column_alias(feat_catalog_entry.name.lower())
                    feat_batch = self.node.function.evaluate(input_batch)
                    feat_batch.drop_column_alias()
                    input_batch.drop_column_alias()
                    feat = feat_batch.column_as_numpy_array("features")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
                else:
                    # Skip index update if CREATE INDEX runs on a different index.
                    logger.warn(msg)
                    return
            else:
                logger.error(msg)
                raise ExecutorError(msg)
        else:
            index = None

<<<<<<< HEAD
        try:
            # Add features to index.
=======
            # Find function expression.
            function_expression = None
            for project_expr in self.node.project_expr_list:
                if isinstance(project_expr, FunctionExpression):
                    function_expression = project_expr

            if function_expression is not None:
                feat_col_name = function_expression.output_objs[0].name

=======
>>>>>>> da04707f (feat: insertion update index (#1246))
            # Add features to index.
<<<<<<< HEAD
            # TODO: batch size is hardcoded for now.
            input_dim = -1
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
=======
>>>>>>> a3f66ab5 (feat: insertion update index (#1246))
>>>>>>> da04707f (feat: insertion update index (#1246))
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
=======
>>>>>>> eva-source
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
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
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
            for input_batch in self.children[0].exec():
                input_batch.drop_column_alias()
                feat = input_batch.column_as_numpy_array(feat_col_name)
>>>>>>> 277161e7 (feat: create index from projection (#1244))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> a6ef863c (feat: create index from projection (#1244))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> a6ef863c (feat: create index from projection (#1244))
>>>>>>> a747c7e3 (feat: create index from projection (#1244))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                row_num = input_batch.column_as_numpy_array(ROW_NUM_COLUMN)

                for i in range(len(input_batch)):
                    row_feat = feat[i].reshape(1, -1)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
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
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

                    # Create new index if not exists.
                    if index is None:
                        input_dim = row_feat.shape[1]
                        index = VectorStoreFactory.init_vector_store(
                            self.vector_store_type,
                            self.name,
                            **handle_vector_store_params(
                                self.vector_store_type, index_path, self.catalog
=======
<<<<<<< HEAD
=======

                    # Create new index if not exists.
>>>>>>> da04707f (feat: insertion update index (#1246))
                    if index is None:
                        input_dim = row_feat.shape[1]
                        index = VectorStoreFactory.init_vector_store(
                            self.vector_store_type,
                            self.name,
                            **handle_vector_store_params(
<<<<<<< HEAD
                                self.node.vector_store_type, index_path
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
                                self.vector_store_type, index_path
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======

                    # Create new index if not exists.
>>>>>>> da04707f (feat: insertion update index (#1246))
                    if index is None:
                        input_dim = row_feat.shape[1]
                        index = VectorStoreFactory.init_vector_store(
                            self.vector_store_type,
                            self.name,
                            **handle_vector_store_params(
<<<<<<< HEAD
                                self.node.vector_store_type, index_path
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
                                self.vector_store_type, index_path
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
                                self.vector_store_type, index_path
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> georgia-tech-db-main
                    if index is None:
                        input_dim = row_feat.shape[1]
                        index = VectorStoreFactory.init_vector_store(
                            self.node.vector_store_type,
                            self.node.name,
                            **handle_vector_store_params(
                                self.node.vector_store_type, index_path
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                            ),
                        )
                        index.create(input_dim)

                    # Row ID for mapping back to the row.
                    index.add([FeaturePayload(row_num[i], row_feat)])

            # Persist index.
            index.persist()

            # Save to catalog.
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
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
            if index_catalog_entry is None:
                self.catalog().insert_index_catalog_entry(
                    self.name,
                    index_path,
                    self.vector_store_type,
                    feat_col_catalog_entry,
                    function_expression_signature,
                    self.index_def,
                )
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
            self.catalog().insert_index_catalog_entry(
                self.node.name,
                index_path,
                self.node.vector_store_type,
                feat_column,
                function_expression.signature()
                if function_expression is not None
                else None,
                self.node.index_def,
            )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
=======
=======
>>>>>>> da04707f (feat: insertion update index (#1246))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
            self.catalog().insert_index_catalog_entry(
                self.node.name,
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
                index_path,
                self.node.vector_store_type,
                feat_column,
                function_expression.signature()
                if function_expression is not None
                else None,
                self.node.index_def,
            )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
            self.catalog().insert_index_catalog_entry(
                self.node.name,
                index_path,
                self.node.vector_store_type,
                feat_column,
                function_expression.signature()
                if function_expression is not None
                else None,
                self.node.index_def,
            )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> a590a82c (feat: insertion update index (#1246))
=======
                self.index_path,
=======
                index_path,
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
                self.node.vector_store_type,
                feat_column,
                function_expression.signature()
                if function_expression is not None
                else None,
                self.node.index_def,
            )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
        except Exception as e:
            # Delete index.
            if index:
                index.delete()

            # Throw exception back to user.
            raise ExecutorError(str(e))
