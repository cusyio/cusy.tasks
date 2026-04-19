# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""The configuration file for all cli tests."""

import shlex

import pytest

from typer.testing import CliRunner

from cusy import tasks


runner = CliRunner()


@pytest.fixture
def tasks_cli_no_redirect():
    """Fixture for calling the cli app with a list of parameters.

    Returns:
        function: Function for calling the cli app with the list of parameters.

    """

    def run_cli(command_string):
        """Pass `tasks.cli.app` and a list of strings to :func:`invoke`.

        More precisely, pass the application `tasks.cli.app` and a list of
        strings to the :func:`invoke` function of the cli test runner.

        Returns:
            str: Table with the columns ID, state, owner and summary

        """
        command_list = shlex.split(command_string)
        result = runner.invoke(tasks.cli.app, command_list)
        return result.output.rstrip()

    return run_cli


@pytest.fixture
def tasks_cli(tasks_cli_no_redirect, db_path, monkeypatch, tasks_db):
    """Monkeypatch fixture for the ITEMS_DB_DIR environment variable."""
    monkeypatch.setenv("ITEMS_DB_DIR", db_path.as_posix())
    return tasks_cli_no_redirect
