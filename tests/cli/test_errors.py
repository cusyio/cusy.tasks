# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli behavior with missing arguments, invalid ids and commands."""

import pytest


@pytest.mark.parametrize(
    "command",
    ["delete", "update"],
)
def test_missing_required_args(command, tasks_cli):
    """Commands with missing required arguments should throw an error."""
    out = tasks_cli(command)
    assert "Missing argument" in out


@pytest.mark.parametrize(
    "command",
    ["delete 42", "start 42", "finish 42", "update 42 -s foo -o veit"],
)
def test_invalid_task_id(command, tasks_cli):
    """Actions on a non-existent task should throw an error message.

    If the task with id 42 is deleted, started, finished or updated, the error
    message "Error: Invalid task id 42" should be output.
    """
    out = tasks_cli(command)
    assert "Error: Invalid task id 42" in out


def test_invalid_command(tasks_cli):
    """Using an invalid command should show an error message."""
    out = tasks_cli("nonexistent")
    assert "No such command 'nonexistent'." in out
