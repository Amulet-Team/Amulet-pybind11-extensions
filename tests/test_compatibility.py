from unittest import TestCase

class CompatibilityTestCase(TestCase):
    def test_compatibility(self) -> None:
        import _test_compatibility_2
        import _test_compatibility_1

        compiler_config_1 = _test_compatibility_1.compiler_config
        self.assertIsInstance(compiler_config_1, dict)
        self.assertIsInstance(compiler_config_1["pybind11_version"], str)
        self.assertIsInstance(compiler_config_1["compiler_id"], str)
        self.assertIsInstance(compiler_config_1["compiler_version"], str)

        compiler_config_2 = _test_compatibility_2.compiler_config
        self.assertIsInstance(compiler_config_2, dict)
        self.assertIsInstance(compiler_config_2["pybind11_version"], str)
        self.assertIsInstance(compiler_config_2["compiler_id"], str)
        self.assertIsInstance(compiler_config_2["compiler_version"], str)
