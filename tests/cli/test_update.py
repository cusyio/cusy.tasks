# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli update function."""

from cusy import tasks


def test_update(tasks_db, tasks_cli):
    """An task is changed, and when called, the changed values are returned.

    More precisely, if the owner and summary are changed with ``update``, this
    information and the unchanged state should be returned when this task is
    called.
    """
    i = tasks_db.add_task(tasks.Task("Update pytest section"))
    tasks_cli(f"update {i} -o veit -s foo")
    expected = tasks.Task("foo", owner="veit", state="todo")
    actual = tasks_db.get_task(i)
    assert actual == expected
