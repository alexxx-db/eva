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
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
        # create a table in the ative database if set
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
        # create a table in the active database if set
>>>>>>> 62080794 (ran spellchecker)
        is_native_table = self.node.table_info.database_name is not None
=======
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
=======
        # create a table in the ative database if set
        is_native_table = self.node.table_info.database_name is not None
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
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
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
        else:
            catalog_entry = create_table_catalog_entry_for_native_table(
                self.node.table_info, self.node.column_list
            )
        storage_engine = StorageEngine.factory(self.db, catalog_entry)
<<<<<<< HEAD

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
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
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
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
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
>>>>>>> eva-master
=======

                    # Populate the table
                    for batch in child.exec():
                        batch.drop_column_alias()
                        storage_engine.write(catalog_entry, batch)
            except Exception as e:
                # rollback if the create call fails
                if create_table_done:
                    storage_engine.drop(catalog_entry)
                raise e
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
