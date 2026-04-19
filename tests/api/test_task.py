# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the Task dataclass methods.

* Task.from_dict and Task.to_dict methods
* Task equality comparison
"""

from cusy.tasks import Task


def test_task_from_dict():
    """Test Task.from_dict method."""
    task_dict = {
        "summary": "Test summary",
        "owner": "Test owner",
        "state": "in progress",
        "id": 42,
    }

    task = Task.from_dict(task_dict)

    assert task.summary == "Test summary"
    assert task.owner == "Test owner"
    assert task.state == "in progress"
    assert task.id == 42


def test_task_to_dict():
    """Test Task.to_dict method."""
    task = Task(
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
    """Test Task equality comparison."""
    task1 = Task(
        summary="Same summary",
        owner="Same owner",
        state="todo",
        id=1,
    )
    task2 = Task(
        summary="Same summary",
        owner="Same owner",
        state="todo",
        id=2,
    )
    task3 = Task(
        summary="Different summary",
        owner="Same owner",
        state="todo",
        id=1,
    )

    # Tasks with same summary, owner, state but different id should be equal
    assert task1 == task2

    # Tasks with different summary should not be equal
    assert task1 != task3
