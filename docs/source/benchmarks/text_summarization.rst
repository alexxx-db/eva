<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
Text Summarization Benchmark 
============================

In this benchmark, we compare the runtime performance of EvaDB and MindsDB on 
a text summarization application operating on a news dataset. In particular, 
we focus on the `CNN-DailyMail News <https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail>`_ dataset.

All the relevant files are located in the `text summarization benchmark folder on Github <https://github.com/georgia-tech-db/evadb/tree/staging/benchmark/text_summarization>`_.

Prepare dataset
---------------
<<<<<<< HEAD
=======
=======
Text summarization benchmark 
=======
Text Summarization Benchmark 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
============================

<<<<<<< HEAD
1. Prepare dataset
------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
In this benchmark, we compare the runtime performance of EvaDB and MindsDB on 
a text summarization application operating on a news dataset. In particular, 
we focus on the `CNN-DailyMail News <https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail>`_ dataset.

All the relevant files are located in the `text summarization benchmark folder on Github <https://github.com/georgia-tech-db/evadb/tree/staging/benchmark/text_summarization>`_.

Prepare dataset
---------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master

.. code-block:: bash

   cd benchmark/text_summarization
   bash download_dataset.sh

<<<<<<< HEAD
Use EvaDB for Text Summarization
--------------------------------
=======
<<<<<<< HEAD
<<<<<<< HEAD
Use EvaDB for Text Summarization
--------------------------------
=======
2. Using EvaDB to summarize the CNN DailyMail News
--------------------------------------------------
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Use EvaDB for Text Summarization
--------------------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master

.. note::
 
   Install ``ray`` along with EvaDB to speed up the queries: 
   ``pip install evadb[ray]``
   
.. code-block:: bash

   cd benchmark/text_summarization
   python text_summarization_with_evadb.py


<<<<<<< HEAD
Loading Data Into EvaDB
~~~~~~~~~~~~~~~~~~~~~~~

=======
<<<<<<< HEAD
<<<<<<< HEAD
Loading Data Into EvaDB
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS cnn_news_test(
        id TEXT(128),
        article TEXT(4096),
        highlights TEXT(1024)
      );

Creating Text Summarization Function in EvaDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   CREATE UDF IF NOT EXISTS TextSummarizer
         TYPE HuggingFace
         TASK 'summarization'
         MODEL 'sshleifer/distilbart-cnn-12-6'
         MIN_LENGTH 5
         MAX_LENGTH 100;


Tuning EvaDB for Maximum GPU Utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   cursor._evadb.config.update_value("executor", "batch_mem_size", 300000)
   cursor._evadb.config.update_value("executor", "gpu_ids", [0,1])
   cursor._evadb.config.update_value("experimental", "ray", True)


Text Summarization Query in EvaDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS cnn_news_summary AS
    SELECT TextSummarizer(article) FROM cnn_news_test;

Use MindsDB for Text Summarization
-----------------------------------

Setup SQLite Database 
~~~~~~~~~~~~~~~~~~~~~~
=======
3. Using MindsDB to summarize the CNN DailyMail News
----------------------------------------------------

Prepare sqlite database for MindsDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Loading Data Into EvaDB
~~~~~~~~~~~~~~~~~~~~~~~

>>>>>>> eva-master
.. code-block:: sql

    CREATE TABLE IF NOT EXISTS cnn_news_test(
        id TEXT(128),
        article TEXT(4096),
        highlights TEXT(1024)
      );

Creating Text Summarization Function in EvaDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   CREATE UDF IF NOT EXISTS TextSummarizer
         TYPE HuggingFace
         TASK 'summarization'
         MODEL 'sshleifer/distilbart-cnn-12-6'
         MIN_LENGTH 5
         MAX_LENGTH 100;


Tuning EvaDB for Maximum GPU Utilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   cursor._evadb.config.update_value("executor", "batch_mem_size", 300000)
   cursor._evadb.config.update_value("executor", "gpu_ids", [0,1])
   cursor._evadb.config.update_value("experimental", "ray", True)


Text Summarization Query in EvaDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS cnn_news_summary AS
    SELECT TextSummarizer(article) FROM cnn_news_test;

Use MindsDB for Text Summarization
-----------------------------------

Setup SQLite Database 
~~~~~~~~~~~~~~~~~~~~~~
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master

.. code-block:: bash

   sqlite3 cnn_news_test.db
   > .mode csv
   > .import cnn_news_test.csv cnn_news_test
   > .exit


Install MindsDB
~~~~~~~~~~~~~~~

<<<<<<< HEAD
Follow the `MindsDB nstallation guide <https://docs.mindsdb.com/setup/self-hosted/pip/source>`_ to install it via ``pip``.

.. note::

   You will need to manually run ``pip install evaluate`` for the ``HuggingFace`` model to work in MindsDB.

=======
<<<<<<< HEAD
<<<<<<< HEAD
Follow the `MindsDB nstallation guide <https://docs.mindsdb.com/setup/self-hosted/pip/source>`_ to install it via ``pip``.

.. note::

   You will need to manually run ``pip install evaluate`` for the ``HuggingFace`` model to work in MindsDB.
=======
Follow the `Setup for Source Code via pip <https://docs.mindsdb.com/setup/self-hosted/pip/source>`_ to install mindsdb.

.. note::

   At the time of this documentation, we need to manually ``pip install evaluate`` for huggingface model to work in MindsDB.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Follow the `MindsDB nstallation guide <https://docs.mindsdb.com/setup/self-hosted/pip/source>`_ to install it via ``pip``.

.. note::

   You will need to manually run ``pip install evaluate`` for the ``HuggingFace`` model to work in MindsDB.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

>>>>>>> eva-master
After installation, use the ``MySQL`` client for connecting to ``MindsDB``. Update the port number if needed.

.. code-block:: bash

   mysql -h 127.0.0.1 --port 47335 -u mindsdb -p

<<<<<<< HEAD
Benchmark MindsDB 
~~~~~~~~~~~~~~~~~
=======
<<<<<<< HEAD
<<<<<<< HEAD
Benchmark MindsDB 
~~~~~~~~~~~~~~~~~
=======
Run Experiment
~~~~~~~~~~~~~~
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Benchmark MindsDB 
~~~~~~~~~~~~~~~~~
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master

Connect ``MindsDB`` to the ``sqlite`` database we created before:

.. code-block:: text

   CREATE DATABASE sqlite_datasource
   WITH ENGINE = 'sqlite',
   PARAMETERS = {
     "db_file": "cnn_news_test.db"
   };

Create a ``text summarization`` model and wait for it to be ``ready``.

.. code-block:: text

   CREATE MODEL mindsdb.hf_bart_sum_20
   PREDICT PRED
   USING
   engine = 'huggingface',
   task = 'summarization',
   model_name = 'sshleifer/distilbart-cnn-12-6',
   input_column = 'article',
   min_output_length = 5,
   max_output_length = 100;

   DESCRIBE mindsdb.hf_bart_sum_20;

Use the ``text summarization`` model to summarize the CNN news dataset:

.. code-block:: text

   CREATE OR REPLACE TABLE sqlite_datasource.cnn_news_summary (
     SELECT PRED
     FROM mindsdb.hf_bart_sum_20
     JOIN sqlite_datasource.cnn_news_test
   );


<<<<<<< HEAD
Benchmarking Results
--------------------
=======
<<<<<<< HEAD
<<<<<<< HEAD
Benchmarking Results
--------------------
=======
4. Experiment results
---------------------
Below are numbers from a server with 56 Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz and two Quadro P6000 GPU.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Benchmarking Results
--------------------
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master

Here are the key runtime metrics for the ``Text Summarization`` benchmark.

The experiment is conducted on a server with 56 Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz and two Quadro P6000 GPUs.

.. list-table::
   :widths: 20 30 30 30

   * - 
     - **MindsDB**
     - **EvaDB** 
     - **EvaDB**
   * - 
     - **(off-the-shelf)**
     - **(off-the-shelf)**
     - **(tuned for maximum**
   * - 
     - 
     - 
     - **GPU utilization)**     
   * - **Runtime**
     - 4 hours 45 mins
     - 1 hour 10 mins
     - 43 mins
   * - **Speedup**
     - 1x
     - 4.1x
     - 6.3x 
