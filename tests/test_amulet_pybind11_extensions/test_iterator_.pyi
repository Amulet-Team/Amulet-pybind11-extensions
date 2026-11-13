from __future__ import annotations

import collections.abc

__all__: list[str] = ["get_iterator"]

def get_iterator() -> collections.abc.Iterator[int]: ...
