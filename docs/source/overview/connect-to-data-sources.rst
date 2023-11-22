Connect to Data Sources
=======================

EvaDB supports a wide range of data sources including SQL database systems, object stores, and vector database systems.

Connect to an Existing SQL Database System
------------------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
=======
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database server. For example, here is the SQL command to connect EvaDB with a locally running :ref:`PostgreSQL<postgresql>` database server running on port ``5432``.
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> eva-source
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
=======
1. Use the :ref:`CREATE DATABASE<create-database>` statement to connect to an **existing** SQL database.
>>>>>>> 32e513d7 (docs: updates)
>>>>>>> 5f27824c (docs: updates)
>>>>>>> 35b99c88 (docs: updates)
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD

For quick prototyping, you can use an embedded :ref:`SQLite<sqlite>` database. Here, the SQLite database file is called ``evadb.db``.

.. code-block::

   CREATE DATABASE restaurant_reviews 
   WITH ENGINE = 'sqlite', 
   PARAMETERS = {
       "database": "evadb.db"
   };
=======
>>>>>>> 32e513d7 (docs: updates)
>>>>>>> georgia-tech-db-main
=======
=======
1. Use the `CREATE DATABASE` statement to connect to an existing SQL database.
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
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
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
   CREATE DATABASE restaurant_reviews 
   WITH ENGINE = 'postgres', 
   PARAMETERS = {
       "user": "eva",
       "password": "password",
       "host": "localhost",
       "port": "5432",
       "database": "restaurant_reviews"
   };
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> eva-source
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> georgia-tech-db-main

.. note::

   Go over the :ref:`CREATE DATABASE<create-database>` statement for more details. The :ref:`Databases<databases>` page lists all the database systems that EvaDB currently supports.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
=======

=======
>>>>>>> 32e513d7 (docs: updates)
>>>>>>> georgia-tech-db-main
2. Preview the data using ``SELECT``
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
2. Preview the Available Data Using ``SELECT``
=======
2. Preview the data using ``SELECT``
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> eva-source
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> georgia-tech-db-main

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
<<<<<<< HEAD
=======
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
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> eva-source
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> georgia-tech-db-main

Connect to Object Store
------------------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> georgia-tech-db-main
EvaDB supports diverse types of `unstructured data` (e.g., PDFs, videos). You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<load-video>` statement.

.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
Load Unstructured Data
-----------------------

EvaDB supports diverse types of unstructured data. Here are some examples:

1. Load Images from Local Filesystem

You can load a collection of images obtained from Reddit from the local filesystem into EvaDB using the :ref:`LOAD<sql-load>` statement.

<<<<<<< HEAD
<<<<<<< HEAD
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
<<<<<<< HEAD
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
=======
=======
>>>>>>> georgia-tech-db-main
.. code-block:: python
   
   cursor.query("""
      LOAD IMAGE 'reddit-images/*.jpg' 
      INTO reddit_dataset;
   """).df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main

2. Load Video from Cloud Bucket

You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<sql-load>` statement.
=======
EvaDB supports diverse types of `unstructured data` (e.g., PDFs, videos). You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<load-video>` statement.
>>>>>>> c2094b0c (docs: updated sql statement list)

<<<<<<< HEAD
<<<<<<< HEAD
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
<<<<<<< HEAD
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
=======
=======
>>>>>>> georgia-tech-db-main
.. code-block:: python

   cursor.query("""
      LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' 
      INTO MNISTVid;
   """).df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> eva-source
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> georgia-tech-db-main

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

<<<<<<< HEAD
   Go over the :ref:`CREATE INDEX<create-index>` statement for more details. The :ref:`Vector Databases<vector_databases>` page lists all the vector database systems that EvaDB currently supports.
=======
   Go over the :ref:`CREATE INDEX<create-index>` statement for more details. The :ref:`Vector Databases<databases>` page lists all the vector database systems that EvaDB currently supports.
>>>>>>> 35b99c88 (docs: updates)

.. include:: ../shared/designs/design3.rst