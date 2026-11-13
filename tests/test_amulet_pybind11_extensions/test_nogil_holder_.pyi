from __future__ import annotations

__all__: list[str] = ["Bool", "NoGILHolderTestClass"]

class Bool:
    def __bool__(self) -> bool: ...
    def __init__(self, arg0: bool) -> None: ...

class NoGILHolderTestClass:
    def __init__(self, arg0: Bool) -> None: ...
