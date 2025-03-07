.. _image-search:

Image Search
============

.. raw:: html

    <embed>
    <table align="left">
    <td>
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
>>>>>>> fbfc3ace (docs: updates)
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
<<<<<<< HEAD
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
>>>>>>> fbfc3ace (docs: updates)
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/11-similarity-search-for-motif-mining.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    </td>
    </table><br><br>
    </embed>

Introduction
------------

In this tutorial, we present how to use classical vision models (i.e., ``SIFT feature extractor``) in EvaDB to search for similar images powered by a ``vector index``. In particular, we focus on retrieving similar images from the ``Reddit`` dataset that contain similar ``motifs``. EvaDB makes it easy to do image search using its built-in support for vision models and vector database systems (e.g., ``FAISS``).

.. include:: ../shared/evadb.rst

We will assume that the input ``Reddit`` image collection is loaded into ``EvaDB``. To download this image dataset and load it into ``EvaDB``, see the complete `image search notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/11-similarity-search-for-motif-mining.ipynb>`_.

Create Image Feature Extraction Function
----------------------------------------

To create a custom ``SiftFeatureExtractor`` function, use the ``CREATE FUNCTION`` statement. We will assume that the file is downloaded and stored as ``sift_feature_extractor.py``. Now, run the following query to register this function:

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
.. code-block:: sql

    CREATE FUNCTION 
        IF NOT EXISTS SiftFeatureExtractor
        IMPL  'evadb/udfs/sift_feature_extractor.py'
=======
.. tab-set::
    
    .. tab-item:: Python

        .. code-block:: python

            cursor.query("""
                CREATE FUNCTION 
                IF NOT EXISTS SiftFeatureExtractor
                IMPL  'evadb/udfs/sift_feature_extractor.py'
            """).df()

    .. tab-item:: SQL 

        .. code-block:: sql

            CREATE FUNCTION 
                IF NOT EXISTS SiftFeatureExtractor
                IMPL  'evadb/udfs/sift_feature_extractor.py'
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. code-block:: sql

    CREATE FUNCTION 
        IF NOT EXISTS SiftFeatureExtractor
        IMPL  'evadb/udfs/sift_feature_extractor.py'
>>>>>>> f916e34f (docs: updates)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main


Create Vector Index for Similar Image Search
--------------------------------------------

To locate images with similar appearance, we next create an index based on the feature vectors returned by ``SiftFeatureExtractor`` on the loaded images. EvaDB will later use this vector index to quickly returns similar images.

EvaDB lets you connect to your favorite vector database via the ``CREATE INDEX`` statement. In this query, we will create a new index using the ``FAISS`` vector index framework from ``Meta``.

The following EvaQL statement creates a vector index on the ``SiftFeatureExtractor(data)`` column in the ``reddit_dataset`` table:

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
.. code-block:: sql

    CREATE INDEX reddit_sift_image_index 
        ON reddit_dataset (SiftFeatureExtractor(data)) 
        USING FAISS;
=======
.. tab-set::
    
    .. tab-item:: Python

        .. code-block:: python

            cursor.query("""
                CREATE INDEX reddit_sift_image_index 
                ON reddit_dataset (SiftFeatureExtractor(data)) 
                USING FAISS;
            """).df()

    .. tab-item:: SQL 

        .. code-block:: sql

            CREATE INDEX reddit_sift_image_index 
                ON reddit_dataset (SiftFeatureExtractor(data)) 
                USING FAISS;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. code-block:: sql

    CREATE INDEX reddit_sift_image_index 
        ON reddit_dataset (SiftFeatureExtractor(data)) 
        USING FAISS;
>>>>>>> f916e34f (docs: updates)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

Similar Image Search Powered By Vector Index
--------------------------------------------

EvaQL supports the ``ORDER BY`` and ``LIMIT`` clauses to retrieve the ``top-k`` most similar images for a given image. 

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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> fb00f6de (ran spellchecker)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
EvaDB contains a built-in ``Similarity(x, y)`` function that computes the Euclidean distance between ``x`` and ``y``. We will use this function to compare the feature vector of image being search (i.e., the given image) and the feature vectors of all the images in the dataset that is stored in the vector index.

EvaDB's query optimizer automatically picks the correct vector index to accelerate a given EvaQL query. It uses the vector index created in the prior step to accelerate the following image search query:

<<<<<<< HEAD

.. code-block:: sql

    SELECT name FROM reddit_dataset ORDER BY
    Similarity(
        SiftFeatureExtractor(Open('reddit-images/g1074_d4mxztt.jpg')),
        SiftFeatureExtractor(data)
    )
    LIMIT 5
=======
EvaDB contains a built-in ``Similarity(x, y)`` function that computets the Euclidean distance between ``x`` and ``y``. We will use this function to compare the feature vector of image being search (i.e., the given image) and the feature vectors of all the images in the dataset that is stored in the vector index.
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
EvaDB contains a built-in ``Similarity(x, y)`` function that computes the Euclidean distance between ``x`` and ``y``. We will use this function to compare the feature vector of image being search (i.e., the given image) and the feature vectors of all the images in the dataset that is stored in the vector index.
>>>>>>> 5b27053e (ran spellchecker)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
EvaDB contains a built-in ``Similarity(x, y)`` function that computes the Euclidean distance between ``x`` and ``y``. We will use this function to compare the feature vector of image being search (i.e., the given image) and the feature vectors of all the images in the dataset that is stored in the vector index.
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> fb00f6de (ran spellchecker)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

EvaDB's query optimizer automatically picks the correct vector index to accelerate a given EvaQL query. It uses the vector index created in the prior step to accelerate the following image search query:

.. tab-set::
    
    .. tab-item:: Python
<<<<<<< HEAD

        .. code-block:: python

=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f916e34f (docs: updates)

.. code-block:: sql

<<<<<<< HEAD
=======

        .. code-block:: python

>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======

        .. code-block:: python

>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
            query = cursor.query("""
                SELECT name FROM reddit_dataset ORDER BY
                Similarity(
                    SiftFeatureExtractor(Open('reddit-images/g1074_d4mxztt.jpg')),
                    SiftFeatureExtractor(data)
                )
                LIMIT 5
            """).df()

    .. tab-item:: SQL 

        .. code-block:: sql

            SELECT name FROM reddit_dataset ORDER BY
            Similarity(
                SiftFeatureExtractor(Open('reddit-images/g1074_d4mxztt.jpg')),
                SiftFeatureExtractor(data)
            )
            LIMIT 5

.. code-block:: python
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
    SELECT name FROM reddit_dataset ORDER BY
    Similarity(
        SiftFeatureExtractor(Open('reddit-images/g1074_d4mxztt.jpg')),
        SiftFeatureExtractor(data)
    )
    LIMIT 5
>>>>>>> f916e34f (docs: updates)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

This query returns the top-5 most similar images in a ``DataFrame``:

.. code-block::

    +---------------------------------+
    | reddit_dataset.name             |
    |---------------------------------|
    | reddit-images/g1074_d4mxztt.jpg |
    | reddit-images/g348_d7ju7dq.jpg  |
    | reddit-images/g1209_ct6bf1n.jpg |
    | reddit-images/g1190_cln9xzr.jpg |
    | reddit-images/g1190_clna2x2.jpg |
    +---------------------------------+

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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design8.rst
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design8.rst
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
