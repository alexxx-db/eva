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
from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.parser.set_statement import SetStatement


class SetExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: SetStatement):
        super().__init__(db, node)

    def exec(self, *args, **kwargs):
        # Get method implementation from the config.update_value
        """
        NOTE :- Currently adding adding all configs in 'default' category.
        The idea is to deprecate category to maintain the same format for
        the query as DuckDB and Postgres

        Ref :-
        https://www.postgresql.org/docs/7.0/sql-set.htm
        https://duckdb.org/docs/sql/configuration.html

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
>>>>>>> fb00f6de (ran spellchecker)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        This design change for configuration manager will be taken care of
=======
        This design change for configuation manager will be taken care of
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
        as a separate PR for the issue #1140, where all instances of config use
        will be replaced
        """

        self.catalog().upsert_configuration_catalog_entry(
=======
        This design change for configuation manager will be taken care of
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
        This design change for configuration manager will be taken care of
>>>>>>> 5b27053e (ran spellchecker)
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
        This design change for configuration manager will be taken care of
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> fb00f6de (ran spellchecker)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        as a separate PR for the issue #1140, where all instances of config use
        will be replaced
        """
        self._config.update_value(
            category="default",
<<<<<<< HEAD
<<<<<<< HEAD
            key=self.node.config_name.upper(),
=======
            key=self.node.config_name,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
            key=self.node.config_name,
=======
            key=self.node.config_name.upper(),
>>>>>>> 7dce1d6d (SHOW command for retrieveing configurations (#1264))
=======
            key=self.node.config_name.upper(),
=======
            key=self.node.config_name,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
            key=self.node.config_name.upper(),
=======
            key=self.node.config_name,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            value=self.node.config_value.value,
        )
