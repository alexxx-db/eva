.. _release_steps:


Release Steps
=============

Update Version 
~~~~~~~~~~~~~~~

Update the new version number in ``evadb/version.py``.


Update ``master`` with ``staging``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply point ``master`` head to the latest commit of ``staging``.

.. code-block:: bash

    git checkout master
    git reset --hard <latest commit of staging>
    git push -f origin master


Setup Credentials
~~~~~~~~~~~~~~~~~~

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
Please check :ref:`setup_pypi_account` about how to setup PyPI account.
=======
Please check :ref:`setup_pypi_account` about how to setup PyPi account.
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
Please check :ref:`setup_pypi_account` about how to setup PyPI account.
>>>>>>> 5b27053e (ran spellchecker)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)

Setup Github token. You can obtain a personal token from Github.

.. code-block:: bash

    export GITHUB_KEY="..."

Build Wheel and Release
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
    python script/releasing/releaser.py -n minor -u
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
    python script/releasing/releaser.py -n minor -u
=======
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
    python script/releasing/releaser.py -n minor -u
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
       git tag -a v0.0.6 -m "v0.0.6 release"
       git push origin v0.0.6

8. Build the source and wheel distributions:

.. code-block:: bash

       rm -rf dist build  # clean old builds & distributions
       python3 setup.py sdist  # create a source distribution
       python3 setup.py bdist_wheel  # create a universal wheel

9. Check that everything looks correct by installing the wheel locally and checking the version:

.. code-block:: python

       python3 -m venv test_evadb  # create a virtualenv for testing
       source test_evadb/bin/activate  # activate virtualenv
       python3 -m pip install dist/evadb-0.9.1-py3-none-any.whl
       python3 -c "import evadb; print(evadb.__version__)"

10. Publish to PyPI

.. code-block:: python

       pip install twine  # if not installed
       twine upload dist/* -r pypi

11. A PR is automatically submitted (this will take a few hours) on [`conda-forge/eva-feedstock`] to update the version.
    * A maintainer needs to accept and merge those changes.

12. Create a new release on Github.
    * Input the recently-created Tag Version: ``v0.0.6``
    * Copy the release notes in ``CHANGELOG.md`` to the GitHub tag.
    * Attach the resulting binaries in (``dist/evadb-x.x.x.*``) to the release.
    * Publish the release.

13. Update version to, e.g. ``0.9.1+dev`` in ``evadb/version.py``.

14. Add a new changelog entry for the unreleased version in `CHANGELOG.md`:

.. code-block:: python

       ##  [Unreleased]
       ### [Breaking Changes]
       ### [Added]
       ### [Changed]
       ### [Deprecated]
       ### [Removed]

15. Commit these changes and create a PR:

.. code-block:: bash

       git checkout -b bump-v0.9.1+dev
       git add . -u
       git commit -m "[BUMP]: v0.9.1+dev"
       git push --set-upstream origin bump-v0.9.1+dev
       
16. Add the new tag to `the EvaDB project on ReadTheDocs <https://readthedocs.org/projects/evadb>`_,

    * Trigger a build for main to pull new tags.
    * Go to the ``Versions`` tab, and ``Activate`` the new tag.
    * Go to Admin/Advanced to set this tag as the new default version.
    * In ``Overview``, make sure a build is triggered:
        * For the tag ``v0.9.1``
        * For ``latest``

Credits: `Snorkel <https://github.com/snorkel-team/snorkel/blob/main/RELEASING.md>`_
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
    python script/releasing/releaser.py -n minor -u
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
