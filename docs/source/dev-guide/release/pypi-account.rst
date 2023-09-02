.. _setup_pypi_account:

Setup PyPI Account
==================

Make sure you have `PyPI <https://pypi.org>`_ account with maintainer access to the EvaDB project. 
Create a .pypirc in your home directory. It should look like this:

.. code-block:: python

    [distutils]
    index-servers =
    pypi
    pypitest
    
    [pypi]
    username=YOUR_USERNAME
    password=YOUR_PASSWORD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
Then run ``chmod 600 ~/.pypirc`` so that only you can read/write the file.
=======
Then run ``chmod 600 ./.pypirc`` so that only you can read/write the file.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
Then run ``chmod 600 ~/.pypirc`` so that only you can read/write the file.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
Then run ``chmod 600 ~/.pypirc`` so that only you can read/write the file.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
Then run ``chmod 600 ./.pypirc`` so that only you can read/write the file.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
>>>>>>> f028c383 (release: merge staging into master (#1032))
