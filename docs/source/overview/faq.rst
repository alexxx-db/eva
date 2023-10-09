<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 32e513d7 (docs: updates)
Frequently Asked Questions
==========================
=======
:orphan:

===
FAQ
===
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

.. _faq:

Here are some frequently asked questions that we have seen pop up for EvaDB.

<<<<<<< HEAD
.. note::

=======
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
Frequently Asked Questions
==========================
=======
:orphan:

===
FAQ
===
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
Frequently Asked Questions
==========================
>>>>>>> 32e513d7 (docs: updates)

.. _faq:

Here are some frequently asked questions that we have seen pop up for EvaDB.

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 32e513d7 (docs: updates)
.. note::

>>>>>>> 35b99c88 (docs: updates)
    Have another question or want to give feedback? Ask us on `Slack <https://evadb.ai/community>`__!

Why am I not able to install EvaDB?
-----------------------------------

Ensure that the Python interpreter's version is >= `3.9`. 

.. note::

    If you are using the `evadb[ray]` installation option, ensure that the Python  version is <= `3.10` due to a `Ray issue <https://github.com/autogluon/autogluon/issues/2687>`_. Follow `these instructions <https://github.com/ray-project/ray/issues/33039>`_ to install `ray`.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 32e513d7 (docs: updates)
=======
Why am I not able to install EvaDB in my Python environment?
============================================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 35b99c88 (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> 32e513d7 (docs: updates)


Where does EvaDB store all the data?
------------------------------------

By default, EvaDB connects to **existing** data sources like SQL database systems. It stores all the meta-data (i.e., data about data sources) in a local folder named ``evadb_data``. Deleting this folder will reset EvaDB's state and lead to data loss.

Why do I see no output from the server?
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 32e513d7 (docs: updates)
---------------------------------------
=======
=======================================
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
---------------------------------------
>>>>>>> 35b99c88 (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
---------------------------------------
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> 32e513d7 (docs: updates)

If a query runs a complex AI task (e.g., sentiment analysis) on a large table, the query is expected to take a non-trivial amount of time to finish. You can check the status of the server by running ``top`` or ``pgrep``:

.. code-block:: bash

    top
    pgrep evadb_server

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 32e513d7 (docs: updates)
=======
pip install ray fails because of grpcio
=======================================

Follow these instructions to install ``ray``:
https://github.com/ray-project/ray/issues/33039
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 35b99c88 (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 35b99c88 (docs: updates)
>>>>>>> 32e513d7 (docs: updates)
