import unittest
from types import ModuleType
import os


class PyModuleTestCase(unittest.TestCase):
    def test_py_module(self) -> None:
        import _test_py_module.sub

        self.assertIsInstance(_test_py_module.sub, ModuleType)
        self.assertIsInstance(_test_py_module.sub.__path__, list)
        self.assertEqual(
            [os.path.join(_test_py_module.__path__[0], "sub")],
            _test_py_module.sub.__path__,
        )


if __name__ == "__main__":
    unittest.main()
