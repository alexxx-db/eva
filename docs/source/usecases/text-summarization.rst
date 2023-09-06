.. _text-summarization:

Text Summarization 
==================

.. raw:: html

    <embed>
    <table align="left">
    <td>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
<<<<<<< HEAD
<<<<<<< HEAD
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
>>>>>>> fbfc3ace (docs: updates)
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
<<<<<<< HEAD
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
>>>>>>> fbfc3ace (docs: updates)
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/12-query-pdf.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
    </td>
    </table><br><br>
    </embed>


Introduction
------------

In this tutorial, we present how to use ``HuggingFace`` models in EvaDB to summarize and classify text. In particular, we will first load ``PDF`` documents into ``EvaDB`` using the ``LOAD PDF`` statement. The text in each paragraph from the PDF is automatically stored in the ``data`` column of a table for subsequent analysis. We then run text summarization and text classification AI queries on the ``data`` column obtained from the loaded ``PDF`` documents.

EvaDB makes it easy to process text using its built-in support for ``HuggingFace``.

.. include:: ../shared/evadb.rst

We will assume that the input ``pdf_sample1`` PDF is loaded into ``EvaDB``. To download the PDF and load it into ``EvaDB``, see the complete `text summarization notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/master/tutorials/12-query-pdf.ipynb>`_.


Create Text Summarization and Classification Functions
------------------------------------------------------

To create custom ``TextSummarizer`` and ``TextClassifier`` functions, use the ``CREATE FUNCTION`` statement. In these queries, we leverage EvaDB's built-in support for ``HuggingFace`` models. We only need to specify the ``task`` and the ``model`` parameters in the query to create these functions:

.. code-block:: sql

        CREATE FUNCTION IF NOT EXISTS TextSummarizer
        TYPE HuggingFace
        TASK 'summarization'
        MODEL 'facebook/bart-large-cnn';

        CREATE FUNCTION IF NOT EXISTS TextClassifier
        TYPE HuggingFace
        TASK 'text-classification'
        MODEL 'distilbert-base-uncased-finetuned-sst-2-english';

.. note::
    
    EvaDB has built-in support for a wide range of :ref:`HuggingFace<hf>` models.

AI Query Using Registered Functions
-----------------------------------

After registering these two functions, we use them in a single AI query over the ``data`` column to retrieve a subset of paragraphs from the loaded ``PDF`` documents with `negative` sentiment:

.. code-block:: sql

        CREATE TABLE text_summary AS 
        SELECT data, TextSummarizer(data) 
        FROM MyPDFs
        WHERE page = 1 
              AND paragraph >= 1 AND paragraph <= 3
              AND TextClassifier(data).label = 'NEGATIVE';

Here, the ``TextClassifier`` function is applied on the ``data`` column of the ``pdf_sample1`` PDF loaded into EvaDB and its output is used to filter out a subset of paragraphs with `negative sentiment`. 

EvaDB's query optimizer automatically applies the earlier predicates on page number and paragraph numbers to (e.g., ``page = 1``) to avoid running the expensive ``TextClassifier`` function on all the rows in the table. After filtering out a subset of paragraphs, EvaDB applies the ``TextSummarizer`` function to derive their summaries.

Here is the query's output ``DataFrame``:

.. code-block:: 

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
    +--------------------------------------------------------------+--------------------------------------------------------------+
    |                         mypdfs.data                          |                 textsummarizer.summary_text                  |
    +--------------------------------------------------------------+--------------------------------------------------------------+
    | DEFINATION  Specialized connective tissue with          ... | Specialized connective tissue with fluid matrix. Erythro ... |
    | PHYSICAL CHARACTERISTICS ( 1 )  COLOUR   -- Red  ( 2 )  ... | The temperature is 38° C / 100.4° F. The body weight is  ... |
    +--------------------------------------------------------------+--------------------------------------------------------------+
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
    +--------------------------------------------------------+--------------------------------------------------------+
    | mypdfs.data                                         | mypdfs.summary_text                             |
    +--------------------------------------------------------+--------------------------------------------------------+
    | DEFINATION  Specialized connective tissue wit...  | Specialized connective tissue with fluid matri... |
    | PHYSICAL CHARACTERISTICS ( 1 ) COLOUR -- R...  | The temperature is 38° C / 100.4° F. The body ...  |
    +--------------------------------------------------------+--------------------------------------------------------+
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
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
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))


.. include:: ../shared/nlp.rst

.. include:: ../shared/footer.rst
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))

<<<<<<< HEAD
.. include:: ../shared/designs/design2.rst
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======

.. include:: ../shared/design2.rst
>>>>>>> f398c41b (docs: updates)
=======
.. include:: ../shared/designs/design2.rst
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 864a7bed (docs: updates)
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))

.. include:: ../shared/designs/design2.rst
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======

.. include:: ../shared/designs/design2.rst
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======

.. include:: ../shared/design2.rst
>>>>>>> f398c41b (docs: updates)
>>>>>>> 864a7bed (docs: updates)
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
