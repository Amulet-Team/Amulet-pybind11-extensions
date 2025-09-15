import unittest
from types import ModuleType
import os


class PyModuleTestCase(unittest.TestCase):
    def test_py_module(self) -> None:
        import test_amulet_pybind11_extensions.test_py_module_.sub

        self.assertIsInstance(test_amulet_pybind11_extensions.test_py_module_.sub, ModuleType)
        self.assertIsInstance(test_amulet_pybind11_extensions.test_py_module_.sub.__path__, list)
        self.assertEqual(
            [os.path.join(test_amulet_pybind11_extensions.test_py_module_.__path__[0], "sub")],
            test_amulet_pybind11_extensions.test_py_module_.sub.__path__,
        )


if __name__ == "__main__":
    unittest.main()
