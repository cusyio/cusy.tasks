# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli add function."""

from cusy import tasks


def test_add(tasks_db, tasks_cli):
    """Two tests for adding a task.

    The first test checks whether the number of tasks is 1 after a task has
    been added; the second test checks whether the summary, owner and status of
    this task match.
    """
    tasks_cli("add some task")
    expected = tasks.Item("some task", owner="", state="todo")
    all = tasks_db.list_tasks()
    assert len(all) == 1
    assert all[0] == expected


def test_add_with_owner(tasks_db, tasks_cli):
    """The same tests as above, but an owner is also specified."""
    tasks_cli("add some task -o veit")
    expected = tasks.Item("some task", owner="veit", state="todo")
    all = tasks_db.list_tasks()
    assert len(all) == 1
    assert all[0] == expected
