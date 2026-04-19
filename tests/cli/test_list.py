# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli list function.

* Tests the expected output, even if no parameter was specified.
* Test the cli list function with owner and state filters.
"""

from cusy import tasks


expected_output = """\

  ID   state   owner   summary                      
 ────────────────────────────────────────────────── 
  1    todo            Update pytest section        
  2    todo            Update cibuildwheel section  
"""


def test_list(tasks_db, tasks_cli):
    """When two tasks are added, ``list`` should be the ``expected_output``."""
    tasks_db.add_task(tasks.Task("Update pytest section"))
    tasks_db.add_task(tasks.Task("Update cibuildwheel section"))
    output = tasks_cli("list")
    assert output.strip() == expected_output.strip()


def test_main(tasks_db, tasks_cli):
    """Tasks without options on the command line should return the table.

    More precisely, even if tasks is called without options on the command
    line, the corresponding table should be returned.
    """
    tasks_db.add_task(tasks.Task("Update pytest section"))
    tasks_db.add_task(tasks.Task("Update cibuildwheel section"))
    output = tasks_cli("")
    assert output.strip() == expected_output.strip()


def test_list_filter_by_owner(tasks_db, tasks_cli):
    """Test filtering the list by owner."""
    tasks_db.add_task(tasks.Task("Task for Alice", owner="alice"))
    tasks_db.add_task(tasks.Task("Task for Bob", owner="bob"))
    tasks_db.add_task(tasks.Task("Another task for Alice", owner="alice"))

    output = tasks_cli("list -o alice")

    # Verify only Alice's tasks are shown
    assert "Task for Alice" in output
    assert "Another task for Alice" in output
    assert "Task for Bob" not in output


def test_list_filter_by_state(tasks_db, tasks_cli):
    """Test filtering the list by state."""
    tasks_db.add_task(tasks.Task("Todo task", state="todo"))
    in_progress_id = tasks_db.add_task(tasks.Task("In progress task"))
    done_id = tasks_db.add_task(tasks.Task("Done task"))

    tasks_db.start(in_progress_id)
    tasks_db.finish(done_id)

    output = tasks_cli("list -s 'in progress'")

    # Verify only "in progress" tasks are shown
    assert "In progress task" in output
    assert "Todo task" not in output
    assert "Done task" not in output


def test_list_filter_by_owner_and_state(tasks_db, tasks_cli):
    """Test filtering the list by both owner and state."""
    tasks_db.add_task(tasks.Task("Alice todo", owner="alice", state="todo"))
    in_progress_id = tasks_db.add_task(
        tasks.Task("Alice in progress", owner="alice"),
    )
    tasks_db.add_task(tasks.Task("Bob todo", owner="bob", state="todo"))

    tasks_db.start(in_progress_id)

    output = tasks_cli("list -o alice -s 'in progress'")

    # Verify only Alice's "in progress" tasks are shown
    assert "Alice in progress" in output
    assert "Alice todo" not in output
    assert "Bob todo" not in output
