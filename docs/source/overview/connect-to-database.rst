<<<<<<< HEAD
Connect to Database
============================

EvaDB supports an extensive range of data sources for structured and unstructured data.

Connect to a SQL Database System
--------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
=======
<<<<<<< HEAD
Connect to Data Sources
=======================

EvaDB supports a wide range of data sources including SQL database systems, object stores, and vector database systems.

Connect to an Existing SQL Database System
------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
>>>>>>> d8799826 (docs: updates)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
>>>>>>> 5f27824c (docs: updates)
>>>>>>> georgia-tech-db-main

.. code-block::

   CREATE DATABASE restaurant_reviews 
   WITH ENGINE = 'postgres', 
   PARAMETERS = {
       "user": "eva",
       "password": "password",
       "host": "localhost",
       "port": "5432",
       "database": "restaurant_reviews"
   };
=======
1. Use the `CREATE DATABASE` statement to connect to an existing SQL database.
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
1. Use the `CREATE DATABASE` statement to connect to an existing SQL database.
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
Connect to Database
============================

EvaDB supports an extensive range of data sources for structured and unstructured data.

Connect to a SQL Database System
--------------------------------

1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.

.. code-block::

<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   cursor.query("""
        CREATE DATABASE restaurant_reviews 
        WITH ENGINE = 'postgres', 
        PARAMETERS = {
            "user": "eva",
            "password": "password",
            "host": "localhost",
            "port": "5432",
            "database": "restaurant_reviews"
     	   };""").df()
<<<<<<< HEAD
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   CREATE DATABASE restaurant_reviews 
   WITH ENGINE = 'postgres', 
   PARAMETERS = {
       "user": "eva",
       "password": "password",
       "host": "localhost",
       "port": "5432",
       "database": "restaurant_reviews"
   };
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

.. note::

   Go over the :ref:`CREATE DATABASE<create-database>` statement for more details. The :ref:`Databases<databases>` page lists all the database systems that EvaDB currently supports.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
>>>>>>> d8799826 (docs: updates)
2. Preview the Available Data Using ``SELECT``
=======
2. Preview the data using ``SELECT``
>>>>>>> 5f27824c (docs: updates)

You can now preview the data stored in the ``food_review`` table in the ``restaurant_reviews`` database with a :ref:`SELECT<select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run native queries inside the connected database with ``USE``

You can also run native queries directly inside the connected database system with the :ref:`USE<use>` statement.

.. code-block::

   USE restaurant_reviews {
       INSERT INTO food_review (name, review) 
       VALUES (
           'Customer 1', 
           'I ordered fried rice but it is too salty.'
       )
   };
=======
2. Preview the Available Data Using `SELECT`
<<<<<<< HEAD
<<<<<<< HEAD
=======
2. Preview the Available Data Using ``SELECT``
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block::

<<<<<<< HEAD
=======
2. Preview the Available Data Using `SELECT`
=======
2. Preview the Available Data Using ``SELECT``
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block::

<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
=======
2. Preview the Available Data Using ``SELECT``
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block::

<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

.. note::

   Go over the :ref:`CREATE DATABASE<sql-create-database>` statement for more details. The :ref:`Databases<databases>` page lists all the database systems that EvaDB currently supports.

<<<<<<< HEAD
<<<<<<< HEAD
2. Preview the Available Data Using ``SELECT``

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block::

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
   cursor.query(
      """
        USE restaurant_reviews {
                INSERT INTO food_review (name, review) 
                VALUES (
                  'Customer 1', 
                  'I ordered fried rice but it is too salty.'
                )
        };
      """).df()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   USE restaurant_reviews {
       INSERT INTO food_review (name, review) 
       VALUES (
           'Customer 1', 
           'I ordered fried rice but it is too salty.'
       )
   };
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

Connect to Object Store
------------------------

<<<<<<< HEAD
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
2. Preview the Available Data Using `SELECT`
=======
2. Preview the Available Data Using ``SELECT``
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block::

<<<<<<< HEAD
   cursor.query(
      """
        USE restaurant_reviews {
                INSERT INTO food_review (name, review) 
                VALUES (
                  'Customer 1', 
                  'I ordered fried rice but it is too salty.'
                )
        };
      """).df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
   USE restaurant_reviews {
       INSERT INTO food_review (name, review) 
       VALUES (
           'Customer 1', 
           'I ordered fried rice but it is too salty.'
       )
   };
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD


=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)


>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
Load Unstructured Data
-----------------------

EvaDB supports diverse types of unstructured data. Here are some examples:

1. Load Images from Local Filesystem

You can load a collection of images obtained from Reddit from the local filesystem into EvaDB using the :ref:`LOAD<sql-load>` statement.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
.. code-block:: python
   
   cursor.query("""
      LOAD IMAGE 'reddit-images/*.jpg' 
      INTO reddit_dataset;
   """).df()
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

2. Load Video from Cloud Bucket

You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<sql-load>` statement.
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
EvaDB supports diverse types of `unstructured data` (e.g., PDFs, videos). You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<load-video>` statement.
>>>>>>> c2094b0c (docs: updated sql statement list)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======

>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
.. code-block:: python

   cursor.query("""
      LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' 
      INTO MNISTVid;
   """).df()
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

.. note::

   Go over the :ref:`LOAD VIDEO<load-video>` statement for more details on the types of unstructured data that EvaDB supports.

Connect to Local Filesystem
---------------------------

You can load a collection of images obtained from Reddit from the local filesystem into EvaDB using the :ref:`LOAD IMAGE<load-image>` statement.

.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;


Connect to Vector Database System
---------------------------------

Vector database systems are useful for querying unstructured data. A vector index contains the vectors (embeddings) generated by processing the unstructured data using a feature extractor function.

You can use the ``CREATE INDEX`` statement to connect to an existing vector database system.

.. code-block:: text

   CREATE INDEX index_name ON table_name (data) USING FAISS;

.. note::

   Go over the :ref:`CREATE INDEX<create-index>` statement for more details. The :ref:`Vector Databases<databases>` page lists all the vector database systems that EvaDB currently supports.

.. include:: ../shared/designs/design3.rst
=======
=======
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

.. note::

   Go over the :ref:`LOAD statement<sql-load>` statement for more details on the types of unstructured data that EvaDB supports.
   
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
