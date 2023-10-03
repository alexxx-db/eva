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
import contextlib

import pandas as pd

from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.executor.executor_utils import (
    create_table_catalog_entry_for_native_table,
    handle_if_not_exists,
)
from evadb.models.storage.batch import Batch
from evadb.plan_nodes.create_plan import CreatePlan
from evadb.storage.storage_engine import StorageEngine
from evadb.utils.errors import CatalogError
from evadb.utils.logging_manager import logger


class CreateExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: CreatePlan):
        super().__init__(db, node)

    def exec(self, *args, **kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
        # create a table in the ative database if set
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
        # create a table in the active database if set
>>>>>>> 62080794 (ran spellchecker)
        is_native_table = self.node.table_info.database_name is not None
=======
>>>>>>> 5b27053e (ran spellchecker)
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
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
        # create a table in the ative database if set
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
        # create a table in the active database if set
>>>>>>> 62080794 (ran spellchecker)
        is_native_table = self.node.table_info.database_name is not None
=======
<<<<<<< HEAD
>>>>>>> 5b27053e (ran spellchecker)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # create a table in the active database if set
=======
        # create a table in the ative database if set
>>>>>>> f028c383 (release: merge staging into master (#1032))
        is_native_table = self.node.table_info.database_name is not None
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
        if not handle_if_not_exists(
            self.catalog(), self.node.table_info, self.node.if_not_exists
        ):
            create_table_done = False
            logger.debug(f"Creating table {self.node.table_info}")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
        if not handle_if_not_exists(
            self.catalog(), self.node.table_info, self.node.if_not_exists
        ):
            create_table_done = False
            logger.debug(f"Creating table {self.node.table_info}")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        # create a table in the ative database if set
=======
        # create a table in the active database if set
=======
        # create a table in the ative database if set
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
        is_native_table = self.node.table_info.database_name is not None
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
        if not handle_if_not_exists(
            self.catalog(), self.node.table_info, self.node.if_not_exists
        ):
            create_table_done = False
            logger.debug(f"Creating table {self.node.table_info}")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
=======
        if not handle_if_not_exists(
            self.catalog(), self.node.table_info, self.node.if_not_exists
        ):
            create_table_done = False
            logger.debug(f"Creating table {self.node.table_info}")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
=======
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)

        check_if_exists = handle_if_not_exists(
            self.catalog(), self.node.table_info, self.node.if_not_exists
        )
        name = self.node.table_info.table_name
        if check_if_exists:
            yield Batch(pd.DataFrame([f"Table {name} already exists"]))
            return

        create_table_done = False
        logger.debug(f"Creating table {self.node.table_info}")

        if not is_native_table:
            catalog_entry = self.catalog().create_and_insert_table_catalog_entry(
                self.node.table_info, self.node.column_list
            )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
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
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
        else:
            catalog_entry = create_table_catalog_entry_for_native_table(
                self.node.table_info, self.node.column_list
            )
        storage_engine = StorageEngine.factory(self.db, catalog_entry)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
            storage_engine = StorageEngine.factory(self.db, catalog_entry)
            try:
                storage_engine.create(table=catalog_entry)
                create_table_done = True
                if self.children != []:
                    assert (
                        len(self.children) == 1
                    ), "Create table from query expects 1 child, finds {}".format(
                        len(self.children)
                    )
                    child = self.children[0]
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
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)

        try:
            storage_engine.create(table=catalog_entry)
            create_table_done = True

            msg = f"The table {name} has been successfully created"
            if self.children != []:
                assert (
                    len(self.children) == 1
                ), "Create table from query expects 1 child, finds {}".format(
                    len(self.children)
                )
                child = self.children[0]

                rows = 0
                # Populate the table
                for batch in child.exec():
                    batch.drop_column_alias()
                    storage_engine.write(catalog_entry, batch)
                    rows += len(batch)

                msg = (
                    f"The table {name} has been successfully created with {rows} rows."
                )

            yield Batch(pd.DataFrame([msg]))
        except Exception as e:
            # rollback if the create call fails
            with contextlib.suppress(CatalogError):
                if create_table_done:
                    storage_engine.drop(catalog_entry)
<<<<<<< HEAD
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
=======
            # rollback catalog entry, suppress any errors raised by catalog
            with contextlib.suppress(CatalogError):
                self.catalog().delete_table_catalog_entry(catalog_entry)
            raise e
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
