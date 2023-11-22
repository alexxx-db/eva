.. _sql-select:

SELECT
======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
.. _select:

SELECT TUPLES WITH PREDICATES
=======
SELECT FRAMES WITH PREDICATES
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
.. _select:

SELECT TUPLES WITH PREDICATES
>>>>>>> 7e60bf69 (docs: updated sql statement list)
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
-----------------------------

Search for frames with a car

.. code:: sql

   SELECT id, frame 
   FROM MyVideo 
   WHERE ['car'] <@ FastRCNNObjectDetector(frame).labels
   ORDER BY id;

Search frames with a pedestrian and a car

.. code:: sql

   SELECT id, frame 
   FROM MyVideo 
   WHERE ['pedestrian', 'car'] <@ FastRCNNObjectDetector(frame).labels;

Search for frames containing greater than 3 cars

.. code:: sql

   SELECT id FROM MyVideo
   WHERE ArrayCount(FastRCNNObjectDetector(data).label, 'car') > 3
   ORDER BY id;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
<<<<<<< HEAD
<<<<<<< HEAD
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
>>>>>>> 7e60bf69 (docs: updated sql statement list)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
>>>>>>> eva-source
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
>>>>>>> 7e60bf69 (docs: updated sql statement list)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
>>>>>>> c2094b0c (docs: updated sql statement list)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 7e60bf69 (docs: updated sql statement list)
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

Compose multiple user-defined functions in a single query to construct semantically complex queries.

.. code:: sql

   SELECT id, bbox, EmotionDetector(Crop(data, bbox)) 
   FROM HAPPY JOIN LATERAL UNNEST(FaceDetector(data)) AS Face(bbox, conf)  
   WHERE id < 15;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
SELECT TUPLES WITHOUT TABLE
---------------------------
=======
SELECT WITHOUT TABLE
--------------------
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
SELECT TUPLES WITHOUT TABLE
---------------------------
>>>>>>> 7e60bf69 (docs: updated sql statement list)
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

In EvaDB, we can compose a query that does not have a table source. This type of queries are usually expressions.

.. code:: sql

   SELECT 1;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   SELECT 1 > 2;
=======
   SELECT 1>2;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
   SELECT 1 > 2;
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
   SELECT 1 > 2;
>>>>>>> 7e60bf69 (docs: updated sql statement list)
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   SELECT HomeRentalForecast(12);

.. note::

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.
=======
   Go over :ref:`forecast` for forecasting function support in EvaDB.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.
>>>>>>> 7e60bf69 (docs: updated sql statement list)
>>>>>>> 5651b7e2 (docs: updated sql statement list)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

