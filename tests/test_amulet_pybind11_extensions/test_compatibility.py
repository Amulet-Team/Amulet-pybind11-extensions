import unittest


class CompatibilityTestCase(unittest.TestCase):
    def test_compatibility(self) -> None:
        import test_amulet_pybind11_extensions.test_compatibility_2_
        import test_amulet_pybind11_extensions.test_compatibility_1_

        compiler_config_1 = test_amulet_pybind11_extensions.test_compatibility_1_.compiler_config
        self.assertIsInstance(compiler_config_1, dict)
        self.assertIsInstance(compiler_config_1["pybind11_version"], str)
        self.assertIsInstance(compiler_config_1["compiler_id"], str)
        self.assertIsInstance(compiler_config_1["compiler_version"], str)

        compiler_config_2 = test_amulet_pybind11_extensions.test_compatibility_2_.compiler_config
        self.assertIsInstance(compiler_config_2, dict)
        self.assertIsInstance(compiler_config_2["pybind11_version"], str)
        self.assertIsInstance(compiler_config_2["compiler_id"], str)
        self.assertIsInstance(compiler_config_2["compiler_version"], str)


if __name__ == "__main__":
    unittest.main()
