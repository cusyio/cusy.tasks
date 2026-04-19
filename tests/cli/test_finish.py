# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli finish function."""

from cusy import tasks


def test_finish(tasks_db, tasks_cli):
    """After finish has been called for a task, the status should be "done".

    After a task has been created and ``finish`` has been called for this task,
    the status should be "done".
    """
    i = tasks_db.add_task(tasks.Task("Update pytest section"))
    tasks_cli(f"finish {i}")
    after = tasks_db.get_task(i)
    assert after.state == "done"
