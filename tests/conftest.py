# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""The configuration file for all tests."""

import pytest

from cusy import tasks
from cusy.tasks import Item


@pytest.fixture(scope="session")
def db_path(tmp_path_factory):
    """Path to a temporary database."""
    return tmp_path_factory.mktemp("tasks_db")


@pytest.fixture(scope="session")
def session_tasks_db(db_path):
    """Establish and close the connection to the database."""
    db_ = tasks.ItemsDB(db_path)
    yield db_
    db_.close()


@pytest.fixture
def tasks_db(session_tasks_db, request, faker):
    """Return the database object."""
    db = session_tasks_db
    db.delete_all()
    # support for `@pytest.mark.num_tasks(<some number>)`
    faker.seed_instance(101)  # random seed
    m = request.node.get_closest_marker("num_tasks")
    if m and len(m.args) > 0:
        num_tasks = m.args[0]
        for _ in range(num_tasks):
            db.add_task(
                Item(summary=faker.sentence(), owner=faker.first_name()),
            )
    return db
