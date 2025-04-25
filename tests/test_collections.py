import unittest
from typing import Callable
from collections.abc import Iterable, Iterator

from _test_collections import (
    IterTest,
    test_iterable_obj,
    test_iterable_int,
    test_iterable_cls,
    test_iterator_obj,
    test_iterator_int,
    test_iterator_cls,
)


class CollectionsTestCase(unittest.TestCase):
    def test_iterator(self) -> None:
        self.assertEqual(
            "test_iterator_obj(arg0: collections.abc.Iterator[object], arg1: list) -> collections.abc.Iterator[object]",
            test_iterator_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterator_int(arg0: collections.abc.Iterator[int], arg1: list) -> collections.abc.Iterator[int]",
            test_iterator_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterator_cls(arg0: collections.abc.Iterator[_test_collections.IterTest], arg1: list) -> collections.abc.Iterator[_test_collections.IterTest]",
            test_iterator_cls.__doc__.strip(),
        )

        def call_iterator(obj: Iterable, func: Callable[[Iterator, list], Iterator]) -> None:
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

        call_iterator([IterTest(1), IterTest(2), IterTest(3)], test_iterator_cls)
        call_iterator((IterTest(1), IterTest(2), IterTest(3)), test_iterator_cls)
        call_iterator(
            dict.fromkeys([IterTest(1), IterTest(2), IterTest(3)], None),
            test_iterator_cls,
        )

        out = []
        with self.assertRaises(RuntimeError):
            test_iterator_int(iter([1, 2, "test"]), out)
        self.assertEqual([1, 2], out)

    def test_iterable(self) -> None:
        self.assertEqual(
            "test_iterable_obj(arg0: collections.abc.Iterable[object], arg1: list) -> collections.abc.Iterable[object]",
            test_iterable_obj.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterable_int(arg0: collections.abc.Iterable[int], arg1: list) -> collections.abc.Iterable[int]",
            test_iterable_int.__doc__.strip(),
        )
        self.assertEqual(
            "test_iterable_cls(arg0: collections.abc.Iterable[_test_collections.IterTest], arg1: list) -> collections.abc.Iterable[_test_collections.IterTest]",
            test_iterable_cls.__doc__.strip(),
        )

        def call_iterable(obj: Iterable, func: Callable[[Iterable, list], Iterable]) -> None:
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

        call_iterable([IterTest(1), IterTest(2), IterTest(3)], test_iterable_cls)
        call_iterable((IterTest(1), IterTest(2), IterTest(3)), test_iterable_cls)
        call_iterable(
            dict.fromkeys([IterTest(1), IterTest(2), IterTest(3)], None),
            test_iterable_cls,
        )

        out = []
        with self.assertRaises(RuntimeError):
            test_iterable_int([1, 2, "test"], out)
        self.assertEqual([1, 2], out)


if __name__ == "__main__":
    unittest.main()
