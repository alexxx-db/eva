Connect EvaDB to PostgreSQL Database Server
-------------------------------------------

We will assume that you have a ``PostgreSQL`` database server running locally that contains the data needed for analysis. Follow these instructions to install `PostgreSQL <https://www.postgresql.org/download/>`_.

EvaDB lets you connect to your favorite databases, data warehouses, data lakes, etc., via the ``CREATE DATABASE`` statement. In this query, we connect EvaDB to an existing ``PostgreSQL`` server:

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. code-block::
=======
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
.. code-block::
=======
.. code-block:: text
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)

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
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
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
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
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
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
