.. _installation options:

Installation Options
====================

<<<<<<< HEAD
EvaDB supports a wide range of installation options for extending its functionality.

Computer Vision
---------------

This installation option enables use-cases related to vision including image classification, object detection, and emotion analysis.

.. code-block:: python

    pip install evadb[vision]

Natural Language Processing
---------------------------

This installation option enables use-cases related to natural language processing including text summarization, question answering, and sentiment analysis.

.. code-block:: python

    pip install evadb[document]

Vector Database Systems
-----------------------

This installation option enables use-cases related to similarity search based on feature vectors by connecting to vector database systems.

.. code-block:: python

    pip install evadb[qdrant]

AI Engines
----------

This installation option enables use-cases related to training and fine-tuning AI models using AI engines.

.. code-block:: python

    pip install evadb[ludwig]

Forecasting
-----------

This installation option enables use-cases related to time-series forecasting.

.. code-block:: python

    pip install evadb[forecasting]

Ray
----

This installation option enables more efficient query execution on CPUs and GPUs using the Ray compute engine.

.. code-block:: python

    pip install evadb[ray]
=======
EvaDB provides the following additional installation options for extending its functionality.

* ``pip install evadb[vision]`` for installing computer vision packages. They enable use-cases including image classification, object detection, and emotion analysis.

* ``pip install evadb[document]`` for installing natural language processing packages. They enable use-cases including text summarization, question answering, and sentiment analysis.

* ``pip install evadb[qdrant]`` for installing the Qdrant vector database system. It enables use-cases related to similarity search based on feature vectors.

<<<<<<< HEAD
<<<<<<< HEAD
* ``pip install evadb[ludwig]`` for installing the Ludwig model training framework. It enables use-cases related to training and fine-tuning AI models.

* ``pip install evadb[forecasting]`` for installing the statsforecast forecasting framework. It enables use-cases related to time series forecasting.
<<<<<<< HEAD
=======
* ``pip install evadb[ludwig]`` for installing the Ludwig model training framework. It enables use-cases related to training and fine-tunining AI models.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
* ``pip install evadb[ludwig]`` for installing the Ludwig model training framework. It enables use-cases related to training and fine-tuning AI models.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

* ``pip install evadb[ray]`` for installing the Ray compute engine. It enables EvaDB to do more efficient query execution on CPUs and GPUs.

>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
