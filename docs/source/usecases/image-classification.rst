<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. _image-classification:
=======
=======
=======
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
.. _image-classification:
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
.. _image-classification:
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
<<<<<<< HEAD
<<<<<<< HEAD
.. _image-classification:
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
.. _image-classification:
=======
=======
.. _image-classification:
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
.. _image classification:

Image Classification Pipeline using EvaDB
=========================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master

Image Classification
====================

<<<<<<< HEAD
.. raw:: html
=======
<<<<<<< HEAD
.. raw:: html
=======
1. Connect to EvaDB
-------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master

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
<<<<<<< HEAD
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
=======
2. Register Image Classification Model as a Function in SQL
-----------------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master

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
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
.. _image-classification:
=======
.. _image classification:

Image Classification Pipeline using EvaDB
=========================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
.. _image-classification:
=======
.. _image classification:

Image Classification Pipeline using EvaDB
=========================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
.. _image-classification:
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))

Image Classification
====================

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
.. raw:: html
=======
1. Connect to EvaDB
-------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
.. raw:: html
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

    <embed>
    <table align="left">
    <td>
<<<<<<< HEAD
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/01-mnist.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
    </td>
    </table><br><br>
    </embed>

Introduction
------------

<<<<<<< HEAD
<<<<<<< HEAD
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
=======
2. Register Image Classification Model as a Function in SQL
-----------------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.
=======
Create Image Classification Function
------------------------------------

<<<<<<< HEAD
To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_.
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.
>>>>>>> ae08f806 (Bump v0.3.4+ dev)

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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
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
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
=======
2. Register Image Classification Model as a Function in SQL
-----------------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
In this tutorial, we present how to use ``PyTorch`` models in EvaDB to classify images. In particular, we focus on classifying images from the ``MNIST`` dataset that contains ``digits``. EvaDB makes it easy to do image classification using its built-in support for ``PyTorch`` models.
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))

In this tutorial, besides classifying images, we will also showcase a query where the model's output is used to retrieve images with the digit ``6``.

.. include:: ../shared/evadb.rst

We will assume that the input ``MNIST`` video is loaded into ``EvaDB``. To download the video and load it into ``EvaDB``, see the complete `image classification notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
Create Image Classification Function
------------------------------------
=======
3. Execute Image Classification through SQL
-------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

<<<<<<< HEAD
To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_.
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
To create a custom ``MnistImageClassifier`` function, use the ``CREATE FUNCTION`` statement. The code for the custom classification model is available `here <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_.
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
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
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
    +------------------------------+
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
    +------------------------------+
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
    +------------------------------+
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
    +------------------------------+
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    +------------------------------+
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    +------------------------------+
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
    +------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
    +------------------------------+
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
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main


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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/footer.rst
=======
=======
<<<<<<< HEAD
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
.. include:: ../shared/footer.rst
=======
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
>>>>>>> eva-source
=======
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
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
.. include:: ../shared/footer.rst
=======
>>>>>>> e867f37e (docs: updated images)
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
.. include:: ../shared/footer.rst
<<<<<<< HEAD
=======

.. include:: ../shared/designs/design7.rst
>>>>>>> eva-source
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
>>>>>>> eva-master
=======
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
>>>>>>> 08db5ebb (docs: updated images)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e867f37e (docs: updated images)
=======
>>>>>>> eva-source
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
.. include:: ../shared/footer.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
>>>>>>> 08db5ebb (docs: updated images)
<<<<<<< HEAD
>>>>>>> e867f37e (docs: updated images)
=======
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5678c9a3 (docs: updated images)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
.. include:: ../shared/footer.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> eva-master
=======
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
>>>>>>> 08db5ebb (docs: updated images)
<<<<<<< HEAD
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
>>>>>>> 5678c9a3 (docs: updated images)
=======
=======
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design7.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_ for working example.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
.. include:: ../shared/footer.rst
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
.. include:: ../shared/footer.rst
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
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
