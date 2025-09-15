import unittest


class HashTestCase(unittest.TestCase):
    def test_hash(self) -> None:
        from test_amulet_pybind11_extensions.test_hash_ import TestHashIdentity, TestUnhashable

        obj = TestHashIdentity()
        self.assertEqual(id(obj), hash(obj))

        with self.assertRaises(TypeError) as exception_context:
            hash(TestUnhashable())
        self.assertEqual(
            ("unhashable type: 'TestUnhashable'",), exception_context.exception.args
        )


if __name__ == "__main__":
    unittest.main()
