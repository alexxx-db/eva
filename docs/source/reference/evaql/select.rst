.. _sql-select:

SELECT
======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
.. _select:

SELECT TUPLES WITH PREDICATES
=======
SELECT FRAMES WITH PREDICATES
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. _select:

SELECT TUPLES WITH PREDICATES
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
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
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
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
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
>>>>>>> c2094b0c (docs: updated sql statement list)
<<<<<<< HEAD
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
=======
=======
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
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

Compose multiple user-defined functions in a single query to construct semantically complex queries.

.. code:: sql

   SELECT id, bbox, EmotionDetector(Crop(data, bbox)) 
   FROM HAPPY JOIN LATERAL UNNEST(FaceDetector(data)) AS Face(bbox, conf)  
   WHERE id < 15;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
SELECT TUPLES WITHOUT TABLE
---------------------------
=======
SELECT WITHOUT TABLE
--------------------
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
SELECT TUPLES WITHOUT TABLE
---------------------------
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

In EvaDB, we can compose a query that does not have a table source. This type of queries are usually expressions.

.. code:: sql

   SELECT 1;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
   SELECT 1 > 2;
=======
   SELECT 1>2;
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
   SELECT 1 > 2;
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
   SELECT HomeRentalForecast(12);

.. note::

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.
=======
   Go over :ref:`forecast` for forecasting function support in EvaDB.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.
>>>>>>> 7e60bf69 (docs: updated sql statement list)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

