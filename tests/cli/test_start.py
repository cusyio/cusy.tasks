# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli start function."""

from cusy import tasks


def test_start(tasks_db, tasks_cli):
    """When start is called for a task, the state should be in progress."""
    i = tasks_db.add_task(tasks.Task("Update pytest section"))
    tasks_cli(f"start {i}")
    after = tasks_db.get_task(i)
    assert after.state == "in progress"
