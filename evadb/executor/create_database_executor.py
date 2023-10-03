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
import pandas as pd

from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.executor.executor_utils import ExecutorError
from evadb.models.storage.batch import Batch
from evadb.parser.create_statement import CreateDatabaseStatement
from evadb.third_party.databases.interface import get_database_handler
from evadb.utils.logging_manager import logger


class CreateDatabaseExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: CreateDatabaseStatement):
        super().__init__(db, node)

    def exec(self, *args, **kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        # Check if database already exists.
        db_catalog_entry = self.catalog().get_database_catalog_entry(
            self.node.database_name
        )

        if db_catalog_entry is not None:
            if self.node.if_not_exists:
                msg = f"{self.node.database_name} already exists, nothing added."
                yield Batch(pd.DataFrame([msg]))
                return
            else:
                raise ExecutorError(f"{self.node.database_name} already exists.")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
        # TODO: handle if_not_exists
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
        # TODO: handle if_not_exists
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)

        logger.debug(
            f"Trying to connect to the provided engine {self.node.engine} with params {self.node.param_dict}"
        )

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        # Check the validity of database entry.
        with get_database_handler(self.node.engine, **self.node.param_dict):
            pass
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Check the validity of database entry.
        with get_database_handler(self.node.engine, **self.node.param_dict):
            pass
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
        # Check if database already exists.
        db_catalog_entry = self.catalog().get_database_catalog_entry(
            self.node.database_name
        )
        if db_catalog_entry is not None:
            raise ExecutorError(f"{self.node.database_name} already exists.")

        # Check the validity of database entry.
        handler = get_database_handler(self.node.engine, **self.node.param_dict)
        resp = handler.connect()
        if not resp.status:
            raise ExecutorError(f"Cannot establish connection due to {resp.error}")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
        # Check the validity of database entry.
        with get_database_handler(self.node.engine, **self.node.param_dict):
            pass
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)

        logger.debug(f"Creating database {self.node}")
        self.catalog().insert_database_catalog_entry(
            self.node.database_name, self.node.engine, self.node.param_dict
        )

        yield Batch(
            pd.DataFrame(
                [
                    f"The database {self.node.database_name} has been successfully created."
                ]
            )
        )
