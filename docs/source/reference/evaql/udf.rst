:orphan:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))

Functions
=========

SHOW FUNCTIONS
--------------
=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

Functions
=========

<<<<<<< HEAD
SHOW UDFS
---------
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
SHOW FUNCTIONS
--------------
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
UDF
===
=======
Functions
=========
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

<<<<<<< HEAD
SHOW UDFS
---------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
SHOW FUNCTIONS
--------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======

Functions
=========

<<<<<<< HEAD
SHOW UDFS
---------
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
SHOW FUNCTIONS
--------------
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
UDF
===
=======
Functions
=========
>>>>>>> f75511e6 (feat: sync master staging (#1050))

<<<<<<< HEAD
SHOW UDFS
---------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
SHOW FUNCTIONS
--------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))

Here is a list of built-in user-defined functions in EvaDB.

.. code:: mysql

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    SHOW FUNCTIONS;

    id   name                    impl
    0    FastRCNNObjectDetector  evadb/functions/fastrcnn_object_detector.p
    1    MVITActionRecognition   evadb/functions/mvit_action_recognition.py
    2    ArrayCount              evadb/functions/ndarray/array_count.py
    3    Crop                    evadb/evadb/functions/ndarray/crop.py
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
    SHOW UDFS;

    id   name                    impl
    0    FastRCNNObjectDetector  evadb/udfs/fastrcnn_object_detector.p
    1    MVITActionRecognition   evadb/udfs/mvit_action_recognition.py
    2    ArrayCount              evadb/udfs/ndarray/array_count.py
    3    Crop                    evadb/evadb/udfs/ndarray/crop.py
<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
    SHOW FUNCTIONS;

    id   name                    impl
=======
    SHOW FUNCTIONS;

    id   name                    impl
>>>>>>> f431fb09 (feat: sync master staging (#1050))
    0    FastRCNNObjectDetector  evadb/functions/fastrcnn_object_detector.p
    1    MVITActionRecognition   evadb/functions/mvit_action_recognition.py
    2    ArrayCount              evadb/functions/ndarray/array_count.py
    3    Crop                    evadb/evadb/functions/ndarray/crop.py
<<<<<<< HEAD
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))


FastRCNNObjectDetector is a model for detecting objects. MVITActionRecognition is a model for recognizing actions. 

ArrayCount and Crop are utility functions for counting the number of objects in an array and cropping a bounding box from an image, respectively.

<<<<<<< HEAD
<<<<<<< HEAD
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
SELECT WITH MULTIPLE UDFS
-------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
SELECT WITH MULTIPLE FUNCTIONS
------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

Here is a query that illustrates how to use multiple functions in a single query.
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
SELECT WITH MULTIPLE UDFS
-------------------------

Here is a query that illustrates how to use multiple UDFs in a single query.
<<<<<<< HEAD
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
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
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))

.. code:: sql

   SELECT id, bbox, EmotionDetector(Crop(data, bbox)) 
   FROM HAPPY JOIN LATERAL UNNEST(FaceDetector(data)) AS Face(bbox, conf)  
   WHERE id < 15;
