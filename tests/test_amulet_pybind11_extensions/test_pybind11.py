import unittest
import weakref


class Pybind11TestCase(unittest.TestCase):
    def test_pybind11(self) -> None:
        from test_amulet_pybind11_extensions.test_pybind11_ import (
            get_keep_alive,
            RefTest,
        )

        a, b = get_keep_alive()
        self.assertIsInstance(a, RefTest)
        self.assertIsInstance(b, RefTest)
        b_ref = weakref.ref(b)
        del b
        self.assertIsNotNone(b_ref())
        del a
        self.assertIsNone(b_ref())


if __name__ == "__main__":
    unittest.main()
