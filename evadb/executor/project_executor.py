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
from typing import Iterator

import pandas as pd

from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 842cc5f8 (fix: Catalog init introduces significant overhead  (#1270))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
from evadb.executor.executor_utils import (
    ExecutorError,
    apply_project,
    instrument_function_expression_cost,
)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from evadb.executor.executor_utils import ExecutorError, apply_project
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 842cc5f8 (fix: Catalog init introduces significant overhead  (#1270))
=======
=======
from evadb.executor.executor_utils import ExecutorError, apply_project
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
from evadb.executor.executor_utils import ExecutorError, apply_project
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
from evadb.models.storage.batch import Batch
from evadb.plan_nodes.project_plan import ProjectPlan


class ProjectExecutor(AbstractExecutor):
    """ """

    def __init__(self, db: EvaDBDatabase, node: ProjectPlan):
        super().__init__(db, node)
        self.target_list = node.target_list

    def exec(self, *args, **kwargs) -> Iterator[Batch]:
        # SELECT expr;
        if len(self.children) == 0:
            # Create a dummy batch with size 1
            dummy_batch = Batch(pd.DataFrame([0]))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
            batch = apply_project(dummy_batch, self.target_list)
=======
            batch = apply_project(dummy_batch, self.target_list, self.catalog())
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
            batch = apply_project(dummy_batch, self.target_list)
>>>>>>> 842cc5f8 (fix: Catalog init introduces significant overhead  (#1270))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
            if not batch.empty():
                yield batch
        # SELECT expr FROM table;
        elif len(self.children) == 1:
            child_executor = self.children[0]
            for batch in child_executor.exec(**kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
                batch = apply_project(batch, self.target_list)
=======
                batch = apply_project(batch, self.target_list, self.catalog())
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
                batch = apply_project(batch, self.target_list)
>>>>>>> 842cc5f8 (fix: Catalog init introduces significant overhead  (#1270))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
                if not batch.empty():
                    yield batch
        else:
            raise ExecutorError("ProjectExecutor has more than 1 children.")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

        # instrument required stats
        instrument_function_expression_cost(self.target_list, self.catalog())
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======

        # instrument required stats
        instrument_function_expression_cost(self.target_list, self.catalog())
>>>>>>> 842cc5f8 (fix: Catalog init introduces significant overhead  (#1270))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
