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
from typing import Iterator, List

import numpy as np
import pandas as pd
from sqlalchemy import Column, MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from evadb.catalog.catalog_type import ColumnType
from evadb.catalog.models.table_catalog import TableCatalogEntry
from evadb.catalog.models.utils import ColumnCatalogEntry
from evadb.catalog.schema_utils import SchemaUtils
from evadb.database import EvaDBDatabase
from evadb.models.storage.batch import Batch
from evadb.storage.abstract_storage_engine import AbstractStorageEngine
from evadb.third_party.databases.interface import get_database_handler
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
>>>>>>> fdd1c0e5 (Reenable batch for release (#1302))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.utils.generic_utils import PickleSerializer, rebatch
=======
from evadb.utils.generic_utils import PickleSerializer
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
from evadb.utils.generic_utils import PickleSerializer, rebatch
>>>>>>> 3d009af6 (Reenable batch for release (#1302))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
from evadb.utils.generic_utils import PickleSerializer, rebatch
>>>>>>> 3d009af6 (Reenable batch for release (#1302))
>>>>>>> fdd1c0e5 (Reenable batch for release (#1302))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.utils.logging_manager import logger


# Define a function to create a table
def create_table(uri: str, table_name: str, columns: dict):
    """
    Create a table in the database using sqlalchmey.

    Parameters:
    uri (str): the sqlalchmey uri to connect to the database
    table_name (str): The name of the table to create.
    columns (dict): A dictionary where keys are column names and values are column types.
    """

    # Create a Base class for declarative models
    Base = declarative_base()

    attr_dict = {"__tablename__": table_name}

    # make the first column primary otherwise sqlalchmey complains
    column_name, column_type = columns.popitem()
    attr_dict.update({column_name: Column(column_type.type, primary_key=True)})

    attr_dict.update(columns)

    # dynamic schema generation
    # https://sparrigan.github.io/sql/sqla/2016/01/03/dynamic-tables.html
    _ = type(f"__placeholder_class_name__{table_name}", (Base,), attr_dict)()

    # Create a database engine (SQLite in this example)
    engine = create_engine(uri)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create the table in the database
    Base.metadata.create_all(engine)

    # Commit the changes to the database and close the session
    session.commit()
    session.close()


def _dict_to_sql_row(dict_row: dict, columns: List[ColumnCatalogEntry]):
    # Serialize numpy data
    for col in columns:
        if col.type == ColumnType.NDARRAY:
            dict_row[col.name] = PickleSerializer.serialize(dict_row[col.name])
        elif isinstance(dict_row[col.name], (np.generic,)):
            # Sqlalchemy does not consume numpy generic data types
            # convert numpy datatype to python generic datatype using tolist()
            # eg. np.int64 -> int
            # https://stackoverflow.com/a/53067954
            dict_row[col.name] = dict_row[col.name].tolist()
    return dict_row


def _deserialize_sql_row(sql_row: tuple, columns: List[ColumnCatalogEntry]):
    # Deserialize numpy data

    dict_row = {}
    for idx, col in enumerate(columns):
        # hack, we skip deserializing if sql_row[col.name] is not of type bytes
        if col.type == ColumnType.NDARRAY and isinstance(sql_row[col.name], bytes):
            dict_row[col.name] = PickleSerializer.deserialize(sql_row[idx])
        else:
            dict_row[col.name] = sql_row[idx]
    return dict_row


class NativeStorageEngine(AbstractStorageEngine):
    def __init__(self, db: EvaDBDatabase):
        super().__init__(db)

    def _get_database_catalog_entry(self, database_name):
        db_catalog_entry = self.db.catalog().get_database_catalog_entry(database_name)
        if db_catalog_entry is None:
            raise Exception(
                f"Could not find database with name {database_name}. Please register the database using the `CREATE DATABASE` command."
            )
        return db_catalog_entry

    def create(self, table: TableCatalogEntry):
        try:
            db_catalog_entry = self._get_database_catalog_entry(table.database_name)
            uri = None
            with get_database_handler(
                db_catalog_entry.engine, **db_catalog_entry.params
            ) as handler:
                uri = handler.get_sqlalchmey_uri()
            sqlalchemy_schema = SchemaUtils.xform_to_sqlalchemy_schema(table.columns)
            create_table(uri, table.name, sqlalchemy_schema)
        except Exception as e:
            err_msg = f"Failed to create the table {table.name} in data source {table.database_name} with exception {str(e)}"
            logger.exception(err_msg)
            raise Exception(err_msg)

    def write(self, table: TableCatalogEntry, rows: Batch):
        try:
            db_catalog_entry = self._get_database_catalog_entry(table.database_name)
            with get_database_handler(
                db_catalog_entry.engine, **db_catalog_entry.params
            ) as handler:
                uri = handler.get_sqlalchmey_uri()

            # Create a metadata object
            engine = create_engine(uri)
            metadata = MetaData()

            # Retrieve the SQLAlchemy table object for the existing table
            table_to_update = Table(table.name, metadata, autoload_with=engine)
            columns = rows.frames.keys()
            data = []
            # Todo: validate the data type before inserting into the table
            for record in rows.frames.values:
                row_data = {col: record[idx] for idx, col in enumerate(columns)}
                data.append(_dict_to_sql_row(row_data, table.columns))

            Session = sessionmaker(bind=engine)
            session = Session()
            session.execute(table_to_update.insert(), data)
            session.commit()
            session.close()

        except Exception as e:
            err_msg = f"Failed to write to the table {table.name} in data source {table.database_name} with exception {str(e)}"
            logger.exception(err_msg)
            raise Exception(err_msg)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    def read(
        self, table: TableCatalogEntry, batch_mem_size: int = 30000000
    ) -> Iterator[Batch]:
=======
<<<<<<< HEAD
    def read(self, table: TableCatalogEntry) -> Iterator[Batch]:
=======
    def read(
        self, table: TableCatalogEntry, batch_mem_size: int = 30000000
    ) -> Iterator[Batch]:
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
    def read(
        self, table: TableCatalogEntry, batch_mem_size: int = 30000000
    ) -> Iterator[Batch]:
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        try:
            db_catalog_entry = self._get_database_catalog_entry(table.database_name)
            with get_database_handler(
                db_catalog_entry.engine, **db_catalog_entry.params
            ) as handler:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                handler_response = handler.select(table.name)
                # we prefer the generator/iterator when available
                result = []
                if handler_response.data_generator:
                    result = handler_response.data_generator
                elif handler_response.data:
                    result = handler_response.data
=======
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
>>>>>>> eva-source
=======
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
>>>>>>> georgia-tech-db-main
=======
                handler_response = handler.select(table.name)
                # we prefer the generator/iterator when available
                result = []
                if handler_response.data_generator:
                    result = handler_response.data_generator
                elif handler_response.data:
                    result = handler_response.data
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
>>>>>>> eva-source
=======
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main

                if handler.is_sqlalchmey_compatible():
                    # For sql data source, we can deserialize sql rows into numpy array
                    cols = result[0]._fields
                    index_dict = {
                        element.lower(): index for index, element in enumerate(cols)
                    }
                    try:
                        ordered_columns = sorted(
                            table.columns, key=lambda x: index_dict[x.name.lower()]
                        )
                    except KeyError as e:
                        raise Exception(f"Column mismatch with error {e}")
                    result = (
                        _deserialize_sql_row(row, ordered_columns) for row in result
                    )

<<<<<<< HEAD
<<<<<<< HEAD
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
                for df in rebatch(result, batch_mem_size):
                    yield Batch(pd.DataFrame(df))
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

<<<<<<< HEAD
=======
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))

<<<<<<< HEAD
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
            if data_batch:
                yield Batch(pd.DataFrame(data_batch))

            session.close()
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
                handler_response = handler.select(table.name)
                # we prefer the generator/iterator when available
                result = []
                if handler_response.data_generator:
                    result = handler_response.data_generator
                elif handler_response.data:
                    result = handler_response.data
=======
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))

                if handler.is_sqlalchmey_compatible():
                    # For sql data source, we can deserialize sql rows into numpy array
                    cols = result[0]._fields
                    index_dict = {
                        element.lower(): index for index, element in enumerate(cols)
                    }
                    try:
                        ordered_columns = sorted(
                            table.columns, key=lambda x: index_dict[x.name.lower()]
                        )
                    except KeyError as e:
                        raise Exception(f"Column mismatch with error {e}")
                    result = (
                        _deserialize_sql_row(row, ordered_columns) for row in result
                    )

<<<<<<< HEAD
<<<<<<< HEAD
                for df in rebatch(result, batch_mem_size):
                    yield Batch(pd.DataFrame(df))
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
=======
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))

<<<<<<< HEAD
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
            if data_batch:
                yield Batch(pd.DataFrame(data_batch))

            session.close()
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                handler_response = handler.select(table.name)
                # we prefer the generator/iterator when available
                result = []
                if handler_response.data_generator:
                    result = handler_response.data_generator
                elif handler_response.data:
                    result = handler_response.data
=======
<<<<<<< HEAD
                uri = handler.get_sqlalchmey_uri()
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)

                if handler.is_sqlalchmey_compatible():
                    # For sql data source, we can deserialize sql rows into numpy array
                    cols = result[0]._fields
                    index_dict = {
                        element.lower(): index for index, element in enumerate(cols)
                    }
                    try:
                        ordered_columns = sorted(
                            table.columns, key=lambda x: index_dict[x.name.lower()]
                        )
                    except KeyError as e:
                        raise Exception(f"Column mismatch with error {e}")
                    result = (
                        _deserialize_sql_row(row, ordered_columns) for row in result
                    )

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))
=======
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                for df in rebatch(result, batch_mem_size):
                    yield Batch(pd.DataFrame(df))
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))
=======
                for df in rebatch(result, batch_mem_size):
                    yield Batch(pd.DataFrame(df))
>>>>>>> fdd1c0e5 (Reenable batch for release (#1302))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
=======
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 495ce7d7 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
>>>>>>> 374a5b02 (GitHub Data Source Integration (#1233))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> ae3b0364 (GitHub Data Source Integration (#1233))
=======
=======
>>>>>>> georgia-tech-db-main
=======
            if data_batch:
                yield Batch(pd.DataFrame(data_batch))

            session.close()
=======
                handler_response = handler.select(table.name)
                # we prefer the generator/iterator when available
                result = []
                if handler_response.data_generator:
                    result = handler_response.data_generator
                elif handler_response.data:
                    result = handler_response.data

                if handler.is_sqlalchmey_compatible():
                    # For sql data source, we can deserialize sql rows into numpy array
                    cols = result[0]._fields
                    index_dict = {
                        element.lower(): index for index, element in enumerate(cols)
                    }
                    try:
                        ordered_columns = sorted(
                            table.columns, key=lambda x: index_dict[x.name.lower()]
                        )
                    except KeyError as e:
                        raise Exception(f"Column mismatch with error {e}")
                    result = (
                        _deserialize_sql_row(row, ordered_columns) for row in result
                    )

                for data_batch in result:
                    yield Batch(pd.DataFrame([data_batch]))

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
        except Exception as e:
            err_msg = f"Failed to read the table {table.name} in data source {table.database_name} with exception {str(e)}"
            logger.exception(err_msg)
            raise Exception(err_msg)

    def drop(self, table: TableCatalogEntry):
        try:
            db_catalog_entry = self._get_database_catalog_entry(table.database_name)
            with get_database_handler(
                db_catalog_entry.engine, **db_catalog_entry.params
            ) as handler:
                uri = handler.get_sqlalchmey_uri()

            # Create a metadata object
            engine = create_engine(uri)
            metadata = MetaData()
            Session = sessionmaker(bind=engine)
            session = Session()
            # Retrieve the SQLAlchemy table object for the existing table
            table_to_remove = Table(table.name, metadata, autoload_with=engine)

            table_to_remove.drop(engine)
            session.commit()
            session.close()
        except Exception as e:
            err_msg = f"Failed to drop the table {table.name} in data source {table.database_name} with exception {str(e)}"
            logger.error(err_msg)
            raise Exception(err_msg)
