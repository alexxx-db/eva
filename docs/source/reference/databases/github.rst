Github
==========

The connection to Github is based on the `PyGithub <https://github.com/PyGithub/PyGithub>`_ library.

Dependency
----------

* PyGithub


Parameters
----------

Required:

* ``owner`` is the owner of the Github repository. For example, georgia-tech-db is the owner of the EvaDB repository.
* ``repo`` is the name of the Github repository. For example, evadb is the name of this repository.

Optional:

<<<<<<< HEAD
<<<<<<< HEAD
* ``github_token`` is not required for public repositories. However, the rate limit is lower without a valid github_token. Check the `Rate limits page <https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api?apiVersion=2022-11-28>`_ to learn more about how to check your rate limit status. Check `Managing your personal access tokens page <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_ to learn how to create personal access tokens.
=======
* ``github_token`` is not required for public repositories. However, the rate limit is lower without a valid github_token. Check `Rate limits page <https://docs.github.com/en/rest/overview/resources-in-the-rest-api?apiVersion=2022-11-28#rate-limits>`_ to learn more about how to check your rate limit status. Check `Managing your personal access tokens page <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_ to learn how to create personal access tokens.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
* ``github_token`` is not required for public repositories. However, the rate limit is lower without a valid github_token. Check `Rate limits page <https://docs.github.com/en/rest/overview/resources-in-the-rest-api?apiVersion=2022-11-28#rate-limits>`_ to learn more about how to check your rate limit status. Check `Managing your personal access tokens page <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_ to learn how to create personal access tokens.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)

Create Connection
-----------------

.. code-block:: text

   CREATE DATABASE github_data WITH ENGINE = 'github', PARAMETERS = {
        "owner": "georgia-tech-db",
        "repo": "evadb"
   };

Supported Tables
----------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
* ``stargazers``: Lists the people that have starred the repository. Check `table_column_info.py <https://github.com/georgia-tech-db/evadb/blob/staging/evadb/third_party/databases/github/table_column_info.py>`_ for all the available columns in the table.
=======
* ``stargazers``: Lists the people that have starred the repository. Check `evadb/third_party/databases/github/table_column_info.py` for all the available columns in the table.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
* ``stargazers``: Lists the people that have starred the repository. Check `evadb/third_party/databases/github/table_column_info.py` for all the available columns in the table.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
* ``stargazers``: Lists the people that have starred the repository. Check `evadb/third_party/databases/github/table_column_info.py` for all the available columns in the table.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
* ``stargazers``: Lists the people that have starred the repository. Check `table_column_info.py <https://github.com/georgia-tech-db/evadb/blob/staging/evadb/third_party/databases/github/table_column_info.py>`_ for all the available columns in the table.
>>>>>>> 858b8c1c (Collection of fixes for the staging branch (#1253))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
* ``stargazers``: Lists the people that have starred the repository. Check `evadb/third_party/databases/github/table_column_info.py` for all the available columns in the table.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
* ``stargazers``: Lists the people that have starred the repository. Check `evadb/third_party/databases/github/table_column_info.py` for all the available columns in the table.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

.. code-block:: sql

   SELECT * FROM github_data.stargazers;

Here is the query output:

.. code-block:: 

    +---------------------------------------------------+-----+---------------------------------------------+
    |                             stargazers.avatar_url | ... |                              stargazers.url |
    |---------------------------------------------------|-----|---------------------------------------------|
    | https://avatars.githubusercontent.com/u/105357... | ... |      https://api.github.com/users/jaehobang |
    | https://avatars.githubusercontent.com/u/436141... | ... | https://api.github.com/users/VineethAljapur |
    |                                               ... | ... |                                         ... |
    +---------------------------------------------------+-----+---------------------------------------------+

.. note::

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
   Looking for another table from Github? You can add a table mapping in `github_handler.py <https://github.com/georgia-tech-db/evadb/blob/staging/evadb/third_party/databases/github/github_handler.py>`_, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
=======
   Looking for another table from Github? You can add a table mapping in `evadb/third_party/databases/github/github_handler.py`, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
   Looking for another table from Github? You can add a table mapping in `evadb/third_party/databases/github/github_handler.py`, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
   Looking for another table from Github? You can add a table mapping in `evadb/third_party/databases/github/github_handler.py`, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
   Looking for another table from Github? You can add a table mapping in `github_handler.py <https://github.com/georgia-tech-db/evadb/blob/staging/evadb/third_party/databases/github/github_handler.py>`_, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 858b8c1c (Collection of fixes for the staging branch (#1253))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
   Looking for another table from Github? You can add a table mapping in `evadb/third_party/databases/github/github_handler.py`, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
   Looking for another table from Github? You can add a table mapping in `evadb/third_party/databases/github/github_handler.py`, or simply raise a `Feature Request <https://github.com/georgia-tech-db/evadb/issues/new/choose>`_.
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
