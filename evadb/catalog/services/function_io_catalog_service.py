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

from evadb.catalog.models.function_io_catalog import (
    FunctionIOCatalog,
    FunctionIOCatalogEntry,
)
from evadb.catalog.services.base_service import BaseService
from evadb.utils.logging_manager import logger


class FunctionIOCatalogService(BaseService):
    def __init__(self, db_session: Session):
        super().__init__(FunctionIOCatalog, db_session)

    def get_input_entries_by_function_id(
        self, function_id: int
    ) -> List[FunctionIOCatalogEntry]:
        try:
            result = (
                self.session.execute(
                    select(self.model).filter(
                        self.model._function_id == function_id,
                        self.model._is_input == True,  # noqa
                    )
                )
                .scalars()
                .all()
            )
            return [obj.as_dataclass() for obj in result]
        except Exception as e:
            error = f"Getting inputs for function id {function_id} raised {e}"
            logger.error(error)
            raise RuntimeError(error)

    def get_output_entries_by_function_id(
        self, function_id: int
    ) -> List[FunctionIOCatalogEntry]:
        try:
            result = (
                self.session.execute(
                    select(self.model).filter(
                        self.model._function_id == function_id,
                        self.model._is_input == False,  # noqa
                    )
                )
                .scalars()
                .all()
            )
            return [obj.as_dataclass() for obj in result]
        except Exception as e:
            error = f"Getting outputs for function id {function_id} raised {e}"
            logger.error(error)
            raise RuntimeError(error)

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
    def create_entries(self, io_list: List[FunctionIOCatalogEntry]):
        io_objs = []
=======
    def insert_entries(self, io_list: List[FunctionIOCatalogEntry]):
        """Commit entries to the function_io table

        Arguments:
            io_list (List[FunctionIOCatalogEntry]): List of io info io be added
        """

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
    def create_entries(self, io_list: List[FunctionIOCatalogEntry]):
        io_objs = []
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
        for io in io_list:
            io_obj = FunctionIOCatalog(
                name=io.name,
                type=io.type,
                is_nullable=io.is_nullable,
                array_type=io.array_type,
                array_dimensions=io.array_dimensions,
                is_input=io.is_input,
                function_id=io.function_id,
            )
            io_objs.append(io_obj)
        return io_objs
