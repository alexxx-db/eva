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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
.. code-block:: text
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. code-block::
=======
=======
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
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
.. code-block::
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 63510989 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
.. code-block:: text
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
.. code-block::
>>>>>>> aeb9a3be (Remove dimensions from `TEXT` and `FLOAT` (#1261))
<<<<<<< HEAD
>>>>>>> 63510989 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
=======
=======
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
.. code-block::
=======
>>>>>>> georgia-tech-db-main
>>>>>>> 63510989 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
.. code-block:: text
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
.. code-block::
=======
.. code-block:: text
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
.. code-block::
>>>>>>> aeb9a3be (Remove dimensions from `TEXT` and `FLOAT` (#1261))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 63510989 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
>>>>>>> eva-source
=======
>>>>>>> 63510989 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
<<<<<<< HEAD
>>>>>>> 25352b39 (Remove dimensions from `TEXT` and `FLOAT` (#1261))
=======
=======
>>>>>>> georgia-tech-db-main
=======
.. code-block::
=======
.. code-block:: text
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

    CREATE DATABASE postgres_data 
    WITH ENGINE = 'postgres', 
    PARAMETERS = {
        "user": "eva",
        "password": "password",
        "host": "localhost",
        "port": "5432",
        "database": "evadb"
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
We will assume that you have a ``PostgreSQL`` database server running locally that contains the data needed for analysis. Follow these instructions to install `PostgreSQL <https://www.postgresql.org/download/>`_.

EvaDB lets you connect to your favorite databases, data warehouses, data lakes, etc., via the ``CREATE DATABASE`` statement. In this query, we connect EvaDB to an existing ``PostgreSQL`` server:

.. code-block:: text

<<<<<<< HEAD
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
.. tab-set::
    
    .. tab-item:: Python

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
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
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
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
=======
.. tab-set::
    
    .. tab-item:: Python

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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
.. tab-set::
    
    .. tab-item:: Python

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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
