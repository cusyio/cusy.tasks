.. SPDX-FileCopyrightText: 2023 Veit Schiele

.. SPDX-License-Identifier: BSD-3-Clause

API reference
=============

.. automodule:: cusy.tasks.api

:class:`cusy.tasks.api.Item` class
----------------------------------

.. autoclass:: Item
   :members: from_dict, to_dict

:class:`cusy.tasks.api.ItemsDB` class
-------------------------------------

.. autoclass:: ItemsDB
   :members: add_task, get_task, list_tasks, count, update_task, start, finish,
       delete_task, delete_all, close, path

Exceptions
----------

.. autoexception:: ItemsError
.. autoexception:: MissingSummaryError
.. autoexception:: InvalidItemIdError
