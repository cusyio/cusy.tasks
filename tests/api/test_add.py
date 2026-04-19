# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test Cases.

* `add` to an empty database, with summary
* `add` to a non-empty database, with summary
* `add` a task with both summary and owner set
* `add` a duplicate task
* `add` a task with None owner
* `add` a task with empty string as owner
"""

import pytest

from cusy.tasks import Task


def test_add_from_empty(tasks_db):
    """'count' should be 1 and task retrievable."""
    c = Task(summary="do something")
    i = tasks_db.add_task(c)
    assert tasks_db.count() == 1
    assert tasks_db.get_task(i) == c


@pytest.mark.num_tasks(3)
def test_add_from_nonempty(tasks_db):
    """'count' should increase by 1 and task retrievable."""
    c = Task(summary="do something")
    i = tasks_db.add_task(c)
    assert tasks_db.count() == 4
    assert tasks_db.get_task(i) == c


def test_add_with_summary_and_owner(tasks_db):
    """'count' should be 1 and task retrievable."""
    c = Task(summary="do something", owner="Veit")
    i = tasks_db.add_task(c)
    assert tasks_db.count() == 1
    assert tasks_db.get_task(i) == c


def test_add_duplicate(tasks_db):
    """Duplicates allowed, both retrievable, separate indices."""
    c = Task(summary="do something")
    i_1 = tasks_db.add_task(c)
    i_2 = tasks_db.add_task(c)
    c1 = tasks_db.get_task(i_1)
    c2 = tasks_db.get_task(i_2)
    assert i_1 != i_2
    assert c1 == c2 == c


def test_none_owner(tasks_db):
    """When None is passed as owner, it should be stored as an empty string."""
    i = tasks_db.add_task(Task(summary="Task with None owner", owner=None))
    c = tasks_db.get_task(i)
    assert c.owner == ""


def test_empty_owner(tasks_db):
    """Empty string owner should be stored as is."""
    i = tasks_db.add_task(Task(summary="Task with empty owner", owner=""))
    c = tasks_db.get_task(i)
    assert c.owner == ""
