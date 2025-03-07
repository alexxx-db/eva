CREATE 
======

.. _sql-create-database:

CREATE DATABASE
---------------

The CREATE DATABASE statement allows us to connect to an external structured data store in EvaDB.

.. code:: text

   CREATE DATABASE [database_connection]
        WITH ENGINE = [database_engine],
        PARAMETERS = [key_value_parameters];

* [database_connection] is the name of the database connection. `[database_connection].[table_name]` will be used as table name to compose SQL queries in EvaDB.
* [database_engine] is the supported database engine. Check :ref:`supported data sources<databases>` for all engine and their available configuration parameters.
* [key_value_parameters] is a list of key-value pairs as arguments to establish a connection.


Examples
~~~~~~~~

.. code:: text

   CREATE DATABASE postgres_data WITH ENGINE = 'postgres', PARAMETERS = {
        "user": "eva", 
        "password": "password",
        "host": "localhost",
        "port": "5432", 
        "database": "evadb"
   };

CREATE TABLE
------------

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
To create a table, we can specify the schema of the table.

.. code-block::

   CREATE TABLE [IF NOT EXISTS] table_name ( [
     column_name data_type
     [, ... ]
   ] );

Blew is an example:
<<<<<<< HEAD
=======
To create a table, specify the schema of the table.
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
To create a table, specify the schema of the table.
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
To create a table, specify the schema of the table.
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
=======
To create a table, specify the schema of the table.
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

.. code:: mysql

   CREATE TABLE IF NOT EXISTS MyCSV (
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
     id INTEGER UNIQUE,
     frame_id INTEGER,
     video_id INTEGER,
     dataset_name TEXT,
     label TEXT,
     bbox NDARRAY FLOAT32(4),
     object_id INTEGER
   );

Below are all supported column types:

* INTEGER
* TEXT
* FLOAT
* NDARRAY 
* BOOLEAN

.. note::

   Check `NdArrayType <https://github.com/georgia-tech-db/evadb/blob/staging/evadb/catalog/catalog_type.py>`_ for available NDARRAY types.

We can also create table from the output of a ``SELECT`` query.

.. code-block::

   CREATE TABLE [IF NOT EXISTS] table_name 
   AS select_query

Below is an example:

.. code-block:: sql

    CREATE TABLE UADETRAC_FastRCNN AS
    SELECT id, FastRCNNObjectDetector(frame).labels 
    FROM UADETRAC
    WHERE id<5;


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
CREATE INDEX
------------
=======
<<<<<<< HEAD
=======
>>>>>>> eva-source
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
CREATE INDEX
------------
=======
CREATE UDF
----------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
CREATE INDEX
------------
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main

The CREATE INDEX statement allows us to construct an EvaDB based index to accelerate semantic based searching.
The index can be created on either a column of a table directly or outputs from a function running on a column of a table.

.. code:: sql
   
   CREATE INDEX [index_name]
      ON [table_name] ([column_name])
      USING [index_method]

   CREATE INDEX [index_name]
      ON [table_name] ([function_name]([column_name]))
      USING [index_method]

* [index_name] is the name the of constructed index.
* [table_name] is the name of the table, on which the index is created.
* [column_name] is the name of one of the column in the table. We currently only support creating index on single column of a table.
* [function_name] is an optional parameter that can be added if the index needs to be constructed on results of a function.
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main

Examples
~~~~~~~~

.. code:: sql

   CREATE INDEX reddit_index
   ON reddit_dataset (data)
   USING FAISS

   CREATE INDEX func_reddit_index
   ON reddit_dataset (SiftFeatureExtractor(data))
   USING QDRANT

You can check out :ref:`similarity search use case<image-search>` about how to use index automatically.

CREATE FUNCTION
---------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
CREATE FUNCTION
---------------

>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
To register an user-defined function, specify the implementation details of the function.

.. code-block:: sql

    CREATE FUNCTION IF NOT EXISTS FastRCNNObjectDetector
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
                   id INTEGER UNIQUE,
                   frame_id INTEGER,
                   video_id INTEGER,
                   dataset_name TEXT(30),
                   label TEXT(30),
                   bbox NDARRAY FLOAT32(4),
                   object_id INTEGER
    );
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
CREATE INDEX
------------
=======
CREATE UDF
----------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
CREATE INDEX
------------
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

The CREATE INDEX statement allows us to construct an EvaDB based index to accelerate semantic based searching.
The index can be created on either a column of a table directly or outputs from a function running on a column of a table.

.. code:: sql
   
   CREATE INDEX [index_name]
      ON [table_name] ([column_name])
      USING [index_method]

   CREATE INDEX [index_name]
      ON [table_name] ([function_name]([column_name]))
      USING [index_method]

* [index_name] is the name the of constructed index.
* [table_name] is the name of the table, on which the index is created.
* [column_name] is the name of one of the column in the table. We currently only support creating index on single column of a table.
* [function_name] is an optional parameter that can be added if the index needs to be construsted on results of a funciton.

Examples
~~~~~~~~

.. code:: sql

   CREATE INDEX reddit_index
   ON reddit_dataset (data)
   USING FAISS

   CREATE INDEX func_reddit_index
   ON reddit_dataset (SiftFeatureExtractor(data))
   USING QDRANT

You can check out :ref:`similarity search use case<image-search>` about how to use index automatically.

CREATE FUNCTION
---------------

=======
CREATE FUNCTION
---------------

>>>>>>> 2dacff69 (feat: sync master staging (#1050))
To register an user-defined function, specify the implementation details of the function.

.. code-block:: sql

<<<<<<< HEAD
    CREATE UDF IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
    CREATE FUNCTION IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
    INPUT  (frame NDARRAY UINT8(3, ANYDIM, ANYDIM))
    OUTPUT (labels NDARRAY STR(ANYDIM), bboxes NDARRAY FLOAT32(ANYDIM, 4),
            scores NDARRAY FLOAT32(ANYDIM))
    TYPE  Classification
<<<<<<< HEAD
<<<<<<< HEAD
    IMPL  'evadb/functions/fastrcnn_object_detector.py';
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
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
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
CREATE INDEX
------------
=======
CREATE UDF
----------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
CREATE INDEX
------------
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
CREATE INDEX
------------
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

The CREATE INDEX statement allows us to construct an EvaDB based index to accelerate semantic based searching.
The index can be created on either a column of a table directly or outputs from a function running on a column of a table.

.. code:: sql
   
   CREATE INDEX [index_name]
      ON [table_name] ([column_name])
      USING [index_method]

   CREATE INDEX [index_name]
      ON [table_name] ([function_name]([column_name]))
      USING [index_method]

* [index_name] is the name the of constructed index.
* [table_name] is the name of the table, on which the index is created.
* [column_name] is the name of one of the column in the table. We currently only support creating index on single column of a table.
* [function_name] is an optional parameter that can be added if the index needs to be construsted on results of a funciton.
=======
>>>>>>> fb00f6de (ran spellchecker)

Examples
~~~~~~~~

.. code:: sql

   CREATE INDEX reddit_index
   ON reddit_dataset (data)
   USING FAISS

   CREATE INDEX func_reddit_index
   ON reddit_dataset (SiftFeatureExtractor(data))
   USING QDRANT

You can check out :ref:`similarity search use case<image-search>` about how to use index automatically.

CREATE FUNCTION
---------------

=======
CREATE FUNCTION
---------------

>>>>>>> 2dacff69 (feat: sync master staging (#1050))
To register an user-defined function, specify the implementation details of the function.
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
CREATE FUNCTION via Type
----------------------------
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
.. _create-udf-train:

CREATE UDF via Training
-----------------------

To register an user-defined function by training a predication model.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))

.. code-block:: sql

<<<<<<< HEAD
    CREATE UDF IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
    CREATE FUNCTION IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
CREATE UDF
----------
=======
CREATE FUNCTION
---------------
>>>>>>> b87af508 (feat: sync master staging (#1050))

To register an user-defined function, specify the implementation details of the function.

.. code-block:: sql

<<<<<<< HEAD
    CREATE UDF IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
    CREATE FUNCTION IF NOT EXISTS FastRCNNObjectDetector
>>>>>>> b87af508 (feat: sync master staging (#1050))
    INPUT  (frame NDARRAY UINT8(3, ANYDIM, ANYDIM))
    OUTPUT (labels NDARRAY STR(ANYDIM), bboxes NDARRAY FLOAT32(ANYDIM, 4),
            scores NDARRAY FLOAT32(ANYDIM))
    TYPE  Classification
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    IMPL  'evadb/functions/fastrcnn_object_detector.py';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
CREATE FUNCTION via Type
----------------------------
=======
.. _create-udf-train:

CREATE FUNCTION via Training
----------------------------

To register an user-defined function by training a predication model.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
=======
CREATE FUNCTION via Type
----------------------------
>>>>>>> fb00f6de (ran spellchecker)
>>>>>>> georgia-tech-db-main

.. code-block:: sql

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> eva-source
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fb00f6de (ran spellchecker)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 5b27053e (ran spellchecker)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> fb00f6de (ran spellchecker)
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
CREATE FUNCTION via Type
----------------------------
=======
.. _create-udf-train:

CREATE FUNCTION via Training
----------------------------

To register an user-defined function by training a predication model.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

.. code-block:: sql

<<<<<<< HEAD
=======
<<<<<<< HEAD
CREATE FUNCTION via Type
----------------------------

.. code-block:: sql

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
CREATE FUNCTION via Type
----------------------------
=======
.. _create-udf-train:

CREATE FUNCTION via Training
----------------------------

To register an user-defined function by training a predication model.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

.. code-block:: sql

<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> eva-master
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
   CREATE [OR REPALCE] FUNCTION [IF NOT EXISTS] function_name
=======
   CREATE [OR REPLACE] FUNCTION [IF NOT EXISTS] function_name
>>>>>>> 62080794 (ran spellchecker)
   [ FROM ( select ) ]
   TYPE function_type
   [ parameter [ ...] ]

Where the `parameter` is ``key value`` pair.

.. warning::

   For one ``CREATE FUNCTION`` query, we can specify ``OR REPLACE`` or ``IF NOT EXISTS`` or neither, but not both.

.. note::

   Go over :ref:`hf`, :ref:`ludwig`, and :ref:`forecast` to check examples for creating function via type.
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
   CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
   (SELECT * FROM HomeRentals)
   TYPE Ludwig
   PREDICT 'rental_price'
   TIME_LIST 120;
   TUNE_FOR_MEMORY False;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> eva-source

=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
    IMPL  'evadb/udfs/fastrcnn_object_detector.py';
=======
    IMPL  'evadb/functions/fastrcnn_object_detector.py';
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))

.. _create-udf-train:

CREATE FUNCTION via Training
=======
CREATE FUNCTION via Type
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
----------------------------

.. code-block:: sql

=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
CREATE FUNCTION via Type
----------------------------

.. code-block:: sql

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   CREATE [OR REPALCE] FUNCTION [IF NOT EXISTS] function_name
   [ FROM ( select ) ]
   TYPE function_type
   [ parameter [ ...] ]

Where the `parameter` is ``key value`` pair.

.. warning::

   For one ``CREATE FUNCTION`` query, we can specify ``OR REPLACE`` or ``IF NOT EXISTS`` or neither, but not both.

.. note::

   Go over :ref:`hf`, :ref:`ludwig`, and :ref:`forecast` to check examples for creating function via type.
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
   CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
   (SELECT * FROM HomeRentals)
   TYPE Ludwig
   PREDICT 'rental_price'
   TIME_LIST 120;
   TUNE_FOR_MEMORY False;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
    IMPL  'evadb/udfs/fastrcnn_object_detector.py';
=======
    IMPL  'evadb/functions/fastrcnn_object_detector.py';
>>>>>>> b87af508 (feat: sync master staging (#1050))

.. _create-udf-train:

CREATE FUNCTION via Training
=======
CREATE FUNCTION via Type
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
----------------------------

.. code-block:: sql

<<<<<<< HEAD
   CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
   (SELECT * FROM HomeRentals)
   TYPE Ludwig
<<<<<<< HEAD
   'predict' 'rental_price'
   'time_list' 120;
   'tune_for_memory' False;
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
   PREDICT 'rental_price'
   TIME_LIST 120;
   TUNE_FOR_MEMORY False;
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
   CREATE [OR REPALCE] FUNCTION [IF NOT EXISTS] function_name
   [ FROM ( select ) ]
   TYPE function_type
   [ parameter [ ...] ]

Where the `parameter` is ``key value`` pair.

.. warning::

   For one ``CREATE FUNCTION`` query, we can specify ``OR REPLACE`` or ``IF NOT EXISTS`` or neither, but not both.

.. note::

   Go over :ref:`hf`, :ref:`ludwig`, and :ref:`forecast` to check examples for creating function via type.
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
    IMPL  'evadb/udfs/fastrcnn_object_detector.py';
=======
    IMPL  'evadb/functions/fastrcnn_object_detector.py';
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))

.. _create-udf-train:

CREATE FUNCTION via Training
=======
CREATE FUNCTION via Type
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
----------------------------

.. code-block:: sql

<<<<<<< HEAD
   CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
   (SELECT * FROM HomeRentals)
   TYPE Ludwig
<<<<<<< HEAD
   'predict' 'rental_price'
   'time_list' 120;
   'tune_for_memory' False;
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
   PREDICT 'rental_price'
   TIME_LIST 120;
   TUNE_FOR_MEMORY False;
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
   CREATE [OR REPALCE] FUNCTION [IF NOT EXISTS] function_name
   [ FROM ( select ) ]
   TYPE function_type
   [ parameter [ ...] ]

Where the `parameter` is ``key value`` pair.

.. warning::

   For one ``CREATE FUNCTION`` query, we can specify ``OR REPLACE`` or ``IF NOT EXISTS`` or neither, but not both.

.. note::

   Go over :ref:`hf`, :ref:`ludwig`, and :ref:`forecast` to check examples for creating function via type.
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

CREATE MATERIALIZED VIEW
------------------------

To create a view with materialized results -- like the outputs of deep learning model, use the following template:

.. code-block:: sql

    CREATE MATERIALIZED VIEW UADETRAC_FastRCNN (id, labels) AS
    SELECT id, FastRCNNObjectDetector(frame).labels 
    FROM UADETRAC
    WHERE id<5;
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
