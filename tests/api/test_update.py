# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test Cases.

* `update` the owner of a task
* `update` the owner of a task to an empty string
* `update` the summary of a task
* `update` owner and summary of a task at the same time
* `update` a non-existent task
"""

import pytest

from cusy.tasks import InvalidTaskIdError, Task


def test_update_owner(tasks_db):
    """Summary and state should stay the same, only owner should change."""
    i = tasks_db.add_task(Task("Update pytest section", owner="veit"))
    tasks_db.update_task(i, Task(owner="vsc", state=None))

    mod = tasks_db.get_task(i)
    assert mod == Task("Update pytest section", owner="vsc")


def test_update_to_empty_owner(tasks_db):
    """Update an owner to an empty string should work."""
    i = tasks_db.add_task(Task(summary="Update pytest section", owner="veit"))
    tasks_db.update_task(i, Task(owner=""))
    mod = tasks_db.get_task(i)
    assert mod.owner == ""
    assert mod.summary == "Update pytest section"


def test_update_summary(tasks_db):
    """Owner and state should stay the same, summary should change."""
    i = tasks_db.add_task(
        Task("Update pytest section", owner="veit", state="done"),
    )
    tasks_db.update_task(
        i,
        Task(summary="Update cibuildwheel section", state=None),
    )

    mod = tasks_db.get_task(i)
    assert mod == Task(
        "Update cibuildwheel section",
        owner="veit",
        state="done",
    )


def test_update_both(tasks_db):
    """State should stay the same, owner and summary should change."""
    i = tasks_db.add_task(Task("Update pytest section", owner="veit"))
    tasks_db.update_task(
        i,
        Task(summary="Update cibuildwheel section", owner="vsc"),
    )

    mod = tasks_db.get_task(i)
    assert mod == Task(
        "Update cibuildwheel section",
        owner="vsc",
        state="todo",
    )


def test_update_non_existent(tasks_db):
    """Shouldn't be able to update a non-existent task."""
    i = 123  # any number will do, db is empty
    with pytest.raises(InvalidTaskIdError):
        tasks_db.update_task(
            i,
            Task(summary="Update cibuildwheel section", owner="vsc"),
        )
