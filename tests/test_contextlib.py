from unittest import TestCase

import _test_contextlib
from _test_contextlib import func, suppress

class MyException(Exception):
    pass


class ContextLibTestCase(TestCase):
    def test_contextlib(self) -> None:
        self.assertEqual("func() -> contextlib.AbstractContextManager[str, Optional[bool]]", func.__doc__.strip())
        self.assertEqual(0, _test_contextlib.state)
        with func() as value:
            self.assertIsInstance(value, str)
            self.assertEqual("hello world", value)
            self.assertEqual(1, _test_contextlib.state)
        self.assertEqual(0, _test_contextlib.state)
        with self.assertRaises(MyException):
            with func() as value:
                self.assertIsInstance(value, str)
                self.assertEqual("hello world", value)
                self.assertEqual(1, _test_contextlib.state)
                raise MyException
        self.assertEqual(0, _test_contextlib.state)

        with suppress() as value:
            self.assertIsNone(value)
            raise MyException
