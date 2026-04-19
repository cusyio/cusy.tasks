# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Version for the api and the cli."""

__version__ = "26.2.0"

from .api import InvalidTaskIdError, Task, TasksDB
from .cli import app


__all__ = [
    "InvalidTaskIdError",
    "Task",
    "TasksDB",
    "app",
]
