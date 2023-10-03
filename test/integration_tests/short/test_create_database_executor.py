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
import os
import unittest
from test.util import get_evadb_for_testing, shutdown_ray

from mock import patch

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
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
from evadb.executor.executor_utils import ExecutorError
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
from evadb.executor.executor_utils import ExecutorError
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
from evadb.executor.executor_utils import ExecutorError
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
from evadb.executor.executor_utils import ExecutorError
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
from evadb.executor.executor_utils import ExecutorError
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
from evadb.executor.executor_utils import ExecutorError
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
from evadb.executor.executor_utils import ExecutorError
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
from evadb.server.command_handler import execute_query_fetch_all


class CreateDatabaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evadb = get_evadb_for_testing()
        # reset the catalog manager before running each test
        cls.evadb.catalog().reset()
        cls.db_path = f"{os.path.dirname(os.path.abspath(__file__))}/testing.db"

    @classmethod
    def tearDownClass(cls):
        shutdown_ray()
        execute_query_fetch_all(cls.evadb, "DROP DATABASE IF EXISTS test_data_source;")
        execute_query_fetch_all(cls.evadb, "DROP DATABASE IF EXISTS demo;")
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)

    def test_create_database_should_add_the_entry(self):
        params = {
            "user": "user",
            "password": "password",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "demo",
        }
        query = """CREATE DATABASE demo_db
                    WITH ENGINE = "postgres",
                    PARAMETERS = {};""".format(
            params
        )
        with patch("evadb.executor.create_database_executor.get_database_handler"):
            execute_query_fetch_all(self.evadb, query)

        db_entry = self.evadb.catalog().get_database_catalog_entry("demo_db")
        self.assertEqual(db_entry.name, "demo_db")
        self.assertEqual(db_entry.engine, "postgres")
        self.assertEqual(db_entry.params, params)

    def test_should_create_sqlite_database(self):
        import os

        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        database_path = f"{current_file_dir}/testing.db"

        if_not_exists = "IF NOT EXISTS"

        params = {
            "database": database_path,
        }
        query = """CREATE DATABASE {} test_data_source
                    WITH ENGINE = "sqlite",
                    PARAMETERS = {};"""

        # Create the database.
        execute_query_fetch_all(self.evadb, query.format(if_not_exists, params))

        # Trying to create the same database should raise an exception.
        with self.assertRaises(ExecutorError):
            execute_query_fetch_all(self.evadb, query.format("", params))

        # Trying to create the same database should warn if "IF NOT EXISTS" is provided.
        execute_query_fetch_all(self.evadb, query.format(if_not_exists, params))


if __name__ == "__main__":
    unittest.main()
