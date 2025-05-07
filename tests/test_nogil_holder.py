import unittest
from weakref import ref


class NoGILHolderTestCase(unittest.TestCase):
    def test_nogil_holder(self) -> None:
        from _test_nogil_holder import Bool, NoGILHolderTestClass

        b = Bool(True)
        self.assertTrue(b)
        cls = NoGILHolderTestClass(b)
        cls_ref = ref(cls)
        del cls
        self.assertFalse(b)
        self.assertIsNone(cls_ref())


if __name__ == "__main__":
    unittest.main()
