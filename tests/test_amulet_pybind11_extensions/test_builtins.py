import unittest

from test_amulet_pybind11_extensions.test_builtins_ import (
    MyPyClass,
    func1,
    func2,
    func3,
)


class BuiltinsTestCase(unittest.TestCase):
    def test_signature(self) -> None:
        a = MyPyClass(5)
        self.assertIsNot(a, func1(a))
        self.assertIs(a, func2(a))
        self.assertIs(a, func3(a))
        self.assertEqual(
            "func1(arg0: test_amulet_pybind11_extensions.test_builtins_.MyPyClass) -> test_amulet_pybind11_extensions.test_builtins_.MyPyClass",
            func1.__doc__.strip(),
        )
        self.assertEqual(
            "func2(arg0: test_amulet_pybind11_extensions.test_builtins_.MyPyClass) -> test_amulet_pybind11_extensions.test_builtins_.MyPyClass",
            func2.__doc__.strip(),
        )
        self.assertEqual(
            "func3(arg0: test_amulet_pybind11_extensions.test_builtins_.MyPyClass) -> test_amulet_pybind11_extensions.test_builtins_.MyPyClass",
            func3.__doc__.strip(),
        )


if __name__ == "__main__":
    unittest.main()
