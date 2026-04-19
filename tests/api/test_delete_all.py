# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Testing the api delete all function with.

* delete_all removes all tasks from the database
* delete_all on an empty database doesn't cause errors
"""

import pytest


@pytest.mark.num_tasks(5)
def test_delete_all_from_many(tasks_db):
    """Test that delete_all removes all tasks."""
    assert tasks_db.count() == 5
    tasks_db.delete_all()
    assert tasks_db.count() == 0
    assert tasks_db.list_tasks() == []


def test_delete_all_from_empty(tasks_db):
    """Test that delete_all on an empty database works."""
    assert tasks_db.count() == 0
    tasks_db.delete_all()
    assert tasks_db.count() == 0
