.. _sklearn:

Model Training with Sklearn
============================

1. Installation
---------------

To use the `Sklearn framework <https://scikit-learn.org/stable/>`_, we need to install the extra sklearn dependency in your EvaDB virtual environment.

.. code-block:: bash
   
   pip install evadb[sklearn]

2. Example Query
----------------

.. code-block:: sql

   CREATE OR REPLACE FUNCTION PredictHouseRent FROM
   ( SELECT number_of_rooms, number_of_bathrooms, days_on_market, rental_price FROM HomeRentals )
   TYPE Sklearn
   PREDICT 'rental_price';

In the above query, you are creating a new customized function by training a model from the ``HomeRentals`` table using the ``Sklearn`` framework.
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
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> fb00f6de (ran spellchecker)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
The ``rental_price`` column will be the target column for predication, while the rest columns from the ``SELECT`` query are the inputs. 
=======
The ``rental_price`` column will be the target column for predication, while the rest columns from the ``SELET`` query are the inputs. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
The ``rental_price`` column will be the target column for predication, while the rest columns from the ``SELECT`` query are the inputs. 
>>>>>>> 5b27053e (ran spellchecker)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
The ``rental_price`` column will be the target column for predication, while the rest columns from the ``SELECT`` query are the inputs. 
>>>>>>> 5b27053e (ran spellchecker)
>>>>>>> fb00f6de (ran spellchecker)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
