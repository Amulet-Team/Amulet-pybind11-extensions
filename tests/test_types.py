import unittest
from types import NotImplementedType


class TypesTestCase(unittest.TestCase):
    def test_types(self) -> None:
        from _test_types import func

        self.assertEqual(
            "func() -> types.NotImplementedType",
            func.__doc__.strip(),
        )
        self.assertIs(NotImplementedType, func())


if __name__ == "__main__":
    unittest.main()
