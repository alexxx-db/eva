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
from evadb.parser.show_statement import ShowStatement
from evadb.parser.types import ShowType


##################################################################
# SHOW STATEMENT
##################################################################
class Show:
    def show_statement(self, tree):
        token = tree.children[1]

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
        if isinstance(token, str) and str.upper(token) == "FUNCTIONS":
            return ShowStatement(show_type=ShowType.FUNCTIONS)
        elif isinstance(token, str) and str.upper(token) == "TABLES":
=======
        if str.upper(token) == "FUNCTIONS":
            return ShowStatement(show_type=ShowType.FUNCTIONS)
        elif str.upper(token) == "TABLES":
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
            return ShowStatement(show_type=ShowType.TABLES)
        elif isinstance(token, str) and str.upper(token) == "DATABASES":
            return ShowStatement(show_type=ShowType.DATABASES)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
        if isinstance(token, str) and str.upper(token) == "FUNCTIONS":
            return ShowStatement(show_type=ShowType.FUNCTIONS)
        elif isinstance(token, str) and str.upper(token) == "TABLES":
=======
        if str.upper(token) == "FUNCTIONS":
            return ShowStatement(show_type=ShowType.FUNCTIONS)
        elif str.upper(token) == "TABLES":
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
            return ShowStatement(show_type=ShowType.TABLES)
<<<<<<< HEAD
>>>>>>> 7dce1d6d (SHOW command for retrieveing configurations (#1264))
=======
        elif isinstance(token, str) and str.upper(token) == "DATABASES":
            return ShowStatement(show_type=ShowType.DATABASES)
>>>>>>> 9db09fc0 (feat: add support for show databases (#1295))
        elif token is not None:
            return ShowStatement(show_type=ShowType.CONFIG, show_val=self.visit(token))
