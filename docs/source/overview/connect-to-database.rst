Connect to Database
============================

EvaDB supports an extensive range of data sources for structured and unstructured data.

Connect to a SQL Database System
--------------------------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.

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
=======
1. Use the ``CREATE DATABASE`` statement to connect to an existing SQL database.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

.. code-block::

<<<<<<< HEAD
=======
1. Use the `CREATE DATABASE` statement to connect to an existing SQL database.

.. code-block:: python

>>>>>>> a9124e1e (release: merge staging into master (#1032))
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
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))

.. note::

   Go over the :ref:`CREATE DATABASE<sql-create-database>` statement for more details. The :ref:`Databases<databases>` page lists all the database systems that EvaDB currently supports.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
2. Preview the Available Data Using ``SELECT``

You can now preview the available data in the ``restaurant_reviews`` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: sql

   SELECT * FROM restaurant_reviews.food_review;

3. Run Native Queries in the Connected Database With ``USE``

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

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

You can now preview the available data in the `restaurant_reviews` database with a standard :ref:`SELECT<sql-select>` statement.

.. code-block:: python

   cursor.query("""
      SELECT * 
      FROM restaurant_reviews.food_review;
      """).df()

3. Run Native Queries in the Connected Database With `USE`

You can also run native queries directly in the connected database system by the :ref:`USE<sql-use>` statement.

.. code-block:: python

>>>>>>> a9124e1e (release: merge staging into master (#1032))
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
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))


Load Unstructured Data
-----------------------

EvaDB supports diverse types of unstructured data. Here are some examples:

1. Load Images from Local Filesystem

You can load a collection of images obtained from Reddit from the local filesystem into EvaDB using the :ref:`LOAD<sql-load>` statement.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
.. code-block:: python
   
   cursor.query("""
      LOAD IMAGE 'reddit-images/*.jpg' 
      INTO reddit_dataset;
   """).df()
<<<<<<< HEAD
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD IMAGE 'reddit-images/*.jpg' INTO reddit_dataset;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))

2. Load Video from Cloud Bucket

You can load a video from an S3 cloud bucket into EvaDB using the :ref:`LOAD<sql-load>` statement.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
.. code-block:: python

   cursor.query("""
      LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' 
      INTO MNISTVid;
   """).df()
<<<<<<< HEAD
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. code-block:: sql

   LOAD VIDEO 's3://bucket/eva_videos/mnist.mp4' INTO MNISTVid;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))

.. note::

   Go over the :ref:`LOAD statement<sql-load>` statement for more details on the types of unstructured data that EvaDB supports.
   
