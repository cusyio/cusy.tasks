# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Testing the api count function."""

import pytest


def test_count_no_tasks(tasks_db):
    """In an empty database, the result should be 0."""
    assert tasks_db.count() == 0


@pytest.mark.num_tasks(1)
def test_count_one_task(tasks_db):
    """In a database with one task, the result should be 1."""
    assert tasks_db.count() == 1


@pytest.mark.num_tasks(3)
def test_count_three_tasks(tasks_db):
    """In a database with three tasks, the result should be 3."""
    assert tasks_db.count() == 3
