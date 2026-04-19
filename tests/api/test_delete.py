# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Testing the api delete function."""

import pytest

from cusy.tasks import InvalidTaskIdError, Task


@pytest.fixture
def three_tasks(tasks_db):
    """Create three tasks."""
    task1 = tasks_db.add_task(Task("Update pytest section"))
    task2 = tasks_db.add_task(Task("Update cibuildwheel section"))
    task3 = tasks_db.add_task(Task("Update mock tests"))
    return (task1, task2, task3)


def test_delete_from_many(tasks_db, three_tasks):
    """Testing the deletion of one task among several.

    After task2 is deleted, the number should have been reduced from three to
    two. In addition, task1 and task3 should still be present.
    """
    (task1, task2, task3) = three_tasks
    id_to_delete = task2
    ids_still_there = (task1, task3)

    tasks_db.delete_task(id_to_delete)

    assert tasks_db.count() == 2
    # task should not be retrievable after deletion
    with pytest.raises(InvalidTaskIdError):
        tasks_db.get_task(id_to_delete)
    # non-deleted tasks should still be retrievable
    for i in ids_still_there:
        # just making sure this doesn't throw an exception
        tasks_db.get_task(i)


def test_delete_last_task(tasks_db):
    """Test the deletion of the last added task to an empty database.

    The number of tasks should then be 0. In addition, get_task should throw
    an InvalidTaskIdError exception.
    """
    i = tasks_db.add_task(Task("Update pytest section"))
    tasks_db.delete_task(i)
    assert tasks_db.count() == 0
    with pytest.raises(InvalidTaskIdError):
        tasks_db.get_task(i)


def test_delete_non_existent(tasks_db):
    """Deleting a non-existent task.

    This should throw the InvalidTaskIdError exception.
    """
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidTaskIdError):
        tasks_db.delete_task(i)
