<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. _image-classification:
=======
.. _image classification:

Image Classification Pipeline using EvaDB
=========================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

Image Classification
====================

<<<<<<< HEAD
.. raw:: html
=======
1. Connect to EvaDB
-------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

    <embed>
    <table align="left">
    <td>
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
    </td>
    </table><br><br>
    </embed>

Introduction
------------

<<<<<<< HEAD
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
=======
2. Register Image Classification Model as a Function in SQL
-----------------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.

We will assume that the file is downloaded and stored as ``mnist_image_classifier.py``. Now, run the following query to register the AI function:

.. code-block:: sql

        CREATE FUNCTION 
        IF NOT EXISTS MnistImageClassifier 
        IMPL 'mnist_image_classifier.py';

Image Classification Queries
----------------------------

After the function is registered in ``EvaDB``, you can use it subsequent SQL queries in different ways. 

In the following query, we call the classifier on every image in the video. The output of the function is stored in the ``label`` column (i.e., the digit associated with the given frame) of the output ``DataFrame``.

.. code-block:: sql

    SELECT MnistImageClassifier(data).label 
    FROM mnist_video;

=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
.. _image-classification:
=======
.. _image classification:

Image Classification Pipeline using EvaDB
=========================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

Image Classification
====================

<<<<<<< HEAD
.. raw:: html
=======
1. Connect to EvaDB
-------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

    <embed>
    <table align="left">
    <td>
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
    </td>
    </table><br><br>
    </embed>

Introduction
------------

<<<<<<< HEAD
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
=======
2. Register Image Classification Model as a Function in SQL
-----------------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.

We will assume that the file is downloaded and stored as ``mnist_image_classifier.py``. Now, run the following query to register the AI function:

.. code-block:: sql

        CREATE FUNCTION 
        IF NOT EXISTS MnistImageClassifier 
        IMPL 'mnist_image_classifier.py';

Image Classification Queries
----------------------------

After the function is registered in ``EvaDB``, you can use it subsequent SQL queries in different ways. 

In the following query, we call the classifier on every image in the video. The output of the function is stored in the ``label`` column (i.e., the digit associated with the given frame) of the output ``DataFrame``.

.. code-block:: sql

    SELECT MnistImageClassifier(data).label 
    FROM mnist_video;

<<<<<<< HEAD
=======
=======
.. _image-classification:

Image Classification
====================

.. raw:: html

    <embed>
    <table align="left">
    <td>
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
    </td>
    </table><br><br>
    </embed>

Introduction
------------

In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

Create Image Classification Function
------------------------------------

To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.

We will assume that the file is downloaded and stored as ``mnist_image_classifier.py``. Now, run the following query to register the AI function:

.. code-block:: sql

        CREATE FUNCTION 
        IF NOT EXISTS MnistImageClassifier 
        IMPL 'mnist_image_classifier.py';

Image Classification Queries
----------------------------

After the function is registered in ``EvaDB``, you can use it subsequent SQL queries in different ways. 

In the following query, we call the classifier on every image in the video. The output of the function is stored in the ``label`` column (i.e., the digit associated with the given frame) of the output ``DataFrame``.

.. code-block:: sql

    SELECT MnistImageClassifier(data).label 
    FROM mnist_video;

>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
This query returns the label of all the images:

.. code-block:: 

    +------------------------------+
    |   mnistimageclassifier.label |
    |------------------------------|
    |                            6 |
    |                            6 |
    |                          ... |
    |                          ... |
    |                          ... |
    |                          ... |
    |                            4 |
    |                            4 |
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
    +------------------------------+
=======

    ... ...

4. Optional: Process Only Segments of Videos based on Conditions
-----------------------------------------------------------------

Like normal SQL, you can also specify conditions to filter out some frames of the video.

.. tab-set::
    
    .. tab-item:: Python

        .. code-block:: python

            query = cursor.table("mnist_video") \
                        .filter("id < 2") \
                        .select("MnistImageClassifier(data).label")
            
            # Return results in a DataFrame.
            query.df()

    .. tab-item:: SQL

        .. code-block:: sql

            SELECT MnistImageClassifier(data).label FROM mnist_video 
                WHERE id < 2
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))


Filtering Based on AI Function
------------------------------

In the following query, we use the output of the classifier to retrieve a subset of images that contain a particular digit (e.g., ``6``).

.. code-block:: sql

    SELECT id, MnistImageClassifier(data).label 
        FROM mnist_video 
        WHERE MnistImageClassifier(data).label = '6';

Now, the ``DataFrame`` only contains images of the digit ``6``.

.. code-block:: 

    +------------------------------+
    |   mnistimageclassifier.label |
    |------------------------------|
    |                            6 |
    |                            6 |
    +------------------------------+

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
.. include:: ../shared/footer.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
