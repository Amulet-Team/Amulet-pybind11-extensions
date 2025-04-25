from unittest import TestCase


class PyModuleTestCase(TestCase):
    def test_iterator(self) -> None:
        from _test_pybind11 import get_iterator

        it = get_iterator()
        self.assertIs(it, iter(it))
        self.assertEqual(1, next(it))
        self.assertEqual(
            "get_iterator() -> collections.abc.Iterator[int]",
            get_iterator.__doc__.strip(),
        )
