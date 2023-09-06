.. _sentiment-analysis:

Sentiment Analysis
==================

.. raw:: html

    <embed>
    <table align="left">
    <td>
<<<<<<< HEAD
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
    </td>
    </table><br><br>
    </embed>

Introduction
------------

In this tutorial, we present how to use OpenAI models in EvaDB to analyse sentiment in text data. In particular, we focus on analysing sentiments expressed by customers in food reviews. EvaDB makes it easy to do sentiment analysis using its built-in ChatGPT AI function. In this tutorial, besides classifying sentiment, we will also use another query to generate responses to customers for addressing ``negative`` reviews.

We will assume that the input data is loaded into a ``PostgreSQL`` database. 
To load the food review data into your database, see the complete `sentiment analysis notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`_.

.. include:: ../shared/evadb.rst

.. include:: ../shared/postgresql.rst

Sentiment Analysis of Reviews using ChatGPT
-------------------------------------------

We run the following query to analyze whether the review is ``positive`` or ``negative`` with a custom ChatGPT prompt. Here, the query runs on the ``review`` column in the ``review_table`` that is a part of the ``PostgreSQL`` database.

.. code-block:: sql

    SELECT ChatGPT(
        "Is the review positive or negative? Only reply 'positive' or 'negative'. Here are examples. The food is very bad: negative. The food is very good: positive.",
        review)
    FROM postgres_data.review_table;

This query returns the sentiment of the reviews in the table:

.. code-block:: 

    +------------------------------+
    |             chatgpt.response |
    |------------------------------|
    |                     negative |
    |                     positive |
    |                     negative |
    +------------------------------+

Respond to Negative reviews using ChatGPT
-----------------------------------------

Let's next respond to negative food reviews using another EvaQL query that first retrieves the reviews with ``negative`` sentiment, and processes those reviews with another ChatGPT function call that generates a response to address the concerns shared in the review.

.. code-block:: sql

    SELECT ChatGPT(
            "Respond the the review with solution to address the review's concern",
            review)
    FROM postgres_data.review_table
    WHERE ChatGPT(
        "Is the review positive or negative. Only reply 'positive' or 'negative'. Here are examples. The food is very bad: negative. The food is very good: positive.",
        review) = "negative";

While running this query, EvaDB first retrieves the negative reviews and then applies ChatGPT to derive a response. Here is the query's output ``DataFrame``:

.. code-block:: 

    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                                                                                                                                                                                                                             chatgpt.response |
    |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Dear valued customer, Thank you for bringing this matter to our attention. We apologize for the inconvenience caused by the excessive saltiness of your fried rice. We understand how important it is to have a satisfying dining experience, and we would like to make it right for you ... |
    | Dear [Customer's Name], Thank you for bringing this issue to our attention. We apologize for the inconvenience caused by the missing chicken sandwich in your takeout order. We understand how frustrating it can be when an item is missing from your meal. To address this concern, we ... |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. include:: ../shared/nlp.rst

.. include:: ../shared/footer.rst
<<<<<<< HEAD
=======
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/nlp.rst

<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/footer.rst

.. include:: ../shared/designs/design3.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`__ for working example.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
.. include:: ../shared/nlp.rst

.. include:: ../shared/footer.rst
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
.. include:: ../shared/nlp.rst

.. include:: ../shared/footer.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`__ for working example.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
.. include:: ../shared/nlp.rst

.. include:: ../shared/footer.rst
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======

.. include:: ../shared/designs/design2.rst
>>>>>>> 08db5ebb (docs: updated images)
<<<<<<< HEAD
>>>>>>> e867f37e (docs: updated images)
=======
=======
.. include:: ../shared/designs/design3.rst
>>>>>>> ad7bb302 (docs: updates)
<<<<<<< HEAD
>>>>>>> 572f347e (docs: updates)
=======
=======
.. include:: ../shared/designs/design3.rst
=======
Check out our `Jupyter Notebook <https://github.com/georgia-tech-db/evadb/blob/staging/tutorials/14-food-review-tone-analysis-and-response.ipynb>`__ for working example.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
