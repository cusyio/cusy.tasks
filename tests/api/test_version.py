# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test Cases.

* version returns the correct version
"""

import re

from cusy import tasks


def test_version():
    """There is no api for version other than tasks.__version__.

    However, we do expect it to be a string containing a version in the form of
    "I.J.K".
    """
    version = tasks.__version__
    assert re.match(r"\d+\.\d+\.\d+", version)
