import unittest

import test_amulet_pybind11_extensions.test_contextlib_ as test_contextlib
from test_amulet_pybind11_extensions.test_contextlib_ import func, suppress


class MyException(Exception):
    pass


class ContextLibTestCase(unittest.TestCase):
    def test_contextlib(self) -> None:
        self.assertEqual(
            "func() -> contextlib.AbstractContextManager[str, bool | None]",
            (func.__doc__ or "").strip(),
        )
        self.assertEqual(0, test_contextlib.state)
        with func() as value:
            self.assertIsInstance(value, str)
            self.assertEqual("hello world", value)
            self.assertEqual(1, test_contextlib.state)
        self.assertEqual(0, test_contextlib.state)
        with self.assertRaises(MyException):
            with func() as value:
                self.assertIsInstance(value, str)
                self.assertEqual("hello world", value)
                self.assertEqual(1, test_contextlib.state)
                raise MyException
        self.assertEqual(0, test_contextlib.state)

        with suppress() as value:
            self.assertIsNone(value)
            raise MyException


if __name__ == "__main__":
    unittest.main()
