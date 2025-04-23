import unittest

from _test_collections import test_iter_obj, test_iter_int, IterTest, test_iter_cls


class CollectionsTestCase(unittest.TestCase):
    def test_signature(self) -> None:
        self.assertEqual(
            "test_iter_obj(arg0: collections.abc.Iterable) -> collections.abc.Iterable\n",
            test_iter_obj.__doc__,
        )
        self.assertEqual(
            "test_iter_int(arg0: collections.abc.Iterable[int]) -> collections.abc.Iterable[int]\n",
            test_iter_int.__doc__,
        )
        self.assertEqual(
            "test_iter_cls(arg0: collections.abc.Iterable[_test_collections.IterTest]) -> collections.abc.Iterable[_test_collections.IterTest]\n",
            test_iter_cls.__doc__,
        )

    def test_collections(self) -> None:
        test_iter_obj([None, 1, "2", 3.0])
        test_iter_obj((None, 1, "2", 3.0))
        test_iter_obj(dict.fromkeys((None, 1, "2", 3.0), None))

        test_iter_int([1, 2, 3])
        test_iter_int((1, 2, 3))
        test_iter_int(dict.fromkeys([1, 2, 3], None))

        test_iter_cls([IterTest(1), IterTest(2), IterTest(3)])
        test_iter_cls((IterTest(1), IterTest(2), IterTest(3)))
        test_iter_cls(dict.fromkeys([IterTest(1), IterTest(2), IterTest(3)], None))


if __name__ == "__main__":
    unittest.main()
