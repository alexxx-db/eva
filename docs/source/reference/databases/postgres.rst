<<<<<<< HEAD
.. _postgresql:

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
PostgreSQL
==========

The connection to PostgreSQL is based on the `psycopg2 <https://pypi.org/project/psycopg2/>`_ library.

Dependency
----------

* psycopg2


Parameters
----------

Required:

* `user` is the database user.
* `password` is the database password.
* `host` is the host name, IP address, or URL.
* `port` is the port used to make TCP/IP connection.
* `database` is the database name.

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
.. warning:: 
         
     Provide the parameters of an already running ``PostgreSQL`` server. EvaDB only connects to an existing ``PostgreSQL`` database.
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
.. warning:: 
         
     Provide the parameters of an already running ``PostgreSQL`` server. EvaDB only connects to an existing ``PostgreSQL`` database.
>>>>>>> a9ef5071 (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

Create Connection
-----------------

.. code-block:: text

   CREATE DATABASE postgres_data WITH ENGINE = 'postgres', PARAMETERS = {
        "user": "eva", 
        "password": "password",
        "host": "localhost",
        "port": "5432", 
        "database": "evadb"
   };

