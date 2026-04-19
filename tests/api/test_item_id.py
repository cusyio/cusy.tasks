# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test that the task ID is correctly assigned and returned.

* task id is correctly assigned and returned
* task id is included in the task object when retrieved
"""

from cusy.tasks import Task


def test_task_id_assignment(tasks_db):
    """Test that task ids are correctly assigned."""
    c1 = Task(summary="first task")
    c2 = Task(summary="second task")

    id1 = tasks_db.add_task(c1)
    id2 = tasks_db.add_task(c2)

    # Check that ids are different
    assert id1 != id2

    # Check that the ids are correctly stored in the tasks
    task1 = tasks_db.get_task(id1)
    task2 = tasks_db.get_task(id2)

    assert task1.id == id1
    assert task2.id == id2
