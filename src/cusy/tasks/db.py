# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""DB for the tasks project."""

import tinydb


class DB:
    """Class for communication with the database.

    Args:
        db_path (str or pathlib.Path): Directory path for the database file.
        db_file_prefix (str): Prefix for the database filename.

    """

    def __init__(self, db_path, db_file_prefix):
        """Connect to the database or creates it if it doesn't exist."""
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json",
            create_dirs=True,
        )

    def create(self, task: dict) -> int:
        """Create a task in the database.

        Args:
            task (dict): Dictionary containing the task data.

        Returns:
            int: The ID of the newly created task.

        """
        return self._db.insert(task)

    def read(self, id: int):
        """Read a task from the database.

        Args:
            id (int): The ID of the task to read.

        Returns:
            dict or None: The task object or None if not found.

        """
        return self._db.get(doc_id=id)

    def read_all(self):
        """Read the entire database.

        Returns:
            tinydb.TinyDB: All tasks in the database.

        """
        return self._db

    def update(self, id: int, mods) -> None:
        """Update a task in the database.

        Args:
            id (int): The ID of the task to update.
            mods (dict): Dictionary containing the modifications to apply.

        Raises:
            KeyError: If no task with the given ID exists.

        """
        changes = {k: v for k, v in mods.items() if v is not None}
        self._db.update(changes, doc_ids=[id])

    def delete(self, id: int) -> None:
        """Delete a task from the database.

        Args:
            id (int): The ID of the task to delete.

        Raises:
            KeyError: If no task with the given ID exists.

        """
        self._db.remove(doc_ids=[id])

    def delete_all(self) -> None:
        """Delete all tasks in the database.

        Returns:
            None: This function doesn't return anything.

        """
        self._db.truncate()

    def count(self) -> int:
        """Count all tasks in the database.

        Returns:
            int: The number of tasks in the database.

        """
        return len(self._db)

    def close(self):
        """Close the database connection.

        Returns:
            None: This function doesn't return anything.

        """
        self._db.close()
