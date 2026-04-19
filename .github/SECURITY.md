<!-- SPDX-FileCopyrightText: 2023 Veit Schiele

SPDX-License-Identifier: BSD-3-Clause -->

# Security policy

## Supported versions

We follow [calendar versioning](https://calver.org). Therefore, we only support the latest version.

Nevertheless, you should not be afraid to upgrade if you only use our documented public APIs and pay attention to deprecation warnings.
Whenever compatibility needs to be broken, this will be announced in the changelog and a `DeprecationWarning` will be triggered for one year, if possible, before compatibility is finally broken.


> [!WARNING]
> There is **one** exception:
>
> APIs may be labelled as *provisional*.
> They are not guaranteed to be stable, and they may change or be removed without notice.

## Reporting a security vulnerability

If you believe you have found a vulnerability, please use [GitHub’s security advisory form](https://github.com/cusyio/cusy.tasks/security/advisories/new) or email Veit Schiele at veit@cusy.io.
