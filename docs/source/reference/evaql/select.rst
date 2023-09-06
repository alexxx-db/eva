.. _sql-select:

SELECT
======

<<<<<<< HEAD
.. _select:

SELECT TUPLES WITH PREDICATES
=======
SELECT FRAMES WITH PREDICATES
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
SELECT TUPLES WITH MULTIPLE PREDICATES
--------------------------------------
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

Compose multiple user-defined functions in a single query to construct semantically complex queries.

.. code:: sql

   SELECT id, bbox, EmotionDetector(Crop(data, bbox)) 
   FROM HAPPY JOIN LATERAL UNNEST(FaceDetector(data)) AS Face(bbox, conf)  
   WHERE id < 15;

SELECT TUPLES WITHOUT TABLE
---------------------------

In EvaDB, we can compose a query that does not have a table source. This type of queries are usually expressions.

.. code:: sql

   SELECT 1;
   SELECT 1 > 2;
   SELECT HomeRentalForecast(12);

.. note::

   If you are interested in forecasting with EvaDB, go over the :ref:`forecast` page.

