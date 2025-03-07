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

import unittest
from test.util import get_evadb_for_testing
from unittest.mock import patch

import pytest

from evadb.catalog.models.utils import DatabaseCatalogEntry
from evadb.server.command_handler import execute_query_fetch_all


class NativeQueryResponse:
    def __init__(self):
        self.error = None
        self.data = None


@pytest.mark.notparallel
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
class SQLiteNativeStorageEngineTest(unittest.TestCase):
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
class SQLiteNativeStorageEngineTest(unittest.TestCase):
=======
class SQLiiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
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
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
class SQLiiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
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
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
=======
class SQLiiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
=======
=======
class SQLiteNativeStorageEngineTest(unittest.TestCase):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_sqlite_params(self):
        return {
            "database": "evadb.db",
        }

    def setUp(self):
        connection_params = self.get_sqlite_params()
        self.evadb = get_evadb_for_testing()

        # Create all class level patches
        self.get_database_catalog_entry_patcher = patch(
            "evadb.catalog.catalog_manager.CatalogManager.get_database_catalog_entry"
        )
        self.get_database_catalog_entry_mock = (
            self.get_database_catalog_entry_patcher.start()
        )

        self.execute_native_query_patcher = patch(
            "evadb.third_party.databases.sqlite.sqlite_handler.SQLiteHandler.execute_native_query"
        )
        self.execute_native_query_mock = self.execute_native_query_patcher.start()

        self.connect_patcher = patch(
            "evadb.third_party.databases.sqlite.sqlite_handler.SQLiteHandler.connect"
        )
        self.connect_mock = self.connect_patcher.start()

        self.disconnect_patcher = patch(
            "evadb.third_party.databases.sqlite.sqlite_handler.SQLiteHandler.disconnect"
        )
        self.disconnect_mock = self.disconnect_patcher.start()

        # set return values
        self.execute_native_query_mock.return_value = NativeQueryResponse()
        self.get_database_catalog_entry_mock.return_value = DatabaseCatalogEntry(
            name="test_data_source", engine="sqlite", params=connection_params, row_id=1
        )

    def tearDown(self):
        self.get_database_catalog_entry_patcher.stop()
        self.execute_native_query_patcher.stop()
        self.connect_patcher.stop()
        self.disconnect_patcher.stop()

    def test_execute_sqlite_select_query(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                SELECT * FROM test_table
            }""",
        )

        self.connect_mock.assert_called_once()
        self.execute_native_query_mock.assert_called_once()
        self.get_database_catalog_entry_mock.assert_called_once()
        self.disconnect_mock.assert_called_once()

    def test_execute_sqlite_insert_query(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                INSERT INTO test_table (
                    name, age, comment
                ) VALUES (
                    'val', 5, 'testing'
                )
            }""",
        )
        self.connect_mock.assert_called_once()
        self.execute_native_query_mock.assert_called_once()
        self.get_database_catalog_entry_mock.assert_called_once()
        self.disconnect_mock.assert_called_once()

    def test_execute_sqlite_update_query(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                UPDATE test_table
                SET comment = 'update'
                WHERE age > 5
            }""",
        )

        self.connect_mock.assert_called_once()
        self.execute_native_query_mock.assert_called_once()
        self.get_database_catalog_entry_mock.assert_called_once()
        self.disconnect_mock.assert_called_once()

    def test_execute_sqlite_delete_query(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                DELETE FROM test_table
                WHERE age < 5
            }""",
        )

        self.connect_mock.assert_called_once()
        self.execute_native_query_mock.assert_called_once()
        self.get_database_catalog_entry_mock.assert_called_once()
        self.disconnect_mock.assert_called_once()
