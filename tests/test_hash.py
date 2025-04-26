from unittest import TestCase


class PyModuleTestCase(TestCase):
    def test_iterator(self) -> None:
        from _test_hash import TestHashIdentity, TestUnhashable

        obj = TestHashIdentity()
        self.assertEqual(id(obj), hash(obj))

        with self.assertRaises(TypeError) as exception_context:
            hash(TestUnhashable())
        self.assertEqual(("unhashable type: 'TestUnhashable'",), exception_context.exception.args)
