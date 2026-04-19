# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli delete function."""

from cusy import tasks


def test_delete(tasks_db, tasks_cli):
    """After a task has been added and deleted, ``count`` should be ``0``."""
    i = tasks_db.add_task(tasks.Item("Update pytest section"))
    tasks_cli(f"delete {i}")
    assert tasks_db.count() == 0
