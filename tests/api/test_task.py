# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the Item dataclass methods.

* Item.from_dict and Item.to_dict methods
* Item equality comparison
"""

from cusy.tasks import Item


def test_task_from_dict():
    """Test Item.from_dict method."""
    task_dict = {
        "summary": "Test summary",
        "owner": "Test owner",
        "state": "in progress",
        "id": 42,
    }

    task = Item.from_dict(task_dict)

    assert task.summary == "Test summary"
    assert task.owner == "Test owner"
    assert task.state == "in progress"
    assert task.id == 42


def test_task_to_dict():
    """Test Item.to_dict method."""
    task = Item(
        summary="Test summary",
        owner="Test owner",
        state="in progress",
        id=42,
    )

    task_dict = task.to_dict()

    assert task_dict["summary"] == "Test summary"
    assert task_dict["owner"] == "Test owner"
    assert task_dict["state"] == "in progress"
    assert task_dict["id"] == 42


def test_task_equality():
    """Test Item equality comparison."""
    task1 = Item(
        summary="Same summary",
        owner="Same owner",
        state="todo",
        id=1,
    )
    task2 = Item(
        summary="Same summary",
        owner="Same owner",
        state="todo",
        id=2,
    )
    task3 = Item(
        summary="Different summary",
        owner="Same owner",
        state="todo",
        id=1,
    )

    # Items with same summary, owner, state but different id should be equal
    assert task1 == task2

    # Items with different summary should not be equal
    assert task1 != task3
