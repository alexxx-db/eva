:orphan:
<<<<<<< HEAD
<<<<<<< HEAD

Functions
=========

SHOW FUNCTIONS
--------------
=======

Functions
=========

<<<<<<< HEAD
SHOW UDFS
---------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
SHOW FUNCTIONS
--------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======

UDF
===

SHOW UDFS
---------
>>>>>>> a9124e1e (release: merge staging into master (#1032))

Here is a list of built-in user-defined functions in EvaDB.

.. code:: mysql

<<<<<<< HEAD
    SHOW FUNCTIONS;

    id   name                    impl
    0    FastRCNNObjectDetector  evadb/functions/fastrcnn_object_detector.p
    1    MVITActionRecognition   evadb/functions/mvit_action_recognition.py
    2    ArrayCount              evadb/functions/ndarray/array_count.py
    3    Crop                    evadb/evadb/functions/ndarray/crop.py
=======
    SHOW UDFS;

    id   name                    impl
    0    FastRCNNObjectDetector  evadb/udfs/fastrcnn_object_detector.p
    1    MVITActionRecognition   evadb/udfs/mvit_action_recognition.py
    2    ArrayCount              evadb/udfs/ndarray/array_count.py
    3    Crop                    evadb/evadb/udfs/ndarray/crop.py
>>>>>>> a9124e1e (release: merge staging into master (#1032))


FastRCNNObjectDetector is a model for detecting objects. MVITActionRecognition is a model for recognizing actions. 

ArrayCount and Crop are utility functions for counting the number of objects in an array and cropping a bounding box from an image, respectively.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
=======
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

Here is a query that illustrates how to use multiple functions in a single query.
=======
SELECT WITH MULTIPLE UDFS
-------------------------

Here is a query that illustrates how to use multiple UDFs in a single query.
>>>>>>> a9124e1e (release: merge staging into master (#1032))

.. code:: sql

   SELECT id, bbox, EmotionDetector(Crop(data, bbox)) 
   FROM HAPPY JOIN LATERAL UNNEST(FaceDetector(data)) AS Face(bbox, conf)  
   WHERE id < 15;
