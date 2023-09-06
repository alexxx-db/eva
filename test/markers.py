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

import os
import sys

import pytest

from evadb.utils.generic_utils import (
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
    is_chromadb_available,
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
    is_chromadb_available,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
    is_chromadb_available,
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
    is_forecast_available,
    is_gpu_available,
    is_ludwig_available,
    is_pinecone_available,
    is_qdrant_available,
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
    is_replicate_available,
    is_sklearn_available,
    is_xgboost_available,
<<<<<<< HEAD
=======
    is_sklearn_available,
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
)

asyncio_skip_marker = pytest.mark.skipif(
    sys.version_info < (3, 8), reason="Test case requires asyncio support"
)

qdrant_skip_marker = pytest.mark.skipif(
    is_qdrant_available() is False,
    reason="qdrant requires grcpio which is broken on 3.11",
)

pinecone_skip_marker = pytest.mark.skipif(
    is_pinecone_available() is False,
    reason="Skipping since pinecone is not installed",
)

chromadb_skip_marker = pytest.mark.skipif(
    is_chromadb_available() is False,
    reason="Skipping since chromadb is not installed",
)

windows_skip_marker = pytest.mark.skipif(
    sys.platform == "win32", reason="Test case not supported on Windows"
)

linux_skip_marker = pytest.mark.skipif(
    sys.platform == "linux", reason="Test case not supported on Linux"
)

macos_skip_marker = pytest.mark.skipif(
    "darwin" in sys.platform, reason="Test case not supported on MacOS"
)

memory_skip_marker = pytest.mark.skipif(
    sys.platform == "linux", reason="Test case consumes too much memory"
)

ray_skip_marker = pytest.mark.skipif(
    os.environ.get("ray") is None, reason="Run only if Ray is enabled"
)

redundant_test_skip_marker = pytest.mark.skipif(
    sys.platform == "linux",
    reason="Test case is duplicate. Disabling to speed up test suite",
)

ocr_skip_marker = pytest.mark.skip(
    reason="We do not have built-in support for OCR",
)

gpu_skip_marker = pytest.mark.skipif(
    is_gpu_available() is False, reason="Run only if gpu is available"
)

ludwig_skip_marker = pytest.mark.skipif(
    is_ludwig_available() is False, reason="Run only if ludwig is available"
)

sklearn_skip_marker = pytest.mark.skipif(
    is_sklearn_available() is False, reason="Run only if sklearn is available"
)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
xgboost_skip_marker = pytest.mark.skipif(
    is_xgboost_available() is False, reason="Run only if xgboost is available"
)

<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
chatgpt_skip_marker = pytest.mark.skip(
    reason="requires chatgpt",
)

forecast_skip_marker = pytest.mark.skipif(
    is_forecast_available() is False,
    reason="Run only if forecasting packages available",
)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))

stable_diffusion_skip_marker = pytest.mark.skipif(
    is_replicate_available() is False, reason="requires replicate"
)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
