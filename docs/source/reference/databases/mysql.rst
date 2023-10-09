MySQL
==========

The connection to MySQL is based on the `mysql-connector-python <https://pypi.org/project/mysql-connector-python/>`_ library.

Dependency
----------

* mysql-connector-python

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> a9ef5071 (docs: updates)
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
.. warning:: 

     Provide the parameters of an already running ``MySQL`` server. EvaDB only connects to an existing ``MySQL`` database.
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
.. warning:: 

     Provide the parameters of an already running ``MySQL`` server. EvaDB only connects to an existing ``MySQL`` database.
>>>>>>> a9ef5071 (docs: updates)

Create Connection
-----------------

.. code-block:: text

   CREATE DATABASE mysql_data WITH ENGINE = 'mysql', PARAMETERS = {
        "user": "eva", 
        "password": "password",
        "host": "localhost",
        "port": "5432", 
        "database": "evadb"
   };

