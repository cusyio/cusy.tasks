# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""17ggTest Cases.

* finish from "todo", "in progress, and "done" states
* finish an invalid id
"""

import pytest

from cusy.tasks import InvalidItemIdError, Item


@pytest.mark.parametrize("start_state", ["todo", "in progress", "done"])
def test_finish(tasks_db, start_state):
    """End state should be "done"."""
    c = Item("Update pytest section", state=start_state)
    i = tasks_db.add_task(c)
    tasks_db.finish(i)
    c = tasks_db.get_task(i)
    assert c.state == "done"


def test_finish_non_existent(tasks_db):
    """Shouldn't be able to start a non-existent task."""
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidItemIdError):
        tasks_db.finish(i)
