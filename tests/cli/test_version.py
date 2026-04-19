# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli version function."""

from cusy import tasks


def test_version(tasks_cli):
    """The version cli option should be the same as __version__ in Python."""
    assert tasks_cli("version") == tasks.__version__
