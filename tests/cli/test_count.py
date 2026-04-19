# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli count function."""

import pytest


@pytest.mark.num_tasks(3)
def test_count(tasks_cli):
    """After 3 tasks have been written to the db, ``count`` should return 3.

    More precisely, after three tasks have been written to the database with
    ``num_tasks(3)``, ``count`` should return "3".
    """
    assert tasks_cli("count") == "3"
