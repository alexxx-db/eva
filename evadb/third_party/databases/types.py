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
from dataclasses import dataclass
from typing import Generator

import pandas as pd
from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.orm import sessionmaker


@dataclass
class DBHandlerResponse:
    """
    Represents the response from a database handler containing data and an optional error message.

    Attributes:
        data (pd.DataFrame): A Pandas DataFrame containing the data retrieved from the database.
        error (str, optional): An optional error message indicating any issues encountered during the operation.
    """

    data: pd.DataFrame
    data_generator: Generator = None
    error: str = None


@dataclass
class DBHandlerStatus:
    """
    Represents the status of a database handler operation, along with an optional error message.

    Attributes:
        status (bool): A boolean indicating the success (True) or failure (False) of the operation.
        error (str, optional): An optional error message providing details about any errors that occurred.
    """

    status: bool
    error: str = None


class DBHandler:
    """
    Base class for handling database operations.

    Args:
        name (str): The name associated with the database handler instance.
    """

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

    def disconnect(self):
        """
        Disconnects from the database.

        This method can be overridden in derived classes to perform specific disconnect actions.
        """
        raise NotImplementedError()

    def get_sqlalchmey_uri(self) -> str:
        """
        Return the valid sqlalchemy uri to connect to the database.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    def is_sqlalchmey_compatible(self) -> bool:
        """
<<<<<<< HEAD
        Return  whether the data source is sqlaclchemy compatible
=======
        Return  whether the data source is sqlaclemy compatible
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
    def is_sqlalchmey_compatible(self) -> bool:
        """
<<<<<<< HEAD
<<<<<<< HEAD
        Return  whether the data source is sqlaclemy compatible
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
        Return  whether the data source is sqlaclchemy compatible
>>>>>>> 5b27053e (ran spellchecker)
=======
        Return  whether the data source is sqlaclchemy compatible
=======
        Return  whether the data source is sqlaclemy compatible
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
    def is_sqlalchmey_compatible(self) -> bool:
        """
<<<<<<< HEAD
        Return  whether the data source is sqlaclemy compatible
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
        Return  whether the data source is sqlaclchemy compatible
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> fb00f6de (ran spellchecker)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
    def is_sqlalchmey_compatible(self) -> bool:
        """
        Return  whether the data source is sqlaclemy compatible
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

        Returns:
            A True / False boolean value..
        """
        try:
            self.get_sqlalchmey_uri()
        except NotImplementedError:
            return False
        else:
            return True

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    def check_connection(self) -> DBHandlerStatus:
        """
        Checks the status of the database connection.

        Returns:
            DBHandlerStatus: An instance of DBHandlerStatus indicating the connection status.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

    def get_tables(self) -> DBHandlerResponse:
        """
        Retrieves the list of tables from the database.

        Returns:
            DBHandlerResponse: An instance of DBHandlerResponse containing the list of tables or an error message. Data is in a pandas DataFrame.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

    def get_columns(self, table_name: str) -> DBHandlerResponse:
        """
        Retrieves the columns of a specified table from the database.

        Args:
            table_name (str): The name of the table for which to retrieve columns.

        Returns:
            DBHandlerResponse: An instance of DBHandlerResponse containing the columns or an error message. Data is in a pandas DataFrame. It should have the following two columns: name and dtype. The dtype should be a Python dtype and will default to `str`.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

    def execute_native_query(self, query_string: str) -> DBHandlerResponse:
        """
        Executes the query through the handler's database engine.

        Args:
            query_string (str): The string representation of the native query.

        Returns:
            DBHandlerResponse: An instance of DBHandlerResponse containing the columns or an error message. Data is in a pandas DataFrame.

        Raises:
            NotImplementedError: This method should be implemented in derived classes.
        """
        raise NotImplementedError()

    def select(self, table_name: str) -> DBHandlerResponse:
        """
        Returns a generator that yields the data from the given table, or the data.
        Args:
            table_name (str): name of the table whose data is to be retrieved.
        Returns:
            DBHandlerResponse: An instance of DBHandlerResponse containing the data, data generator, or an error message. Data is in a pandas DataFrame.

        Raises:
            NotImplementedError: The default implementation of this method is for sqlalchemy-supported data source. The data source that does not support sqlalchemy should overwrite this function.
        """
        try:
            uri = self.get_sqlalchmey_uri()
            # Create a metadata object
            engine = create_engine(uri)
            metadata = MetaData()

            Session = sessionmaker(bind=engine)
            session = Session()
            # Retrieve the SQLAlchemy table object for the existing table
            table_to_read = Table(table_name, metadata, autoload_with=engine)
            # TODO: there is a BUG in the SQLAlchemy session management, when there is a function expression in the plan tree, we will update the catalog for its cost, which leads to a SQLAlchemy deadlock if we return a generator here.
            result = session.execute(table_to_read.select()).fetchall()
            session.close()
            # A generator is better, however, the current implementation suffers from deadlock from different SQLAlchemy sessions.
            return DBHandlerResponse(data=result)
        except Exception as e:
            return DBHandlerResponse(data=None, error=str(e))
