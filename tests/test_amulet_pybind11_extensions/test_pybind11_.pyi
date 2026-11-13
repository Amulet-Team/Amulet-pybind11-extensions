from __future__ import annotations

import typing

__all__: list[str] = ["RefTest", "get_keep_alive"]

class RefTest:
    pass

def get_keep_alive() -> tuple[typing.Any, typing.Any]: ...
