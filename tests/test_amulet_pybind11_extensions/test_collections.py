from __future__ import annotations

import unittest
from typing import Callable
from collections.abc import Iterable, Iterator, Sequence

from test_amulet_pybind11_extensions.test_collections_ import (
    TestToken,
    test_iterable_obj,
    test_iterable_int,
    test_iterable_cls,
    test_iterator_obj,
    test_iterator_int,
    test_iterator_cls,
    test_sequence_obj,
    test_sequence_int,
    test_sequence_cls,
    test_map_obj,
    test_map_int,
    test_map_cls,
    test_mutable_map_obj,
    test_mutable_map_int,
    test_mutable_map_cls,
    test_keys_view_obj,
    test_keys_view_int,
    test_keys_view_cls,
    test_values_view_obj,
    test_values_view_int,
    test_values_view_cls,
    test_items_view_obj,
    test_items_view_int,
    test_items_view_cls,
)


class CollectionsTestCase(unittest.TestCase):
    def test_collections(self) -> None:
        self.assertEqual(
            "test_iterator_obj(arg0: collections.abc.Iterator[object], arg1: list) -> collections.abc.Iterator[object]",
            test_iterator_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterator_int(arg0: collections.abc.Iterator[int], arg1: list) -> collections.abc.Iterator[int]",
            test_iterator_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterator_cls(arg0: collections.abc.Iterator[test_amulet_pybind11_extensions.test_collections_.TestToken], arg1: list) -> collections.abc.Iterator[test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_iterator_cls.__doc__.strip(),
        )

        def call_iterator(
            obj: Iterable, func: Callable[[Iterator, list], Iterator]
        ) -> None:
            objs = []
            it = iter(obj)
            it2 = func(it, objs)
            self.assertIs(it, it2)
            self.assertEqual(list(obj), objs)

        call_iterator([None, 1, "2", 3.0], test_iterator_obj)
        call_iterator((None, 1, "2", 3.0), test_iterator_obj)
        call_iterator(dict.fromkeys((None, 1, "2", 3.0), None), test_iterator_obj)

        call_iterator([1, 2, 3], test_iterator_int)
        call_iterator((1, 2, 3), test_iterator_int)
        call_iterator(dict.fromkeys([1, 2, 3], None), test_iterator_int)

        call_iterator([TestToken(1), TestToken(2), TestToken(3)], test_iterator_cls)
        call_iterator((TestToken(1), TestToken(2), TestToken(3)), test_iterator_cls)
        call_iterator(
            dict.fromkeys([TestToken(1), TestToken(2), TestToken(3)], None),
            test_iterator_cls,
        )

        out = []
        with self.assertRaises(ValueError):
            test_iterator_int(iter([1, 2, "test"]), out)
        self.assertEqual([1, 2], out)

        with self.assertRaises(TypeError):
            test_iterator_obj([])

        with self.assertRaises(TypeError):
            test_iterator_obj(())

        with self.assertRaises(TypeError):
            test_iterator_obj({})

        with self.assertRaises(TypeError):
            test_iterator_obj(None)

        class MyIterator:
            def __init__(self) -> None:
                self.set = False

            def __iter__(self) -> MyIterator:
                return self

            def __next__(self) -> int:
                if self.set:
                    raise StopIteration
                else:
                    self.set = True
                    return 1

        out = []
        test_iterator_obj(MyIterator(), out)
        self.assertEqual([1], out)

    def test_iterable(self) -> None:
        self.assertEqual(
            "test_iterable_obj(arg0: collections.abc.Iterable[object], arg1: list) -> collections.abc.Iterable[object]",
            test_iterable_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterable_int(arg0: collections.abc.Iterable[typing.SupportsInt], arg1: list) -> collections.abc.Iterable[int]",
            test_iterable_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterable_cls(arg0: collections.abc.Iterable[test_amulet_pybind11_extensions.test_collections_.TestToken], arg1: list) -> collections.abc.Iterable[test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_iterable_cls.__doc__.strip(),
        )

        def call_iterable(
            obj: Iterable, func: Callable[[Iterable, list], Iterable]
        ) -> None:
            objs = []
            obj2 = func(obj, objs)
            self.assertIs(obj, obj2)
            self.assertEqual(list(obj), objs)

        call_iterable([None, 1, "2", 3.0], test_iterable_obj)
        call_iterable((None, 1, "2", 3.0), test_iterable_obj)
        call_iterable(dict.fromkeys((None, 1, "2", 3.0), None), test_iterable_obj)

        call_iterable([1, 2, 3], test_iterable_int)
        call_iterable((1, 2, 3), test_iterable_int)
        call_iterable(dict.fromkeys([1, 2, 3], None), test_iterable_int)

        call_iterable([TestToken(1), TestToken(2), TestToken(3)], test_iterable_cls)
        call_iterable((TestToken(1), TestToken(2), TestToken(3)), test_iterable_cls)
        call_iterable(
            dict.fromkeys([TestToken(1), TestToken(2), TestToken(3)], None),
            test_iterable_cls,
        )

        out = []
        with self.assertRaises(RuntimeError):
            test_iterable_int([1, 2, "test"], out)
        self.assertEqual([1, 2], out)

        with self.assertRaises(TypeError):
            test_iterable_obj(iter([]))

        with self.assertRaises(TypeError):
            test_iterable_obj(iter(()))

        with self.assertRaises(TypeError):
            test_iterable_obj(iter({}))

        with self.assertRaises(TypeError):
            test_iterable_obj(None)

        class MyIterable:
            def __init__(self) -> None:
                self.values = [None, 1, "2", 3.0]

            def __getitem__(self, index: int) -> object:
                return self.values[index]

            def __len__(self) -> int:
                return len(self.values)

        out = []
        test_iterable_obj(MyIterable(), out)
        self.assertEqual([None, 1, "2", 3.0], out)

    def test_sequence(self) -> None:
        self.assertEqual(
            "test_sequence_obj(arg0: collections.abc.Sequence[object], arg1: list) -> collections.abc.Sequence[object]",
            test_sequence_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_sequence_int(arg0: collections.abc.Sequence[typing.SupportsInt], arg1: list) -> collections.abc.Sequence[int]",
            test_sequence_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_sequence_cls(arg0: collections.abc.Sequence[test_amulet_pybind11_extensions.test_collections_.TestToken], arg1: list) -> collections.abc.Sequence[test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_sequence_cls.__doc__.strip(),
        )

        def call_sequence(
            obj: Sequence, func: Callable[[Sequence, list], Sequence]
        ) -> None:
            objs = []
            obj2 = func(obj, objs)
            self.assertIs(obj, obj2)
            self.assertEqual(list(obj), objs)

        call_sequence([None, 1, "2", 3.0], test_sequence_obj)
        call_sequence((None, 1, "2", 3.0), test_sequence_obj)

        call_sequence([1, 2, 3], test_sequence_int)
        call_sequence((1, 2, 3), test_sequence_int)

        call_sequence([TestToken(1), TestToken(2), TestToken(3)], test_sequence_cls)
        call_sequence((TestToken(1), TestToken(2), TestToken(3)), test_sequence_cls)

        out = []
        with self.assertRaises(TypeError):
            test_sequence_int(None, out)
        self.assertEqual([], out)

    def test_map(self) -> None:
        self.assertEqual(
            "test_map_obj(arg0: collections.abc.Mapping[int, object]) -> collections.abc.Mapping[int, object]",
            test_map_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_map_int(arg0: collections.abc.Mapping[int, int]) -> collections.abc.Mapping[int, int]",
            test_map_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_map_cls(arg0: collections.abc.Mapping[int, test_amulet_pybind11_extensions.test_collections_.TestToken]) -> collections.abc.Mapping[int, test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_map_cls.__doc__.strip(),
        )

    def test_mutable_map(self) -> None:
        self.assertEqual(
            "test_mutable_map_obj(arg0: collections.abc.MutableMapping[int, object]) -> collections.abc.MutableMapping[int, object]",
            test_mutable_map_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_mutable_map_int(arg0: collections.abc.MutableMapping[int, int]) -> collections.abc.MutableMapping[int, int]",
            test_mutable_map_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_mutable_map_cls(arg0: collections.abc.MutableMapping[int, test_amulet_pybind11_extensions.test_collections_.TestToken]) -> collections.abc.MutableMapping[int, test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_mutable_map_cls.__doc__.strip(),
        )

    def test_keys_view(self) -> None:
        self.assertEqual(
            "test_keys_view_obj(arg0: collections.abc.KeysView[object]) -> collections.abc.KeysView[object]",
            test_keys_view_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_keys_view_int(arg0: collections.abc.KeysView[int]) -> collections.abc.KeysView[int]",
            test_keys_view_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_keys_view_cls(arg0: collections.abc.KeysView[test_amulet_pybind11_extensions.test_collections_.TestToken]) -> collections.abc.KeysView[test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_keys_view_cls.__doc__.strip(),
        )

    def test_values_view(self) -> None:
        self.assertEqual(
            "test_values_view_obj(arg0: collections.abc.ValuesView[object]) -> collections.abc.ValuesView[object]",
            test_values_view_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_values_view_int(arg0: collections.abc.ValuesView[int]) -> collections.abc.ValuesView[int]",
            test_values_view_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_values_view_cls(arg0: collections.abc.ValuesView[test_amulet_pybind11_extensions.test_collections_.TestToken]) -> collections.abc.ValuesView[test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_values_view_cls.__doc__.strip(),
        )

    def test_items_view(self) -> None:
        self.assertEqual(
            "test_items_view_obj(arg0: collections.abc.ItemsView[int, object]) -> collections.abc.ItemsView[int, object]",
            test_items_view_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_items_view_int(arg0: collections.abc.ItemsView[int, int]) -> collections.abc.ItemsView[int, int]",
            test_items_view_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_items_view_cls(arg0: collections.abc.ItemsView[int, test_amulet_pybind11_extensions.test_collections_.TestToken]) -> collections.abc.ItemsView[int, test_amulet_pybind11_extensions.test_collections_.TestToken]",
            test_items_view_cls.__doc__.strip(),
        )


if __name__ == "__main__":
    unittest.main()
