import unittest
from typing import Any, Callable
from collections.abc import Iterable

from _test_collections import (
    test_iterable_obj,
    test_iterable_int,
    IterTest,
    test_iterable_cls,
)


class CollectionsTestCase(unittest.TestCase):
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
            out = func(obj, objs)
            self.assertIs(obj, out)
            self.assertEqual(list(obj), objs)

        call_iterable([None, 1, "2", 3.0], test_iterable_obj)

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


if __name__ == "__main__":
    unittest.main()
