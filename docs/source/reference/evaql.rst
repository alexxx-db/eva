<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. _evaql:

=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
EvaDB Query Language (EvaQL)
============================
=======
EvaDB Query Language Reference
===============================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
EvaDB Query Language (EvaQL)
============================
=======
EvaDB Query Language Reference
===============================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

>>>>>>> e867f37e (docs: updated images)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
EvaDB Query Language (EvaQL) is tailored for AI apps and is derived from SQL. 

AI models are simply function calls in a EvaQL query. 

This page lists all the EvaDB statements that you can leverage in your AI applications and notebooks. Get started by copying these SQL queries into a `.py` file or a Jupyter notebook.
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
EvaDB Query Language (EvaQL) Reference
======================================

EvaDB Query Language (EvaQL) is tailored for AI apps and is derived from SQL. Deep learning models are simply function calls in a SQL query. This page lists all the EvaDB statements that you can leverage in your applications/notebooks.
>>>>>>> ae8238d8 (docs: update references to UDFs)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

.. tableofcontents::

<<<<<<< HEAD
.. include:: ../shared/designs/design5.rst
=======
<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/designs/design5.rst
=======
.. include:: ../shared/design5.rst
>>>>>>> df4d8a35 (docs: updates)
=======
=======
.. include:: ../shared/design5.rst
>>>>>>> df4d8a35 (docs: updates)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
EvaDB Query Language (EvaQL)
============================
=======
EvaDB Query Language Reference
===============================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
EvaDB Query Language (EvaQL)
============================
=======
EvaDB Query Language Reference
===============================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

>>>>>>> e867f37e (docs: updated images)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
EvaDB Query Language (EvaQL) is tailored for AI apps and is derived from SQL. 

AI models are simply function calls in a EvaQL query. 

This page lists all the EvaDB statements that you can leverage in your AI applications and notebooks. Get started by copying these SQL queries into a `.py` file or a Jupyter notebook.
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
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

<<<<<<< HEAD
.. include:: ../shared/designs/design5.rst
>>>>>>> e867f37e (docs: updated images)
=======
<<<<<<< HEAD
.. include:: ../shared/designs/design5.rst
=======
.. include:: ../shared/design5.rst
>>>>>>> df4d8a35 (docs: updates)
<<<<<<< HEAD
>>>>>>> f1e2bddc (docs: updates)
=======
=======
>>>>>>> georgia-tech-db-main

.. tableofcontents::

.. include:: ../shared/designs/design5.rst
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 5678c9a3 (docs: updated images)
>>>>>>> georgia-tech-db-main
