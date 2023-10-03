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
import mysql.connector
import pandas as pd

from evadb.third_party.databases.types import (
    DBHandler,
    DBHandlerResponse,
    DBHandlerStatus,
)


class MysqlHandler(DBHandler):
    def __init__(self, name: str, **kwargs):
        super().__init__(name)
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.user = kwargs.get("user")
        self.password = kwargs.get("password")
        self.database = kwargs.get("database")

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.connection.autocommit = True
            return DBHandlerStatus(status=True)
        except mysql.connector.Error as e:
            return DBHandlerStatus(status=False, error=str(e))

    def disconnect(self):
        if self.connection:
            self.connection.close()

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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
    def get_sqlalchmey_uri(self) -> str:
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
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
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
    def get_sqlalchmey_uri(self) -> str:
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
    def get_sqlalchmey_uri(self) -> str:
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

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
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
    def get_sqlalchmey_uri(self) -> str:
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
    def check_connection(self) -> DBHandlerStatus:
        if self.connection:
            return DBHandlerStatus(status=True)
        else:
            return DBHandlerStatus(status=False, error="Not connected to the database.")

    def get_tables(self) -> DBHandlerResponse:
        if not self.connection:
            return DBHandlerResponse(data=None, error="Not connected to the database.")

        try:
            query = f"SELECT table_name as 'table_name' FROM information_schema.tables WHERE table_schema='{self.database}'"
            tables_df = pd.read_sql_query(query, self.connection)
            return DBHandlerResponse(data=tables_df)
        except mysql.connector.Error as e:
            return DBHandlerResponse(data=None, error=str(e))

    def get_columns(self, table_name: str) -> DBHandlerResponse:
        if not self.connection:
            return DBHandlerResponse(data=None, error="Not connected to the database.")

        try:
            query = f"SELECT column_name as 'name', data_type as dtype FROM information_schema.columns WHERE table_name='{table_name}'"
            columns_df = pd.read_sql_query(query, self.connection)
            columns_df["dtype"] = columns_df["dtype"].apply(self._mysql_to_python_types)
            return DBHandlerResponse(data=columns_df)
        except mysql.connector.Error as e:
            return DBHandlerResponse(data=None, error=str(e))

    def _fetch_results_as_df(self, cursor):
        """
        This is currently the only clean solution that we have found so far.
        Reference to MySQL API: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html
        In short, currently there is no very clean programming way to differentiate
        CREATE, INSERT, SELECT. CREATE and INSERT do not return any result, so calling
        fetchall() on those will yield a programming error. Cursor has an attribute
        rowcount, but it indicates # of rows that are affected. In that case, for both
        INSERT and SELECT rowcount is not 0, so we also cannot use this API to
        differentiate INSERT and SELECT.
        """
        try:
            res = cursor.fetchall()
            if not res:
                return pd.DataFrame({"status": ["success"]})
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
            res_df = pd.DataFrame(
                res, columns=[desc[0].lower() for desc in cursor.description]
            )
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
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
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
            res_df = pd.DataFrame(
                res, columns=[desc[0].lower() for desc in cursor.description]
            )
=======
            res_df = pd.DataFrame(res, columns=[desc[0] for desc in cursor.description])
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
            res_df = pd.DataFrame(
                res, columns=[desc[0].lower() for desc in cursor.description]
            )
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
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
            res_df = pd.DataFrame(res, columns=[desc[0] for desc in cursor.description])
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
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
            res_df = pd.DataFrame(
                res, columns=[desc[0].lower() for desc in cursor.description]
            )
=======
            res_df = pd.DataFrame(res, columns=[desc[0] for desc in cursor.description])
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
            return res_df
        except mysql.connector.ProgrammingError as e:
            if str(e) == "no results to fetch":
                return pd.DataFrame({"status": ["success"]})
            raise e

    def execute_native_query(self, query_string: str) -> DBHandlerResponse:
        if not self.connection:
            return DBHandlerResponse(data=None, error="Not connected to the database.")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query_string)
            return DBHandlerResponse(data=self._fetch_results_as_df(cursor))
        except mysql.connector.Error as e:
            return DBHandlerResponse(data=None, error=str(e))

    def _mysql_to_python_types(self, mysql_type: str):
        mapping = {
            "char": str,
            "varchar": str,
            "text": str,
            "boolean": bool,
            "integer": int,
            "int": int,
            "float": float,
            "double": float,
            # Add more mappings as needed
        }

        if mysql_type in mapping:
            return mapping[mysql_type]
        else:
            raise Exception(
                f"Unsupported column {mysql_type} encountered in the mysql table. Please raise a feature request!"
            )
