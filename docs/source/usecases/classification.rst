.. _homerental-predict:

Prediction
==========

.. raw:: html

    <embed>
    <table align="left">
    <td>
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c317ee2f (updates)
>>>>>>> georgia-tech-db-main
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
=======
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run on Google Colab</a>
<<<<<<< HEAD
=======
        <a target="_blank" href="https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" width="24px" /> Run on Google Colab</a>
>>>>>>> fbfc3ace (docs: updates)
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" width="24px" /> View source on GitHub</a>
    </td>
    <td>
<<<<<<< HEAD
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 591a8656 (updates)
=======
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" width="24px" /> Download notebook</a>
>>>>>>> fbfc3ace (docs: updates)
=======
>>>>>>> georgia-tech-db-main
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a>
    </td>
    <td>
        <a target="_blank" href="https://github.com/georgia-tech-db/eva/raw/staging/tutorials/17-home-rental-prediction.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" /> Download notebook</a>
>>>>>>> 591a8656 (updates)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> c317ee2f (updates)
>>>>>>> georgia-tech-db-main
    </td>
    </table><br><br>
    </embed>

Introduction
------------

In this tutorial, we present how to to create and train a machine learning model for predicting the rental price of a home using the built-in :ref:`Prediction AI Engines<ludwig>` in EvaDB. EvaDB makes it easy to do prediction queries over data in your database using its built-in ``Prediction`` engines.

.. include:: ../shared/evadb.rst

.. include:: ../shared/postgresql.rst

We will assume that the input data is loaded into a ``PostgreSQL`` database. 
To load the home rental data into your database, see the complete `home rental prediction notebook on Colab <https://colab.research.google.com/github/georgia-tech-db/eva/blob/staging/tutorials/17-home-rental-prediction.ipynb>`_.

Preview the Home Rental Price Data
----------------------------------

The ``home_rentals`` table contains eight columns: ``number_of_rooms``, ``number_of_bathrooms``, ``sqft``, ``location``, ``days_on_market``, ``initial_price``, ``neighborhood``, and ``rental_price``.

.. code-block:: sql

   SELECT * FROM postgres_data.home_rentals LIMIT 3;

This query presents a subset of data in the ``home_rentals`` table:

.. code-block:: 

    +------------------------------+----------------------------------+-------------------+-----------------------+-----------------------------+----------------------------+---------------------------+---------------------------+
    | home_rentals.number_of_rooms | home_rentals.number_of_bathrooms | home_rentals.sqft | home_rentals.location | home_rentals.days_on_market | home_rentals.initial_price | home_rentals.neighborhood | home_rentals.rental_price |
    |------------------------------|----------------------------------|-------------------|-----------------------|-----------------------------|----------------------------|---------------------------|---------------------------|
    |                            1 |                                1 |               674 |                  good |                           1 |                       2167 |                  downtown |                      2167 |
    |                            1 |                                1 |               554 |                  poor |                          19 |                       1883 |                  westbrae |                      1883 |
    |                            0 |                                1 |               529 |                 great |                           3 |                       2431 |                south_side |                      2431 | 
    +------------------------------+----------------------------------+-------------------+-----------------------+-----------------------------+----------------------------+---------------------------+---------------------------+

Train a Home Rental Price Prediction Model
------------------------------------------

Let's next train a prediction model over the ``home_rental`` table using EvaDB's ``CREATE FUNCTION`` statement. We will use the built-in :ref:`Ludwig<ludwig>` engine for this task.

.. code-block:: sql
  
  CREATE OR REPLACE FUNCTION PredictHouseRent FROM
  ( SELECT * FROM postgres_data.home_rental )
  TYPE Ludwig
  PREDICT 'rental_price'
  TIME_LIMIT 3600;

In the above query, we use all the columns (except ``rental_price``) from ``home_rental`` table to predict the ``rental_price`` column.
We set the training time out to be ``3600`` seconds.

.. note::

<<<<<<< HEAD
<<<<<<< HEAD
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
=======
<<<<<<< HEAD
<<<<<<< HEAD
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
=======
   The :ref:`ludwig` page lists all the configurable paramters for the model training framework.
>>>>>>> 591a8656 (updates)
=======
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c317ee2f (updates)
=======
>>>>>>> fb00f6de (ran spellchecker)
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
=======
   The :ref:`ludwig` page lists all the configurable paramters for the model training framework.
>>>>>>> 591a8656 (updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
>>>>>>> 5b27053e (ran spellchecker)
=======
>>>>>>> c317ee2f (updates)
=======
=======
   The :ref:`ludwig` page lists all the configurable parameters for the model training framework.
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> fb00f6de (ran spellchecker)
>>>>>>> georgia-tech-db-main

This query returns the trained model:

.. code-block:: 

   +----------------------------------------------+
   | Function PredictHouseRent successfully added |
   +----------------------------------------------+

Predict using the Trained Model
-------------------------------

Next we use the trained ``PredictHouseRent`` to predict the home rental price.

.. code-block:: sql

   SELECT PredictHouseRent(*) 
   FROM postgres_data.home_rentals 
   LIMIT 3;

We use ``*`` to pass all the columns in the table as input into the ``PredictHouseRent`` function.

.. code-block::

   +-------------------------------------------+
   | predicthouserent.rental_price_predictions |
   +-------------------------------------------+
   |                               2087.763672 |
   |                               1793.570190 |
   |                               2346.319824 |
   +-------------------------------------------+

We next do a ``LATERAL JOIN`` to compare the actual rental prices in the ``home_rentals`` dataset against the predicted rental prices generated by the trained model, ``PredictHouseRent``.

.. code-block:: sql

   SELECT rental_price, predicted_rental_price
   FROM postgres_data.home_rentals
   JOIN LATERAL PredictHouseRent(*) AS Predicted(predicted_rental_price)
   LIMIT 3;

Here is the query's output:

.. code-block::

   +---------------------------+----------------------------------+
   | home_rentals.rental_price | Predicted.predicted_rental_price |
   +---------------------------+----------------------------------+
   |                      2167 |                      2087.763672 |
   |                      1883 |                      1793.570190 |
   |                      2431 |                      2346.319824 |
   +------------------ --------+----------------------------------+
      
.. include:: ../shared/footer.rst
<<<<<<< HEAD
<<<<<<< HEAD

.. include:: ../shared/designs/design10.rst
=======
<<<<<<< HEAD
<<<<<<< HEAD

.. include:: ../shared/designs/design10.rst
=======
>>>>>>> 591a8656 (updates)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c317ee2f (updates)
=======
>>>>>>> 5678c9a3 (docs: updated images)

.. include:: ../shared/designs/design10.rst
=======
>>>>>>> 591a8656 (updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5678c9a3 (docs: updated images)
>>>>>>> georgia-tech-db-main
=======

.. include:: ../shared/designs/design10.rst
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c317ee2f (updates)
=======
>>>>>>> 5678c9a3 (docs: updated images)
>>>>>>> georgia-tech-db-main
