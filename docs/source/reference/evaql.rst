<<<<<<< HEAD
.. _evaql:

EvaDB Query Language (EvaQL)
============================
=======
EvaDB Query Language Reference
===============================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

<<<<<<< HEAD
EvaDB Query Language (EvaQL) is tailored for AI apps and is derived from SQL. 

AI models are simply function calls in a EvaQL query. 

This page lists all the EvaDB statements that you can leverage in your AI applications and notebooks. Get started by copying these SQL queries into a `.py` file or a Jupyter notebook.
=======
EvaDB Query Language (EvaDB) is derived from SQL. It is tailored for AI-driven analytics. EvaDB allows users to invoke deep learning models in the form
of functions.

Here is an example where we first define a function wrapping around the FastRCNN object detection model. We then issue a query with this function to detect objects.

.. code:: sql

    --- Create an user-defined function wrapping around FastRCNN ObjectDetector
    CREATE FUNCTION IF NOT EXISTS FastRCNNObjectDetector
    INPUT  (frame NDARRAY UINT8(3, ANYDIM, ANYDIM))
    OUTPUT (labels NDARRAY STR(ANYDIM), bboxes NDARRAY FLOAT32(ANYDIM, 4),
            scores NDARRAY FLOAT32(ANYDIM))
    TYPE  Classification
    IMPL  'evadb/functions/fastrcnn_object_detector.py';

    --- Use the function to retrieve frames that contain more than 3 cars
    SELECT id FROM MyVideo
    WHERE ArrayCount(FastRCNNObjectDetector(data).label, 'car') > 3
    ORDER BY id;

This page presents a list of all the EvaDB statements that you can leverage in your Jupyter Notebooks.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

.. tableofcontents::

.. include:: ../shared/designs/design5.rst