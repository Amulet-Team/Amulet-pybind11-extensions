import unittest


class IteratorTestCase(unittest.TestCase):
    def test_iterator(self) -> None:
        from test_amulet_pybind11_extensions.test_iterator_ import get_iterator

        it = get_iterator()
        self.assertIs(it, iter(it))
        self.assertEqual(1, next(it))
        self.assertEqual(
            "get_iterator() -> collections.abc.Iterator[int]",
            get_iterator.__doc__.strip(),
        )


if __name__ == "__main__":
    unittest.main()
