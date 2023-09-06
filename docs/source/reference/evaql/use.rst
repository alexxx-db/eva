<<<<<<< HEAD
USE
===

.. _use:

The USE statement allows us to run arbitrary native queries in the connected database.
=======
.. _sql-use:

USE
===

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
The USE statement allows us to run arbitary native queries in the connected database.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
The USE statement allows us to run arbitrary native queries in the connected database.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
The USE statement allows us to run arbitrary native queries in the connected database.
=======
The USE statement allows us to run arbitary native queries in the connected database.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
The USE statement allows us to run arbitrary native queries in the connected database.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))

.. code:: text

   USE [database_connection] { [native_query] };

* [database_connection] is an external database connection instanced by the `CREATE DATABASE statement`.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
* [native_query] is an arbitrary SQL query supported by the [database_connection]. 
=======
* [native_query] is an arbitary SQL query supprted by the [database_connection]. 
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
* [native_query] is an arbitrary SQL query supported by the [database_connection]. 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
* [native_query] is an arbitrary SQL query supported by the [database_connection]. 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))

.. warning::

   Currently EvaDB only supports single query in one USE statement. The [native_query] should not end with semicolon.

Examples
--------

.. code:: text

   USE postgres_data {
     DROP TABLE IF EXISTS food_review
   };
        
   USE postgres_data {
     CREATE TABLE food_review (name VARCHAR(10), review VARCHAR(1000))
   };

   USE postgres_data {
     INSERT INTO food_review (name, review) VALUES ('Customer 1', 'I ordered fried rice but it is too salty.')
   };


