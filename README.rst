.. SPDX-FileCopyrightText: 2023 Veit Schiele

.. SPDX-License-Identifier: BSD-3-Clause

===============================
cusy.tasks – a simple todo list
===============================

*cusy.tasks* is a simple command line tool for managing tasks. It allows you to
create, display, update and delete tasks, as well as change their status.

Status
======

.. image:: https://img.shields.io/github/contributors/cusyio/cusy.tasks.svg
   :alt: Contributors
   :target: https://github.com/cusyio/cusy.tasks/graphs/contributors
.. image:: https://img.shields.io/github/license/cusyio/cusy.tasks.svg
   :alt: License
   :target: https://github.com/cusyio/cusy.tasks/blob/main/LICENSE
.. image:: https://github.com/cusyio/cusy.tasks/workflows/CI/badge.svg
   :target: https://github.com/cusyio/cusy.tasks/actions?workflow=CI
   :alt: CI Status

Features
========

* Create tasks with summary and owner
* Display tasks, optionally filtered by owner or status
* Update tasks and their status (todo, in progress, done)
* Delete individual or all tasks
* Simple command line interface
* Programmable Python API

Installation
============

#. Download and unpack:

   … on Linux/macOS:

   .. code-block:: console

      $ curl -O https://codeload.github.com/cusyio/cusy.tasks/zip/main
      $ unzip main
      Archive:  main
      …
         creating: cusy.tasks-main/
      …

   … on Windows:

   .. code-block:: ps1con

      C:> curl.exe -o main.zip -O https://codeload.github.com/cusyio/cusy.tasks/zip/main
      C:> tar -xvzf main.zip
      cusy.tasks-main/
      cusy.tasks-main/.gitignore
      …

#. Install Python packages:

   … on Linux/macOS:

   .. code-block:: console

      $ cd cusy.tasks
      $ python3 -m venv .
      $ . bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install -e .

   … on Windows:

   .. code-block:: ps1con

      C:> py -m venv .
      C:> Scripts\activate
      C:> python -m pip install --upgrade pip
      C:> python -m pip install -e .

Usage
=====

Command line instructions
-------------------------

After activating the virtual Python environment, you can use cusy.tasks on the
command line:

.. code-block:: console

   # Display all tasks (default if no command is specified)
   $ cusy.tasks

   # Add a new task
   $ cusy.tasks add "My task description" --owner "Veit"

   # Show filtered list
   $ cusy.tasks list --owner "Veit" --state "todo"

   # Update task
   $ cusy.tasks update 1 --owner "Veit" --summary "Update description"

   # Change the status of a task
   $ cusy.tasks start 1    # Set status to "in progress"
   $ cusy.tasks finish 1   # Set status to "done"

   # Delete task
   $ cusy.tasks delete 1

   # Display number of tasks
   $ cusy.tasks count

   # Display the file path of the database
   $ cusy.tasks config

   # Display version
   $ cusy.tasks version

Python API
----------

You can also use the cusy.tasks functionality directly in your Python code:

.. code-block:: python

   # Initialise database
   from cusy.tasks import TasksDB, Task

   # Connect to database
   db = TasksDB("/path/to/database")

   # Add new task
   task = Task(summary="Implement feature", owner="Veit")
   task_id = db.add_task(task)

   # Retrieve task by ID
   task = db.get_task(task_id)

   # Update task
   db.update_task(task_id, Task(summary="Implement feature with tests"))

   # Change status
   db.start(task_id)  # Set to "in progress"
   db.finish(task_id)  # Set to "done"

   #  List tasks (optionally with filtering)
   all_tasks = db.list_tasks()
   veit_tasks = db.list_tasks(owner="Veit")
   in_process = db.list_tasks(state="in progress")

   #  Delete task
   db.delete_task(task_id)

   # Close connection
   db.close()

Configuration
=============

The database file is saved under ``~/tasks_db`` by default. You can change this
path by setting the environment variable ``ITEMS_DB_DIR``:

.. code-block:: console

   # Linux/macOS
   $ export ITEMS_DB_DIR=/pfad/zu/meiner/datenbank

   # Windows
   C:> set ITEMS_DB_DIR=C:\pfad\zu\meiner\datenbank

Project links
=============

* `Documentation <https://tasks.cusy.io>`_
* `GitHub <https://github.com/cusyio/cusy.tasks>`_
* `Mastodon <https://mastodon.social/deck/@Python4DataScience>`_

Collaboration
=============

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/cusyio/cusy.tasks/fork>`_ of my
`GitHub Repository <https://github.com/cusyio/cusy.tasks/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, I’ll be happy to look at your
suggestions.

License
=======

This project is licensed under the BSD-3-Clause licence. Further information can
be found in the ``LICENSE`` file in the project repository.
