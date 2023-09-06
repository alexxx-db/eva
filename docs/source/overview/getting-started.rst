<<<<<<< HEAD
<<<<<<< HEAD
.. _getting-started:
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. _getting-started:
=======
.. _Getting Started:
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. _getting-started:
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-master
=======
.. _Getting Started:
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))

Getting Started
=================

Install EvaDB 
-------------

<<<<<<< HEAD
To install EvaDB, we recommend using the `pip` package manager. EvaDB only supports Python versions greater than or equal to `3.9`.
=======
To install EvaDB, we recommend using the `pip` package manager.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

1. Create a new `virtual environment <https://docs.python-guide.org
/dev/virtualenvs/>`_ called `evadb-venv`.

.. code-block:: bash

    python -m venv evadb-venv
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> eva-master

<<<<<<< HEAD
.. warning::

    EvaDB only supports Python versions greater than or equal to `3.9`. You can check the version of your Python interpreter by running `python --version` on the terminal.

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
Now, activate the virtual environment:

.. code-block:: bash

    source evadb-venv/bin/activate

2. Once inside the virtual environment, run the command below to mitigate the dependency issues.

.. code-block:: bash

   pip install --upgrade pip setuptools wheel

3. Install EvaDB

.. code-block:: bash

<<<<<<< HEAD
   pip install --upgrade evadb

.. note::

    The `--upgrade` option ensure that the latest version of EvaDB is installed.

4. Verify EvaDB installation

.. code-block:: bash

   pip freeze

You should see a list of installed packages including but not limited to the following:

.. code-block:: bash

   Package           Version
   ----------------- -------
   aenum             3.1.15
   decorator         5.1.1
   diskcache         5.6.3
   evadb             0.3.7
   greenlet          2.0.2
   lark              1.1.7
   numpy             1.25.2
   pandas            2.1.0
   ...

5. Run EvaDB

Copy the following Python code to a file called `run_evadb.py`.

The program runs a SQL query for listing all the built-in functions in EvaDB. It consists of importing and connecting to EvaDB, and then running the query. The query's result is returned as a Dataframe.
=======
   pip install evadb

4. Verify EvaDB installation

.. code-block:: bash

   pip freeze

You should see a list of installed packages including but not limited to the following:

.. code-block:: bash

   Package           Version
   ----------------- -------
   aenum             3.1.15
   decorator         5.1.1
   diskcache         5.6.3
   evadb             0.3.3
   greenlet          2.0.2
   lark              1.1.7
   numpy             1.25.2
   pandas            2.1.0
   ...

5. Run EvaDB

Copy the following Python program to a file called `run_evadb.py`.

The program runs a SQL query for listing all the built-in functions in EvaDB. It consists of importing and connecting to EvaDB, and then running the query. The query's result is returned as a Dataframe.

.. code-block:: python

   # Import the EvaDB package 
   import evadb

   # Connect to EvaDB and get a database cursor for running queries
   cursor = evadb.connect().cursor()
<<<<<<< HEAD

   # List all the built-in functions in EvaDB
   print(cursor.query("SHOW FUNCTIONS;").df())

Now, run the Python program:

.. code-block:: bash
=======

   # List all the built-in functions in EvaDB
   print(cursor.query("SHOW FUNCTIONS;").df())

Now, run the Python program:

.. code-block:: bash

    python -m run_evadb.py

You should see a list of built-in functions including but not limited to the following:

.. code-block:: bash

            name                                             inputs  ...                                               impl metadata
    0  ArrayCount   [Input_Array NDARRAY ANYTYPE (), Search_Key ANY]  ...  /home/jarulraj3/evadb/evadb/functions/ndarray/array...       []
    1        Crop  [Frame_Array NDARRAY UINT8 (3, None, None), bb...  ...   /home/jarulraj3/evadb/evadb/functions/ndarray/crop.py       []
    2     ChatGPT  [query NDARRAY STR (1,), content NDARRAY STR (...  ...        /home/jarulraj3/evadb/evadb/functions/chatgpt.py       []

    [3 rows x 6 columns]

.. note::
    Go over the :ref:`Python API<python-api>` to learn more about `connect()` and `cursor`.

.. note::

    EvaDB supports additional installation options for extending its functionality. Go over the :doc:`Installation Options <getting-started/installation-options>` for all the available options.

Illustrative AI Query
---------------------

<<<<<<< HEAD
Here is a simple, illustrative `MNIST image classification <https://en.wikipedia.org/wiki/MNIST_database>`_ AI app in EvaDB.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Here is an illustrative `MNIST image classification <https://en.wikipedia.org/wiki/MNIST_database>`_ AI query in EvaDB.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

.. code-block:: sql
    
    --- This AI query retrieves images in the loaded MNIST video with label 4
    --- We constrain the query to only search through the first 100 frames
    --- We limit the query to only return the first five frames with label 4
    SELECT data, id, MnistImageClassifier(data) 
    FROM MnistVideo 
    WHERE MnistImageClassifier(data) = '4' AND id < 100
    LIMIT 5;

<<<<<<< HEAD
   # Import the EvaDB package 
   import evadb

<<<<<<< HEAD
   # Connect to EvaDB and get a database cursor for running queries
   cursor = evadb.connect().cursor()

   # List all the built-in functions in EvaDB
   print(cursor.query("SHOW FUNCTIONS;").df())
=======
    # Load the MNIST video into EvaDB
    # Each frame in the loaded MNIST video contains a digit
    cursor.load("mnist.mp4", "MNISTVid", format="video").df()

    # We now construct an AI pipeline to run the image classifier 
    # over all the digit images in the video    
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

Now, run the Python program:

<<<<<<< HEAD
.. code-block:: bash
=======
    # Run the model on a subset of frames
    # Here, id refers to the frame id
    query = query.filter("id = 30 OR id = 50 OR id = 70 OR id = 0 OR id = 140")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

    python -m run_evadb.py

You should see a list of built-in functions (with different filenames) including but not limited to the following:

<<<<<<< HEAD
.. code-block:: bash

            name                                             inputs  ...                                               impl metadata
    0  ArrayCount   [Input_Array NDARRAY ANYTYPE (), Search_Key ANY]  ...  /home/username/evadb/evadb-venv/functions/ndarray/array...       []
    1        Crop  [Frame_Array NDARRAY UINT8 (3, None, None), bb...  ...   /home/username/evadb/evadb-venv/functions/ndarray/crop.py       []
    2     ChatGPT  [query NDARRAY STR (1,), content NDARRAY STR (...  ...        /home/username/evadb/evadb/evadb-venv/chatgpt.py       []

    [3 rows x 6 columns]

.. note::
<<<<<<< HEAD
    Go over the :ref:`Python API<python-api>` to learn more about `connect()` and `cursor`.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

Now, activate the virtual environment:

<<<<<<< HEAD
.. code-block:: bash

    source evadb-venv/bin/activate

2. Once inside the virtual environment, run the command below to mitigate the dependency issues.

.. code-block:: bash

   pip install --upgrade pip setuptools wheel

3. Install EvaDB

.. code-block:: bash

   pip install evadb

4. Verify EvaDB installation

.. code-block:: bash

   pip freeze

You should see a list of installed packages including but not limited to the following:

.. code-block:: bash

   Package           Version
   ----------------- -------
   aenum             3.1.15
   decorator         5.1.1
   diskcache         5.6.3
   evadb             0.3.3
   greenlet          2.0.2
   lark              1.1.7
   numpy             1.25.2
   pandas            2.1.0
   ...

5. Run EvaDB

Copy the following Python program to a file called `run_evadb.py`.

The program runs a SQL query for listing all the built-in functions in EvaDB. It consists of importing and connecting to EvaDB, and then running the query. The query's result is returned as a Dataframe.
=======
    EvaDB supports additional installation options for extending its functionality. Go over the :doc:`Installation Options <getting-started/installation-options>` for all the available options.

Illustrative AI Query
---------------------

<<<<<<< HEAD
Here is a simple, illustrative `MNIST image classification <https://en.wikipedia.org/wiki/MNIST_database>`_ AI app in EvaDB.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Here is an illustrative `MNIST image classification <https://en.wikipedia.org/wiki/MNIST_database>`_ AI query in EvaDB.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

.. code-block:: sql
    
    --- This AI query retrieves images in the loaded MNIST video with label 4
    --- We constrain the query to only search through the first 100 frames
    --- We limit the query to only return the first five frames with label 4
    SELECT data, id, MnistImageClassifier(data) 
    FROM MnistVideo 
    WHERE MnistImageClassifier(data) = '4' AND id < 100
    LIMIT 5;

<<<<<<< HEAD
   # Import the EvaDB package 
   import evadb

<<<<<<< HEAD
   # Connect to EvaDB and get a database cursor for running queries
   cursor = evadb.connect().cursor()

   # List all the built-in functions in EvaDB
   print(cursor.query("SHOW FUNCTIONS;").df())
=======
    # Load the MNIST video into EvaDB
    # Each frame in the loaded MNIST video contains a digit
    cursor.load("mnist.mp4", "MNISTVid", format="video").df()

    # We now construct an AI pipeline to run the image classifier 
    # over all the digit images in the video    
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

Now, run the Python program:

<<<<<<< HEAD
.. code-block:: bash
=======
    # Run the model on a subset of frames
    # Here, id refers to the frame id
    query = query.filter("id = 30 OR id = 50 OR id = 70 OR id = 0 OR id = 140")
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master

    python -m run_evadb.py

You should see a list of built-in functions including but not limited to the following:

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> eva-master
.. code-block:: bash

            name                                             inputs  ...                                               impl metadata
    0  ArrayCount   [Input_Array NDARRAY ANYTYPE (), Search_Key ANY]  ...  /home/jarulraj3/evadb/evadb/functions/ndarray/array...       []
    1        Crop  [Frame_Array NDARRAY UINT8 (3, None, None), bb...  ...   /home/jarulraj3/evadb/evadb/functions/ndarray/crop.py       []
    2     ChatGPT  [query NDARRAY STR (1,), content NDARRAY STR (...  ...        /home/jarulraj3/evadb/evadb/functions/chatgpt.py       []

    [3 rows x 6 columns]

.. note::
    Go over the :ref:`Python API<python-api>` to learn more about `connect()` and `cursor`.
=======
    Go over the :ref:`Python API<python-api>` page to learn more about `connect()` and `cursor`.
>>>>>>> ad7bb302 (docs: updates)

.. note::

    EvaDB supports additional installation options for extending its functionality. Go over the :doc:`Installation Options <getting-started/installation-options>` page for all the available options.

Illustrative AI Query
---------------------

Here is an illustrative EvaQL query that analyzes the sentiment of restaurant food reviews and responds to them.

.. code-block:: sql
    
    --- This AI query analyses the sentiment of restaurant food reviews stored 
    --- in a database table and generates a response to negative food reviews
    --- using another ChatGPT call to address the concerns shared in the review
    SELECT
        ChatGPT("Respond to the review with a solution to address the reviewer's concern",
        review)     
    FROM
        postgres_data.review_table     
    WHERE
        ChatGPT("Is the review positive or negative?", review) = "negative";

More details on this usecase is available in the :ref:`Sentiment Analysis <sentiment-analysis>` page. 

<<<<<<< HEAD
<<<<<<< HEAD
The complete `Sentiment Analysis notebook is available on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`_.
Try out EvaDB by experimenting with this introductory notebook.
<<<<<<< HEAD
=======
=======
Try out EvaDB by experimenting with the introductory `MNIST notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. include:: ../shared/designs/design2.rst
=======
Try out EvaDB by experimenting with the introductory `MNIST notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_.

>>>>>>> 7dd70375 (release: merge staging into master (#1032))
.. image:: ../../images/reference/mnist.png

.. note::
    Go over the :ref:`Python API<python-api>` to learn more about the functions used in this app.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
The complete `MNIST notebook is available on Colab <https://colab.research.google.com/github/georgia-tech-db/evadb/blob/master/tutorials/01-mnist.ipynb>`_.
Try out EvaDB by experimenting with this introductory notebook.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-master
=======
The complete `Sentiment Analysis notebook is available on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`_. Try out EvaDB by experimenting with this notebook :)
>>>>>>> 8379a400 (docs: updates)
=======
Try out EvaDB by experimenting with the complete `sentiment analysis notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`_ 🙂
<<<<<<< HEAD
>>>>>>> 1291df05 (docs: updates)
=======

.. include:: ../shared/design1.rst
>>>>>>> 118120e7 (docs: updates)
=======
.. include:: ../shared/design2.rst
>>>>>>> dc9069a2 (docs: updates)
=======
.. include:: ../shared/designs/design2.rst
>>>>>>> 08db5ebb (docs: updated images)
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
