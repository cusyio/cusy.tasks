# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the MissingSummaryError exception.

* adding a task with no summary raises MissingSummaryError
* adding a task with empty summary raises MissingSummaryError
"""

import pytest

from cusy.tasks import Item
from cusy.tasks.api import MissingSummaryError


def test_missing_summary(tasks_db):
    """Test that adding a task with no summary raises MissingSummaryError."""
    with pytest.raises(MissingSummaryError):
        tasks_db.add_task(Item())


def test_empty_summary(tasks_db):
    """Test adding a task with empty summary.

    This should raise a MissingSummaryError.
    """
    with pytest.raises(MissingSummaryError):
        tasks_db.add_task(Item(summary=""))
