from __future__ import annotations

import contextlib

__all__: list[str] = ["func", "state", "suppress"]

def func() -> contextlib.AbstractContextManager[str, bool | None]: ...
def suppress() -> contextlib.AbstractContextManager[None, bool | None]: ...

state: int = 0
