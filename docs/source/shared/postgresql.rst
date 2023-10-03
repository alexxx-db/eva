Connect EvaDB to PostgreSQL Database Server
-------------------------------------------

<<<<<<< HEAD
We will assume that you have a :ref:`PostgreSQL<postgresql>` database running locally that contains the data needed for analysis. Follow these instructions to install `PostgreSQL <https://www.postgresql.org/download/>`_. 

.. note::
    If find it challenging to install the ``PostgreSQL`` database on your machine, here is an alternative for quick prototyping. 
    
    You can use an embedded :ref:`SQLite<sqlite>` database. If you go with the ``sqlite`` database, alter the SQL commands in this tutorial to use the ``sqlite`` engine and the ``evadb.db`` SQLite database file as explained in the :ref:`SQLite<sqlite>` page.

EvaDB lets you connect to your favorite databases, data warehouses, data lakes, etc., via the ``CREATE DATABASE`` statement. In this query, we connect EvaDB to an existing ``PostgreSQL`` server:

<<<<<<< HEAD
<<<<<<< HEAD
.. code-block::
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
.. code-block:: text
>>>>>>> 53dafecf (feat: sync master staging (#1050))

    CREATE DATABASE postgres_data 
    WITH ENGINE = 'postgres', 
    PARAMETERS = {
        "user": "eva",
        "password": "password",
        "host": "localhost",
        "port": "5432",
        "database": "evadb"
    }
=======
<<<<<<< HEAD
We will assume that you have a ``PostgreSQL`` database server running locally that contains the data needed for analysis. Follow these instructions to install `PostgreSQL <https://www.postgresql.org/download/>`_.

EvaDB lets you connect to your favorite databases, data warehouses, data lakes, etc., via the ``CREATE DATABASE`` statement. In this query, we connect EvaDB to an existing ``PostgreSQL`` server:

.. code-block:: text

<<<<<<< HEAD
=======
.. tab-set::
    
    .. tab-item:: Python

>>>>>>> 53dafecf (feat: sync master staging (#1050))
        .. code-block:: python

            params = {
                "user": "eva",
                "password": "password",
                "host": "localhost",
                "port": "5432",
                "database": "evadb",
            }
            query = f"CREATE DATABASE postgres_data 
                      WITH ENGINE = 'postgres', 
                      PARAMETERS = {params};"
            cursor.query(query).df()

    .. tab-item:: SQL 

        .. code-block:: text

            CREATE DATABASE postgres_data 
            WITH ENGINE = 'postgres', 
            PARAMETERS = {
                "user": "eva",
                "password": "password",
                "host": "localhost",
                "port": "5432",
                "database": "evadb"
            }
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
.. code-block:: text

>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    CREATE DATABASE postgres_data 
    WITH ENGINE = 'postgres', 
    PARAMETERS = {
        "user": "eva",
        "password": "password",
        "host": "localhost",
        "port": "5432",
        "database": "evadb"
    }
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
