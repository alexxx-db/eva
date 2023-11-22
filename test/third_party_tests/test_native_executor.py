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
from test.util import get_evadb_for_testing, shutdown_ray

import pytest

from evadb.executor.executor_utils import ExecutorError
from evadb.server.command_handler import execute_query_fetch_all


@pytest.mark.notparallel
class NativeExecutorTest(unittest.TestCase):
    def setUp(self):
        self.evadb = get_evadb_for_testing()
        # reset the catalog manager before running each test
        self.evadb.catalog().reset()

    def tearDown(self):
        shutdown_ray()
        self._drop_table_in_native_database()
        self._drop_table_in_evadb_database()

    def _create_table_in_native_database(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                CREATE TABLE test_table (
                    name VARCHAR(10),
                    Age INT,
                    comment VARCHAR (100)
                )
            }""",
        )

    def _insert_value_into_native_database(self, col1, col2, col3):
        execute_query_fetch_all(
            self.evadb,
            f"""USE test_data_source {{
                INSERT INTO test_table (
                    name, Age, comment
                ) VALUES (
                    '{col1}', {col2}, '{col3}'
                )
            }}""",
        )

    def _drop_table_in_native_database(self):
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                DROP TABLE IF EXISTS test_table
            }""",
        )
        execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                DROP TABLE IF EXISTS derived_table
            }""",
        )

    def _drop_table_in_evadb_database(self):
        execute_query_fetch_all(
            self.evadb,
            "DROP TABLE IF EXISTS eva_table;",
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

    def _create_evadb_table_using_select_query(self):
        execute_query_fetch_all(
            self.evadb,
            """CREATE TABLE eva_table AS SELECT name, Age FROM test_data_source.test_table;""",
        )

        # check if the create table is successful
        res_batch = execute_query_fetch_all(self.evadb, "Select * from eva_table")
        self.assertEqual(len(res_batch), 2)
        self.assertEqual(res_batch.frames["eva_table.name"][0], "aa")
        self.assertEqual(res_batch.frames["eva_table.age"][0], 1)
        self.assertEqual(res_batch.frames["eva_table.name"][1], "bb")
        self.assertEqual(res_batch.frames["eva_table.age"][1], 2)

    def _create_native_table_using_select_query(self):
        execute_query_fetch_all(
            self.evadb,
            """CREATE TABLE test_data_source.derived_table AS SELECT name, age FROM test_data_source.test_table;""",
        )
        res_batch = execute_query_fetch_all(
            self.evadb,
            "SELECT * FROM test_data_source.derived_table",
        )
        self.assertEqual(len(res_batch), 2)
        self.assertEqual(res_batch.frames["derived_table.name"][0], "aa")
        self.assertEqual(res_batch.frames["derived_table.age"][0], 1)
        self.assertEqual(res_batch.frames["derived_table.name"][1], "bb")
        self.assertEqual(res_batch.frames["derived_table.age"][1], 2)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

    def _create_evadb_table_using_select_query(self):
        execute_query_fetch_all(
            self.evadb,
            """CREATE TABLE eva_table AS SELECT name, Age FROM test_data_source.test_table;""",
        )

        # check if the create table is successful
        res_batch = execute_query_fetch_all(self.evadb, "Select * from eva_table")
        self.assertEqual(len(res_batch), 2)
        self.assertEqual(res_batch.frames["eva_table.name"][0], "aa")
        self.assertEqual(res_batch.frames["eva_table.age"][0], 1)
        self.assertEqual(res_batch.frames["eva_table.name"][1], "bb")
        self.assertEqual(res_batch.frames["eva_table.age"][1], 2)

    def _create_native_table_using_select_query(self):
        execute_query_fetch_all(
            self.evadb,
            """CREATE TABLE test_data_source.derived_table AS SELECT name, age FROM test_data_source.test_table;""",
        )
        res_batch = execute_query_fetch_all(
            self.evadb,
            "SELECT * FROM test_data_source.derived_table",
        )
        self.assertEqual(len(res_batch), 2)
        self.assertEqual(res_batch.frames["derived_table.name"][0], "aa")
        self.assertEqual(res_batch.frames["derived_table.age"][0], 1)
        self.assertEqual(res_batch.frames["derived_table.name"][1], "bb")
        self.assertEqual(res_batch.frames["derived_table.age"][1], 2)

    def _execute_evadb_query(self):
        self._create_table_in_native_database()
        self._insert_value_into_native_database("aa", 1, "aaaa")
        self._insert_value_into_native_database("bb", 2, "bbbb")

        res_batch = execute_query_fetch_all(
            self.evadb,
            "SELECT * FROM test_data_source.test_table",
        )
        self.assertEqual(len(res_batch), 2)
        self.assertEqual(res_batch.frames["test_table.name"][0], "aa")
        self.assertEqual(res_batch.frames["test_table.age"][0], 1)
        self.assertEqual(res_batch.frames["test_table.name"][1], "bb")
        self.assertEqual(res_batch.frames["test_table.age"][1], 2)

        self._create_evadb_table_using_select_query()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        self._create_native_table_using_select_query()
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
        self._create_native_table_using_select_query()
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
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
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
        self._create_native_table_using_select_query()
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
        self._create_native_table_using_select_query()
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
        self._create_native_table_using_select_query()
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
        self._create_native_table_using_select_query()
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
        self._create_native_table_using_select_query()
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
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
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
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
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
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
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        self._create_native_table_using_select_query()
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
        self._create_native_table_using_select_query()
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        self._drop_table_in_native_database()
        self._drop_table_in_evadb_database()

    def _execute_native_query(self):
        self._create_table_in_native_database()
        self._insert_value_into_native_database("aa", 1, "aaaa")

        res_batch = execute_query_fetch_all(
            self.evadb,
            """USE test_data_source {
                SELECT * FROM test_table
            }""",
        )
        self.assertEqual(len(res_batch), 1)

        self.assertEqual(res_batch.frames["name"][0], "aa")
        self.assertEqual(res_batch.frames["age"][0], 1)
        self.assertEqual(res_batch.frames["comment"][0], "aaaa")

        self._drop_table_in_native_database()

    def _raise_error_on_multiple_creation(self):
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "5432",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "postgres",
                    PARAMETERS = {params};"""
        with self.assertRaises(ExecutorError):
            execute_query_fetch_all(self.evadb, query)

    def _raise_error_on_invalid_connection(self):
        params = {
            "user": "xxxxxx",
            "password": "xxxxxx",
            "host": "localhost",
            "port": "5432",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE invaid
                    WITH ENGINE = "postgres",
                    PARAMETERS = {params};"""
        with self.assertRaises(ExecutorError):
            execute_query_fetch_all(self.evadb, query)

    def test_should_run_query_in_postgres(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "5432",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "postgres",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

        # Test error.
        self._raise_error_on_multiple_creation()
        self._raise_error_on_invalid_connection()

<<<<<<< HEAD
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
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_clickhouse(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "9000",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "clickhouse",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    @pytest.mark.skip(
        reason="Snowflake does not come with a free version of account, so integration test is not feasible"
    )
    def test_should_run_query_in_snowflake(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "account": "account_number",
            "database": "EVADB",
            "schema": "SAMPLE_DATA",
            "warehouse": "warehouse",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "snowflake",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
=======
    def test_should_run_query_in_sqlite(self):
        # Create database.
        params = {
            "database": "evadb.db",
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_clickhouse(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "9000",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "clickhouse",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
    def test_should_run_query_in_sqlite(self):
        # Create database.
        params = {
            "database": "evadb.db",
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_clickhouse(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "9000",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "clickhouse",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()


    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
    def test_should_run_query_in_sqlite(self):
        # Create database.
        params = {
            "database": "evadb.db",
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
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
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
=======
    def test_should_run_query_in_sqlite(self):
        # Create database.
        params = {
            "database": "evadb.db",
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
    def test_should_run_query_in_sqlite(self):
        # Create database.
        params = {
            "database": "evadb.db",
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
    def test_should_run_query_in_mariadb(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mariadb",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_sqlite(self):
        # Create database.
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))

        params = {
            "database": f"{current_file_dir}/evadb.db",
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
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "sqlite",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()

    def test_should_run_query_in_mysql(self):
        # Create database.
        params = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "3306",
            "database": "evadb",
        }
        query = f"""CREATE DATABASE test_data_source
                    WITH ENGINE = "mysql",
                    PARAMETERS = {params};"""
        execute_query_fetch_all(self.evadb, query)

        # Test executions.
        self._execute_native_query()
        self._execute_evadb_query()


if __name__ == "__main__":
    unittest.main()
