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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
from typing import List

=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
from typing import List

>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from evadb.catalog.models.function_catalog import FunctionCatalog, FunctionCatalogEntry
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
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
from evadb.catalog.models.utils import (
    FunctionIOCatalogEntry,
    FunctionMetadataCatalogEntry,
)
from evadb.catalog.services.base_service import BaseService
from evadb.catalog.services.function_io_catalog_service import FunctionIOCatalogService
from evadb.catalog.services.function_metadata_catalog_service import (
    FunctionMetadataCatalogService,
)
from evadb.utils.errors import CatalogError
<<<<<<< HEAD
<<<<<<< HEAD
=======
from evadb.catalog.services.base_service import BaseService
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
from evadb.catalog.services.base_service import BaseService
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
from evadb.catalog.services.base_service import BaseService
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
from evadb.catalog.services.base_service import BaseService
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
from evadb.utils.logging_manager import logger


class FunctionCatalogService(BaseService):
    def __init__(self, db_session: Session):
        super().__init__(FunctionCatalog, db_session)
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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
        self._function_io_service = FunctionIOCatalogService(db_session)
        self._function_metadata_service = FunctionMetadataCatalogService(db_session)

    def insert_entry(
        self,
        name: str,
        impl_path: str,
        type: str,
        checksum: str,
        function_io_list: List[FunctionIOCatalogEntry],
        function_metadata_list: List[FunctionMetadataCatalogEntry],
=======

    def insert_entry(
        self, name: str, impl_path: str, type: str, checksum: str
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
        self._function_io_service = FunctionIOCatalogService(db_session)
        self._function_metadata_service = FunctionMetadataCatalogService(db_session)

    def insert_entry(
        self,
        name: str,
        impl_path: str,
        type: str,
        checksum: str,
        function_io_list: List[FunctionIOCatalogEntry],
        function_metadata_list: List[FunctionMetadataCatalogEntry],
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    ) -> FunctionCatalogEntry:
        """Insert a new function entry

        Arguments:
            name (str): name of the function
            impl_path (str): path to the function implementation relative to evadb/function
            type (str): function operator kind, classification or detection or etc
            checksum(str): checksum of the function file content, used for consistency

        Returns:
            FunctionCatalogEntry: Returns the new entry created
        """
        function_obj = self.model(name, impl_path, type, checksum)
        function_obj = function_obj.save(self.session)
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
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

        for function_io in function_io_list:
            function_io.function_id = function_obj._row_id
        io_objs = self._function_io_service.create_entries(function_io_list)
        for function_metadata in function_metadata_list:
            function_metadata.function_id = function_obj._row_id
        metadata_objs = self._function_metadata_service.create_entries(
            function_metadata_list
        )

        # atomic operation for adding table and its corresponding columns.
        try:
            self.session.add_all(io_objs)
            self.session.add_all(metadata_objs)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            self.session.delete(function_obj)
            self.session.commit()
            logger.exception(
                f"Failed to insert entry into function catalog with exception {str(e)}"
            )
            raise CatalogError(e)
        else:
            return function_obj.as_dataclass()
<<<<<<< HEAD
<<<<<<< HEAD
=======
        return function_obj.as_dataclass()
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
        return function_obj.as_dataclass()
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> d4c650b6 (fix: make the table/function catalog insert operation atomic (#1293))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
        return function_obj.as_dataclass()
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
        return function_obj.as_dataclass()
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> bc98b4af (fix: make the table/function catalog insert operation atomic (#1293))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

    def get_entry_by_name(self, name: str) -> FunctionCatalogEntry:
        """return the function entry that matches the name provided.
           None if no such entry found.

        Arguments:
            name (str): name to be searched
        """

        function_obj = self.session.execute(
            select(self.model).filter(self.model._name == name)
        ).scalar_one_or_none()
        if function_obj:
            return function_obj.as_dataclass()
        return None

    def get_entry_by_id(self, id: int, return_alchemy=False) -> FunctionCatalogEntry:
        """return the function entry that matches the id provided.
           None if no such entry found.

        Arguments:
            id (int): id to be searched
        """

        function_obj = self.session.execute(
            select(self.model).filter(self.model._row_id == id)
        ).scalar_one_or_none()
        if function_obj:
            return function_obj if return_alchemy else function_obj.as_dataclass()
        return function_obj

    def delete_entry_by_name(self, name: str):
        """Delete a function entry from the catalog FunctionCatalog

        Arguments:
            name (str): function name to be deleted

        Returns:
            True if successfully deleted else True
        """
        try:
            function_obj = self.session.execute(
                select(self.model).filter(self.model._name == name)
            ).scalar_one()
            function_obj.delete(self.session)
        except Exception as e:
            logger.exception(
                f"Delete function failed for name {name} with error {str(e)}"
            )
            return False
        return True
