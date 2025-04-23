import unittest

from _test_builtins import MyPyClass, func1, func2, func3


class CollectionsTestCase(unittest.TestCase):
    def test_signature(self) -> None:
        a = MyPyClass(5)
        self.assertIsNot(a, func1(a))
        self.assertIs(a, func2(a))
        self.assertIs(a, func3(a))
        self.assertEqual("func1(arg0: _test_builtins.MyPyClass) -> _test_builtins.MyPyClass", func1.__doc__.strip())
        self.assertEqual("func2(arg0: _test_builtins.MyPyClass) -> _test_builtins.MyPyClass", func2.__doc__.strip())
        self.assertEqual("func3(arg0: _test_builtins.MyPyClass) -> _test_builtins.MyPyClass", func3.__doc__.strip())


if __name__ == "__main__":
    unittest.main()
