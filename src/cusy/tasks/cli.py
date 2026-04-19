# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""The module provides a command-line interface for managing tasks.

You can run the commands using the ``tasks`` command followed by
the specific subcommand:

.. code-block:: console

    cusy.tasks add "My task description" --owner "Veit"
    cusy.tasks list
    cusy.tasks list --owner "Veit" --state "todo"
    cusy.tasks update 1 --owner "Veit" --summary "Update description"
    cusy.tasks start 1
    cusy.tasks finish 1
    cusy.tasks delete 1
    cusy.tasks count
    cusy.tasks config
    cusy.tasks version

If no subcommand is specified, the ``list`` command is executed by default.
"""

import os
import pathlib

from contextlib import contextmanager
from io import StringIO

import rich
import typer

from rich.table import Table

from cusy import tasks


app = typer.Typer(add_completion=False)


@app.command()
def version():
    """Return the version of the tasks application.

    Returns:
        str: The version string of the tasks package.

    """
    print(tasks.__version__)


@app.command()
def add(summary: list[str], owner: str = typer.Option(None, "-o", "--owner")):
    """Add a task to the database.

    Args:
        summary (list[str]): The summary of the new task.
        owner (str, optional): The owner of the new task. Defaults to None.

    """
    summary = " ".join(summary) if summary else None
    with tasks_db() as db:
        db.add_task(tasks.Task(summary, owner, state="todo"))


@app.command()
def delete(task_id: int):
    """Remove a task from the database.

    Args:
        task_id (int): The ID of the task to delete.

    Raises:
        InvalidTaskIdError: If no task with the given ID exists.

    """
    with tasks_db() as db:
        try:
            db.delete_task(task_id)
        except tasks.InvalidTaskIdError:
            print(f"Error: Invalid task id {task_id}")


@app.command("list")
def list_tasks(
    owner: str = typer.Option(None, "-o", "--owner"),
    state: str = typer.Option(None, "-s", "--state"),
):
    """List tasks in the database, optionally filtered by owner and/or state.

    Args:
        owner (str, optional): Filter tasks by this owner. Defaults to None.
        state (str, optional): Filter tasks by this state. Defaults to None.

    """
    with tasks_db() as db:
        the_tasks = db.list_tasks(owner=owner, state=state)
        table = Table(box=rich.box.SIMPLE)
        table.add_column("ID")
        table.add_column("state")
        table.add_column("owner")
        table.add_column("summary")
        for t in the_tasks:
            owner = "" if t.owner is None else t.owner
            table.add_row(str(t.id), t.state, owner, t.summary)
        out = StringIO()
        rich.print(table, file=out)
        print(out.getvalue())


@app.command()
def update(
    task_id: int,
    owner: str = typer.Option(None, "-o", "--owner"),
    summary: list[str] = typer.Option(None, "-s", "--summary"),
):
    """Update a task in the database.

    Args:
        task_id (int): The ID of the task to update.
        owner (str, optional): The new owner of the task. Defaults to None.
        summary (list[str], optional): The new summary of the task. Defaults to
            None.

    Raises:
        InvalidTaskIdError: If no task with the given ID exists.

    """
    summary = " ".join(summary) if summary else None
    with tasks_db() as db:
        try:
            db.update_task(task_id, tasks.Task(summary, owner, state=None))
        except tasks.InvalidTaskIdError:
            print(f"Error: Invalid task id {task_id}.")


@app.command()
def start(task_id: int):
    """Set a task's state to 'in progress'.

    Args:
        task_id (int): The ID of the task to update.

    Raises:
        InvalidTaskIdError: If no task with the given ID exists.

    """
    with tasks_db() as db:
        try:
            db.start(task_id)
        except tasks.InvalidTaskIdError:
            print(f"Error: Invalid task id {task_id}.")


@app.command()
def finish(task_id: int):
    """Set a task's state to 'done'.

    Args:
        task_id (int): The ID of the task to update.

    Raises:
        InvalidTaskIdError: If no task with the given ID exists.

    """
    with tasks_db() as db:
        try:
            db.finish(task_id)
        except tasks.InvalidTaskIdError:
            print(f"Error: Invalid task id {task_id}.")


@app.command()
def config():
    """Return the path to the Tasks database.

    Returns:
        str: Path to the Tasks database.

    """
    with tasks_db() as db:
        print(db.path())


@app.command()
def count():
    """Return the number of tasks in the database.

    Returns:
        int: Number of tasks in the database.

    """
    with tasks_db() as db:
        print(db.count())


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Tasks is a small command line task tracking application."""
    if ctx.invoked_subcommand is None:
        list_tasks(owner=None, state=None)


def get_path():
    """Determine the path to the database.

    The path is determined from the environment variable ITEMS_DB_DIR.
    If it is not defined, $HOME/tasks_db is used.

    Returns:
        pathlib.Path: Path to the database directory.

    """
    db_path_env = os.getenv("ITEMS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "tasks_db"
    return db_path


@contextmanager
def tasks_db():
    """Open and close the database connection.

    Yields:
        TasksDB: A TasksDB instance connected to the database.

    """
    db_path = get_path()
    db = tasks.TasksDB(db_path)
    yield db
    db.close()
