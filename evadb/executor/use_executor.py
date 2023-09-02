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
from typing import Iterator

from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.executor.executor_utils import ExecutorError
from evadb.models.storage.batch import Batch
from evadb.parser.use_statement import UseStatement
from evadb.third_party.databases.interface import get_database_handler


class UseExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: UseStatement):
        super().__init__(db, node)
        self._database_name = node.database_name
        self._query_string = node.query_string

    def exec(self, *args, **kwargs) -> Iterator[Batch]:
        db_catalog_entry = self.db.catalog().get_database_catalog_entry(
            self._database_name
        )

        if db_catalog_entry is None:
            raise ExecutorError(
                f"{self._database_name} data source does not exist. Use CREATE DATABASE to add a new data source."
            )
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
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD

>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
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
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======

>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======

<<<<<<< HEAD
=======

>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
        handler = get_database_handler(
            db_catalog_entry.engine,
            **db_catalog_entry.params,
        )
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))

        with get_database_handler(
            db_catalog_entry.engine, **db_catalog_entry.params
        ) as handler:
            resp = handler.execute_native_query(self._query_string)

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
        with get_database_handler(
            db_catalog_entry.engine, **db_catalog_entry.params
        ) as handler:
            resp = handler.execute_native_query(self._query_string)

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
        if resp and resp.error is None:
            yield Batch(resp.data)
        else:
            raise ExecutorError(resp.error)
