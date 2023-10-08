.. _python-api:

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
Python API
=======
Basic API
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
Python API
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
Python API
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
==========

To begin a querying session in EvaDB, obtain a connection with a cursor using ``connect`` and ``cursor`` functions. After getting the cursor, you can run queries with the ``query`` function in this manner:

.. code-block:: python

    # Import the EvaDB package
    import evadb

    # Connect to EvaDB and get a database cursor for running queries
    cursor = evadb.connect().cursor()

    # List all the built-in functions in EvaDB
<<<<<<< HEAD
<<<<<<< HEAD
    print(cursor.query("SHOW FUNCTIONS;").df())
=======
    print(cursor.query("SHOW UDFS;").df())
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
    print(cursor.query("SHOW FUNCTIONS;").df())
>>>>>>> aed2d9cf (docs: updated outdated reference to SHOW UDF)


.. autosummary:: 
    :toctree: ./doc
    
    ~evadb.connect
    ~evadb.EvaDBConnection.cursor
    ~evadb.EvaDBCursor.query
<<<<<<< HEAD
    ~evadb.EvaDBQuery.df

.. warning::

    ``cursor.query("...").df()`` constructs and then runs the query to get the output dataframe.

    It is important to call ``df`` to run the actual query and get the output dataframe. ``cursor.query("...")`` only constructs the query. It does not execute the query.
    

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
.. include:: ../shared/designs/design4.rst
=======
=======
>>>>>>> e867f37e (docs: updated images)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> df4d8a35 (docs: updates)
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
=======
    ~evadb.EvaDBCursor.df

.. warning::

    It is important to call ``df`` to run the actual query and get the output dataframe.

    ``cursor.query("...")`` only construct the query and not run the query. ``cursor.query("...").df()`` will both construct and run the query.

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
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
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> eva-master
=======
.. include:: ../shared/design4.rst
>>>>>>> dc9069a2 (docs: updates)
<<<<<<< HEAD
>>>>>>> df4d8a35 (docs: updates)
=======
=======
.. include:: ../shared/designs/design4.rst
>>>>>>> 08db5ebb (docs: updated images)
>>>>>>> e867f37e (docs: updated images)
