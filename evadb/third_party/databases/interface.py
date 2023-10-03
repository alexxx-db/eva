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
import importlib
import os
from contextlib import contextmanager
<<<<<<< HEAD

from evadb.executor.executor_utils import ExecutorError
=======
<<<<<<< HEAD
=======

from evadb.executor.executor_utils import ExecutorError
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

<<<<<<< HEAD
from evadb.executor.executor_utils import ExecutorError
>>>>>>> eva-master

<<<<<<< HEAD
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

<<<<<<< HEAD
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
def _get_database_handler(engine: str, **kwargs):
    """
    Return the database handler. User should modify this function for
    their new integrated handlers.
    """

    # Dynamically import the top module.
    try:
        mod = dynamic_import(engine)
    except ImportError:
        req_file = os.path.join(os.path.dirname(__file__), engine, "requirements.txt")
        if os.path.isfile(req_file):
            with open(req_file) as f:
                raise ImportError(f"Please install the following packages {f.read()}")

    if engine == "postgres":
        return mod.PostgresHandler(engine, **kwargs)
    elif engine == "sqlite":
        return mod.SQLiteHandler(engine, **kwargs)
    elif engine == "mysql":
        return mod.MysqlHandler(engine, **kwargs)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
    elif engine == "mariadb":
        return mod.MariaDbHandler(engine, **kwargs)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> eva-master
    elif engine == "mariadb":
        return mod.MariaDbHandler(engine, **kwargs)
    elif engine == "github":
        return mod.GithubHandler(engine, **kwargs)
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
    else:
        raise NotImplementedError(f"Engine {engine} is not supported")


<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
@contextmanager
def get_database_handler(engine: str, **kwargs):
    handler = _get_database_handler(engine, **kwargs)
    try:
        resp = handler.connect()
        if not resp.status:
            raise ExecutorError(f"Cannot establish connection due to {resp.error}")
        yield handler
    finally:
        handler.disconnect()


<<<<<<< HEAD
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
def dynamic_import(handler_dir):
    import_path = f"evadb.third_party.databases.{handler_dir}.{handler_dir}_handler"
    return importlib.import_module(import_path)
