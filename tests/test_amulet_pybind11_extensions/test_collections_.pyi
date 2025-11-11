from __future__ import annotations

import collections.abc
import types
import typing

__all__: list[str] = [
    "TestToken",
    "test_items_view_cls",
    "test_items_view_int",
    "test_items_view_obj",
    "test_iterable_cls",
    "test_iterable_int",
    "test_iterable_obj",
    "test_iterator_cls",
    "test_iterator_int",
    "test_iterator_obj",
    "test_keys_view_cls",
    "test_keys_view_int",
    "test_keys_view_obj",
    "test_map_cls",
    "test_map_int",
    "test_map_obj",
    "test_mutable_map_cls",
    "test_mutable_map_int",
    "test_mutable_map_obj",
    "test_sequence_cls",
    "test_sequence_int",
    "test_sequence_obj",
    "test_values_view_cls",
    "test_values_view_int",
    "test_values_view_obj",
]

class TestToken:
    @typing.overload
    def __eq__(self, other: TestToken) -> bool: ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool | types.NotImplementedType: ...
    def __hash__(self) -> int: ...
    def __init__(self, arg0: typing.SupportsInt) -> None: ...
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, arg0: typing.SupportsInt) -> None: ...

def test_items_view_cls(
    arg0: collections.abc.ItemsView[typing.SupportsInt, TestToken],
) -> collections.abc.ItemsView[int, TestToken]: ...
def test_items_view_int(
    arg0: collections.abc.ItemsView[typing.SupportsInt, typing.SupportsInt],
) -> collections.abc.ItemsView[int, int]: ...
def test_items_view_obj(
    arg0: collections.abc.ItemsView[typing.SupportsInt, typing.Any],
) -> collections.abc.ItemsView[int, typing.Any]: ...
def test_iterable_cls(
    arg0: collections.abc.Iterable[TestToken], arg1: list
) -> collections.abc.Iterable[TestToken]: ...
def test_iterable_int(
    arg0: collections.abc.Iterable[typing.SupportsInt], arg1: list
) -> collections.abc.Iterable[int]: ...
def test_iterable_obj(
    arg0: collections.abc.Iterable[typing.Any], arg1: list
) -> collections.abc.Iterable[typing.Any]: ...
def test_iterator_cls(
    arg0: collections.abc.Iterator[TestToken], arg1: list
) -> collections.abc.Iterator[TestToken]: ...
def test_iterator_int(
    arg0: collections.abc.Iterator[typing.SupportsInt], arg1: list
) -> collections.abc.Iterator[int]: ...
def test_iterator_obj(
    arg0: collections.abc.Iterator[typing.Any], arg1: list
) -> collections.abc.Iterator[typing.Any]: ...
def test_keys_view_cls(
    arg0: collections.abc.KeysView[TestToken],
) -> collections.abc.KeysView[TestToken]: ...
def test_keys_view_int(
    arg0: collections.abc.KeysView[typing.SupportsInt],
) -> collections.abc.KeysView[int]: ...
def test_keys_view_obj(
    arg0: collections.abc.KeysView[typing.Any],
) -> collections.abc.KeysView[typing.Any]: ...
def test_map_cls(
    arg0: collections.abc.Mapping[typing.SupportsInt, TestToken],
) -> collections.abc.Mapping[int, TestToken]: ...
def test_map_int(
    arg0: collections.abc.Mapping[typing.SupportsInt, typing.SupportsInt],
) -> collections.abc.Mapping[int, int]: ...
def test_map_obj(
    arg0: collections.abc.Mapping[typing.SupportsInt, typing.Any],
) -> collections.abc.Mapping[int, typing.Any]: ...
def test_mutable_map_cls(
    arg0: collections.abc.MutableMapping[typing.SupportsInt, TestToken],
) -> collections.abc.MutableMapping[int, TestToken]: ...
def test_mutable_map_int(
    arg0: collections.abc.MutableMapping[typing.SupportsInt, typing.SupportsInt],
) -> collections.abc.MutableMapping[int, int]: ...
def test_mutable_map_obj(
    arg0: collections.abc.MutableMapping[typing.SupportsInt, typing.Any],
) -> collections.abc.MutableMapping[int, typing.Any]: ...
def test_sequence_cls(
    arg0: collections.abc.Sequence[TestToken], arg1: list
) -> collections.abc.Sequence[TestToken]: ...
def test_sequence_int(
    arg0: collections.abc.Sequence[typing.SupportsInt], arg1: list
) -> collections.abc.Sequence[int]: ...
def test_sequence_obj(
    arg0: collections.abc.Sequence[typing.Any], arg1: list
) -> collections.abc.Sequence[typing.Any]: ...
def test_values_view_cls(
    arg0: collections.abc.ValuesView[TestToken],
) -> collections.abc.ValuesView[TestToken]: ...
def test_values_view_int(
    arg0: collections.abc.ValuesView[typing.SupportsInt],
) -> collections.abc.ValuesView[int]: ...
def test_values_view_obj(
    arg0: collections.abc.ValuesView[typing.Any],
) -> collections.abc.ValuesView[typing.Any]: ...
