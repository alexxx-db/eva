.. _python-api:

<<<<<<< HEAD
Python API
=======
Basic API
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
==========

To begin a querying session in EvaDB, obtain a connection with a cursor using ``connect`` and ``cursor`` functions. After getting the cursor, you can run queries with the ``query`` function in this manner:

.. code-block:: python

    # Import the EvaDB package
    import evadb

    # Connect to EvaDB and get a database cursor for running queries
    cursor = evadb.connect().cursor()

    # List all the built-in functions in EvaDB
    print(cursor.query("SHOW UDFS;").df())


.. autosummary:: 
    :toctree: ./doc
    
    ~evadb.connect
    ~evadb.EvaDBConnection.cursor
    ~evadb.EvaDBCursor.query
    ~evadb.EvaDBCursor.df

.. warning::

    It is important to call ``df`` to run the actual query and get the output dataframe.

    ``cursor.query("...")`` only construct the query and not run the query. ``cursor.query("...").df()`` will both construct and run the query.

<<<<<<< HEAD
=======
EvaDBCursor Interface
---------------------

Using the cursor, you can refer to a table, load documents, create functions, create vector index, and several other tasks.

After connecting to a table using ``table``, you can construct a complex query using the ``EvaDBQuery`` interface.

.. autosummary::
    :toctree: ./doc

    ~evadb.EvaDBCursor.table
    ~evadb.EvaDBCursor.load
    ~evadb.EvaDBCursor.query
    ~evadb.EvaDBCursor.create_function
    ~evadb.EvaDBCursor.create_table
    ~evadb.EvaDBCursor.create_vector_index
    ~evadb.EvaDBCursor.drop_table
    ~evadb.EvaDBCursor.drop_function
    ~evadb.EvaDBCursor.drop_index
    ~evadb.EvaDBCursor.df
    ~evadb.EvaDBCursor.show
    ~evadb.EvaDBCursor.insert
    ~evadb.EvaDBCursor.explain
    ~evadb.EvaDBCursor.rename

EvaDBQuery Interface
---------------------

.. autosummary::
    :toctree: ./doc

    ~evadb.EvaDBQuery.select
    ~evadb.EvaDBQuery.cross_apply
    ~evadb.EvaDBQuery.filter
    ~evadb.EvaDBQuery.df
    ~evadb.EvaDBQuery.alias
    ~evadb.EvaDBQuery.limit
    ~evadb.EvaDBQuery.order
    ~evadb.EvaDBQuery.show
    ~evadb.EvaDBQuery.sql_query
    ~evadb.EvaDBQuery.execute
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
