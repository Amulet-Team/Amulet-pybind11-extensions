import unittest
from collections.abc import Sequence


class SequenceTestCase(unittest.TestCase):
    def test_sequence(self) -> None:
        from _test_sequence import TestSequence

        sequence = TestSequence()
        self.assertEqual(5, len(sequence))

        self.assertEqual(0, sequence[0])
        self.assertEqual(1, sequence[1])
        self.assertEqual(2, sequence[2])
        self.assertEqual(3, sequence[3])
        self.assertEqual(4, sequence[4])

        self.assertEqual([2, 3], sequence[2:4])

        self.assertNotIn(-1, sequence)
        self.assertIn(0, sequence)
        self.assertIn(1, sequence)
        self.assertIn(2, sequence)
        self.assertIn(3, sequence)
        self.assertIn(4, sequence)
        self.assertNotIn(5, sequence)

        it = iter(sequence)
        self.assertEqual(0, next(it))
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(4, next(it))
        with self.assertRaises(StopIteration):
            next(it)

        it = reversed(sequence)
        self.assertEqual(4, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(1, next(it))
        self.assertEqual(0, next(it))
        with self.assertRaises(StopIteration):
            next(it)

        self.assertEqual(0, sequence.index(0))
        self.assertEqual(1, sequence.index(1))
        self.assertEqual(2, sequence.index(2))
        self.assertEqual(3, sequence.index(3))
        self.assertEqual(4, sequence.index(4))

        self.assertEqual(0, sequence.count(-1))
        self.assertEqual(1, sequence.count(0))
        self.assertEqual(1, sequence.count(1))
        self.assertEqual(1, sequence.count(2))
        self.assertEqual(1, sequence.count(3))
        self.assertEqual(1, sequence.count(4))
        self.assertEqual(0, sequence.count(5))

        self.assertIsInstance(sequence, Sequence)


if __name__ == "__main__":
    unittest.main()
