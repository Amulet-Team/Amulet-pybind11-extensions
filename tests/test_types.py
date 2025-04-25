from unittest import TestCase
from types import NotImplementedType


class PyModuleTestCase(TestCase):
    def test_iterator(self) -> None:
        from _test_types import func

        self.assertEqual(
            "func() -> types.NotImplementedType",
            func.__doc__.strip(),
        )
        self.assertIs(NotImplementedType, func())
