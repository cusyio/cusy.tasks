# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test Cases.

* start from "todo", "in progress", and "done" states
* start an invalid id
"""

import pytest

from cusy.tasks import InvalidTaskIdError, Task


@pytest.mark.parametrize("start_state", ["todo", "in progress", "done"])
def test_start(tasks_db, start_state):
    """End state should be "in progress"."""
    i = Task("Update pytest section", state=start_state)
    ai = tasks_db.add_task(i)
    tasks_db.start(ai)
    i = tasks_db.get_task(ai)
    assert i.state == "in progress"


def test_start_non_existent(tasks_db):
    """Shouldn't be able to start a non-existent task."""
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidTaskIdError):
        tasks_db.start(i)
