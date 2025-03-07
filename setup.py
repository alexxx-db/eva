###############################
### EvaDB PACKAGAGING
###############################

import io
import os

# to read contents of README file
from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup
from setuptools.command.install import install
from subprocess import check_call

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

DESCRIPTION = "EvaDB AI-Relational Database System"
NAME = "evadb"
AUTHOR = "Georgia Tech Database Group"
AUTHOR_EMAIL = "arulraj@gatech.edu"
URL = "https://github.com/georgia-tech-db/eva"

# Check Python version
# import sys
# if sys.version_info < (3, 8):
#     sys.exit("Python 3.8 or later is required.")


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


# version.py defines the VERSION and VERSION_SHORT variables
VERSION_DICT: Dict[str, str] = {}
with open("evadb/version.py", "r") as version_file:
    exec(version_file.read(), VERSION_DICT)

DOWNLOAD_URL = "https://github.com/georgia-tech-db/eva"
LICENSE = "Apache License 2.0"
VERSION = VERSION_DICT["VERSION"]

minimal_requirements = [
    "numpy>=1.19.5",
    "pandas>=1.1.5",
    "sqlalchemy>=2.0.0",
    "sqlalchemy-utils>=0.36.6",
    "lark>=1.0.0",
    "pyyaml>=5.1",
    "aenum>=2.2.0",
    "diskcache>=5.4.0",
    "retry>=0.9.2",
    "pydantic<2",  # ray-project/ray#37019.
    "psutil",
    "thefuzz",
]

vision_libs = [
    "torch>=1.10.0",
    "torchvision>=0.11.1",
    "transformers",  # HUGGINGFACE
    "faiss-cpu",  # DEFAULT VECTOR INDEX
    "opencv-python-headless>=4.6.0.66",
    "Pillow>=8.4.0",
    "eva-decord>=0.6.1",  # VIDEO PROCESSING
    "ultralytics>=8.0.93",  # OBJECT DETECTION
    "timm>=0.6.13",  # HUGGINGFACE VISION TASKS
    "sentencepiece",  # TRANSFORMERS
]

document_libs = [
    "transformers",  # HUGGINGFACE
    "langchain",  # DATA LOADERS
    "faiss-cpu",  # DEFAULT VECTOR INDEX
    "pymupdf<1.23.0",  # pymupdf/PyMuPDF#2617 and pymupdf/PyMuPDF#2614
    "pdfminer.six",
    "sentence-transformers",
    "protobuf",
    "bs4",
    "openai>=1.0",  # CHATGPT
    "gpt4all",  # PRIVATE GPT
    "sentencepiece",  # TRANSFORMERS
]

function_libs = [
    "facenet-pytorch>=2.5.2",  # FACE DETECTION
    "pytube",  # YOUTUBE QA APP
    "youtube-transcript-api",  # YOUTUBE QA APP
    "boto3",  # AWS
    "norfair>=2.2.0",  # OBJECT TRACKING
    "kornia",  # SIFT FEATURES
]

ray_libs = [
    "ray>=1.13.0,<2.5.0",  # BREAKING CHANGES IN 2.5.0
]

notebook_libs = [
    "ipython<8.13.0",
    "ipywidgets>=7.7.2",
    "matplotlib>=3.3.4",
    "nbmake>=1.2.1",
    "nest-asyncio>=1.5.6",
]

qdrant_libs = ["qdrant_client"]  # cannot install on 3.11 due to grcpio
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]

milvus_libs = ["pymilvus>=2.3.0"]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

pinecone_libs = ["pinecone-client"]

chromadb_libs = ["chromadb"]

postgres_libs = [
    "psycopg2",
]

ludwig_libs = ["ludwig[hyperopt,distributed]"]  # MODEL TRAIN AND FINE TUNING
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main

sklearn_libs = ["scikit-learn"]

xgboost_libs = ["flaml[automl]"]

forecasting_libs = [
<<<<<<< HEAD
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
<<<<<<< HEAD
=======
<<<<<<< HEAD
    "statsforecast",  # MODEL TRAIN AND FINE TUNING
    "neuralforecast",  # MODEL TRAIN AND FINE TUNING
>>>>>>> georgia-tech-db-main
]

imagegen_libs = [
    "replicate"
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main

sklearn_libs = ["scikit-learn"]

forecasting_libs = [
<<<<<<< HEAD
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
<<<<<<< HEAD
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
>>>>>>> georgia-tech-db-main
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

sklearn_libs = ["scikit-learn"]

xgboost_libs = ["flaml[automl]"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
<<<<<<< HEAD
]

imagegen_libs = [
    "replicate"
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

sklearn_libs = ["scikit-learn"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD
sklearn_libs = ["scikit-learn"]

xgboost_libs = ["flaml[automl]"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
]
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))

sklearn_libs = ["scikit-learn"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
=======
sklearn_libs = ["scikit-learn"]

>>>>>>> ae08f806 (Bump v0.3.4+ dev)
forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
]
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

imagegen_libs = [
    "replicate"
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

sklearn_libs = ["scikit-learn"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
]
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

sklearn_libs = ["scikit-learn"]

forecasting_libs = [
    "statsforecast", # MODEL TRAIN AND FINE TUNING
    "neuralforecast" # MODEL TRAIN AND FINE TUNING
]

### NEEDED FOR DEVELOPER TESTING ONLY

dev_libs = [
    # TESTING PACKAGES
    "pytest>=6.1.2",
    "pytest-cov>=2.11.1",
    "mock",
    "coveralls>=3.0.1",
    "moto[s3]>=4.1.1",
    "pytest-testmon",
    # BENCHMARK PACKAGES
    "pytest-benchmark",
    # LINTING PACKAGES
    "codespell",
    "pylint",
    "black>=23.1.0",
    "isort>=5.10.1",
    "flake8>=3.9.1",
    # DISTRIBUTION PACKAGES
    "wheel>=0.37.1",
    "semantic_version",
    "PyGithub",
    "twine",
    "PyDriller",
]

INSTALL_REQUIRES = minimal_requirements

EXTRA_REQUIRES = {
    "ray": ray_libs,
    "vision": vision_libs,
    "document": document_libs,
    "function": function_libs,
    "notebook": notebook_libs,
    "qdrant": qdrant_libs,
    "pinecone": pinecone_libs,
    "chromadb": chromadb_libs,
<<<<<<< HEAD
    "milvus": milvus_libs,
    "postgres": postgres_libs,
    "ludwig": ludwig_libs,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
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
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    "sklearn": sklearn_libs,
    "xgboost": xgboost_libs,
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs,
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
>>>>>>> georgia-tech-db-main
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs + xgboost_libs
=======
=======
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs + xgboost_libs
=======
<<<<<<< HEAD
>>>>>>> 8a8a90aa (Add stable diffusion integration (#1240))
>>>>>>> georgia-tech-db-main
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs,
<<<<<<< HEAD
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 8a8a90aa (Add stable diffusion integration (#1240))
>>>>>>> georgia-tech-db-main
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
    "postgres": postgres_libs,
    "ludwig": ludwig_libs,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    "sklearn": sklearn_libs,
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
    "sklearn": sklearn_libs,
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    "sklearn": sklearn_libs,
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs,
>>>>>>> bf022329 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
>>>>>>> eva-source
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs + xgboost_libs
<<<<<<< HEAD
>>>>>>> 201f901b (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
=======
>>>>>>> eva-source
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs + xgboost_libs
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 201f901b (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> eva-master
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs,
>>>>>>> bf022329 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
>>>>>>> 8a8a90aa (Add stable diffusion integration (#1240))
=======
=======
=======
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs + sklearn_libs + imagegen_libs + xgboost_libs
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> 201f901b (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
=======
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
    "forecasting": forecasting_libs,
    # everything except ray, qdrant, ludwig and postgres. The first three fail on pyhton 3.11.
    "dev": dev_libs + vision_libs + document_libs + function_libs + notebook_libs + forecasting_libs,
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
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
}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        # "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    # https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point
    entry_points={
        "console_scripts": [
            "evadb_server=evadb.evadb_server:main",
            "evadb_client=evadb.evadb_cmd_client:main",
        ]
    },
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRES,
    include_package_data=True,
    package_data={
        "evadb": [
            "evadb.yml",
            "parser/evadb.lark",
            "third_party/databases/**/requirements.txt",
        ]
    },
)
