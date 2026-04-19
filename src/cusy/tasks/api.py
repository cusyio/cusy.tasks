# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""The API for the tasks project.

This module provides classes and functions to interact with the tasks database
programmatically.
"""

from dataclasses import asdict, dataclass, field

from .db import DB


__all__ = [
    "InvalidItemIdError",
    "Item",
    "ItemsDB",
    "ItemsError",
    "MissingSummaryError",
]


@dataclass
class Item:
    """Defines the tasks type with the attributes summary, owner and state.

    Args:
        summary (str): Summary of a task. Defaults to None.
        owner (str): The person working on a task. Defaults to None.
        state (str): The status of a task. Defaults to 'todo'.
        id (int): The unique identifier for the task. Defaults to None.

    """

    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        """Return a task instance from a dict.

        Args:
            d (dict): Dictionary containing task attributes.

        Returns:
            Item: Item instance created from dictionary values.

        """
        return Item(**d)

    def to_dict(self):
        """Return a dict from a task instance.

        Returns:
            dict: Dictionary containing the task's attributes.

        """
        return asdict(self)


class ItemsError(Exception):
    """Base exception class for the tasks module.

    Parent class for MissingSummaryError and InvalidItemIdError exceptions.
    """


class MissingSummaryError(ItemsError):
    """Exception raised when a task is added without a summary.

    Raised when cusy.tasks.api.ItemsDB.add_task is called with a task that has
    no summary.
    """


class InvalidItemIdError(ItemsError):
    """Exception raised when an operation is performed with an invalid task ID.

    Raised when trying to access or modify a task that doesn't exist.
    """


class ItemsDB:
    """Database class to access the tasks_db file.

    Args:
        db_path (str or pathlib.Path): Path to the database file.

    """

    def __init__(self, db_path):
        """Initiate the database class."""
        self._db_path = db_path
        self._db = DB(db_path, ".tasks_db")

    def add_task(self, task: Item):
        """Add a task to the database.

        Args:
            task (Item): The Item instance to add to the database.

        Returns:
            int: The task id of the newly added task.

        Raises:
            MissingSummaryError: If the task has no summary.

        """
        if not task.summary:
            raise MissingSummaryError
        if task.owner is None:
            task.owner = ""
        task_id = self._db.create(task.to_dict())
        self._db.update(task_id, {"id": task_id})
        return task_id

    def get_task(self, task_id: int):
        """Return a task for the corresponding id.

        Args:
            task_id (int): ID of the task to retrieve.

        Returns:
            Item: Item instance from the database.

        Raises:
            InvalidItemIdError: If no task with the given ID exists.

        """
        db_task = self._db.read(task_id)
        if db_task is not None:
            return Item.from_dict(db_task)
        raise InvalidItemIdError(task_id)

    def list_tasks(self, owner=None, state=None):
        """Return a list of tasks filtered by owner and/or state.

        Args:
            owner (str, optional): Filter tasks by this owner. Defaults to
            None.
            state (str, optional): Filter tasks by this state. Defaults to
            None.

        Returns:
            list[Item]: List of Item instances matching the filters. If no
            filters are specified, returns all tasks.

        """
        all_tasks = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Item.from_dict(t)
                for t in all_tasks
                if (t["owner"] == owner and t["state"] == state)
            ]
        if owner is not None:
            return [
                Item.from_dict(t) for t in all_tasks if t["owner"] == owner
            ]
        if state is not None:
            return [
                Item.from_dict(t) for t in all_tasks if t["state"] == state
            ]
        return [Item.from_dict(t) for t in all_tasks]

    def count(self):
        """Return the number of tasks in the database.

        Returns:
            int: The number of tasks in the database.

        """
        return self._db.count()

    def update_task(self, task_id: int, task_mods: Item):
        """Update a task with modifications.

        Args:
            task_id (int): The ID of the task to update.
            task_mods (Item): Item instance containing the modifications to
            apply.

        Raises:
            InvalidItemIdError: If no task with the given ID exists.

        """
        try:
            self._db.update(task_id, task_mods.to_dict())
        except KeyError as exc:
            raise InvalidItemIdError(task_id) from exc

    def start(self, task_id: int):
        """Set a task state to 'in progress'.

        Args:
            task_id (int): The ID of the task to update.

        Raises:
            InvalidItemIdError: If no task with the given ID exists.

        """
        self.update_task(task_id, Item(state="in progress"))

    def finish(self, task_id: int):
        """Set a task state to 'done'.

        Args:
            task_id (int): The ID of the task to update.

        Raises:
            InvalidItemIdError: If no task with the given ID exists.

        """
        self.update_task(task_id, Item(state="done"))

    def delete_task(self, task_id: int):
        """Remove a task from the database.

        Args:
            task_id (int): The ID of the task to delete.

        Raises:
            InvalidItemIdError: If no task with the given ID exists.

        """
        try:
            self._db.delete(task_id)
        except KeyError as exc:
            raise InvalidItemIdError(task_id) from exc

    def delete_all(self):
        """Remove all tasks from the database."""
        self._db.delete_all()

    def close(self):
        """Close the database connection."""
        self._db.close()

    def path(self):
        """Return the path to the database.

        Returns:
            str or pathlib.Path: Path to the database file.

        """
        return self._db_path
