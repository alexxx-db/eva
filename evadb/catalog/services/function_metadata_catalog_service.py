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
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from evadb.catalog.models.function_metadata_catalog import (
    FunctionMetadataCatalog,
    FunctionMetadataCatalogEntry,
)
from evadb.catalog.services.base_service import BaseService
from evadb.utils.errors import CatalogError
from evadb.utils.logging_manager import logger


class FunctionMetadataCatalogService(BaseService):
    def __init__(self, db_session: Session):
        super().__init__(FunctionMetadataCatalog, db_session)

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
    def create_entries(self, entries: List[FunctionMetadataCatalogEntry]):
        metadata_objs = []
=======
    def insert_entries(self, entries: List[FunctionMetadataCatalogEntry]):
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
    def create_entries(self, entries: List[FunctionMetadataCatalogEntry]):
        metadata_objs = []
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
        try:
            for entry in entries:
                metadata_obj = FunctionMetadataCatalog(
                    key=entry.key, value=entry.value, function_id=entry.function_id
                )
                metadata_objs.append(metadata_obj)
            return metadata_objs
        except Exception as e:
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
=======
            logger.exception(
                f"Failed to insert entry {entry} into function metadata catalog with exception {str(e)}"
            )
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
            raise CatalogError(e)

    def get_entries_by_function_id(
        self, function_id: int
    ) -> List[FunctionMetadataCatalogEntry]:
        try:
            result = (
                self.session.execute(
                    select(self.model).filter(
                        self.model._function_id == function_id,
                    )
                )
                .scalars()
                .all()
            )
            return [obj.as_dataclass() for obj in result]
        except Exception as e:
            error = f"Getting metadata entries for function id {function_id} raised {e}"
            logger.error(error)
            raise CatalogError(error)
