MariaDB
==========

The connection to MariaDB is based on the `mariadb <https://mariadb-corporation.github.io/mariadb-connector-python/>`_ library.

Dependency
----------

* mariadb


Parameters
----------

Required:

* `user` is the username corresponding to the database
* `password` is the password for the above username for the database
* `database` is the database name
* `host` is the host name, IP address or the URL
* `port` is the port used to make the TCP/IP connection.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9ef5071 (docs: updates)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
.. warning:: 
         
     Provide the parameters of an already running ``MariaDB`` server. EvaDB only connects to an existing ``MariaDB`` database.

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> a9ef5071 (docs: updates)
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)

Create Connection
-----------------

.. code-block:: text

   CREATE DATABASE mariadb_data WITH ENGINE = 'mariadb', PARAMETERS = {
        "user" : "eva",
        "password": "password",
        "host": "127.0.0.1".
        "port": "7567",
        "database": "evadb"
   };

