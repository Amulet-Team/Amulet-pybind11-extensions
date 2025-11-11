import unittest
from collections.abc import Sequence, MutableSequence
from weakref import ref

from test_amulet_pybind11_extensions.test_mutable_sequence_ import TestMutableSequence


class SequenceTestCase(unittest.TestCase):
    def test_getitem(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertEqual(1, sequence[0])
        self.assertEqual(2, sequence[1])
        self.assertEqual(3, sequence[2])
        self.assertEqual(4, sequence[3])
        self.assertEqual(5, sequence[4])

        with self.assertRaises(IndexError):
            _ = sequence[5]

        with self.assertRaises(IndexError):
            _ = sequence[-6]

    def test_getitem_slice(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], sequence[:])
        self.assertEqual([2, 3, 4], sequence[1:-1])
        self.assertEqual([1, 2, 3, 4], sequence[:-1])
        self.assertEqual([2, 3, 4, 5], sequence[1:])
        self.assertEqual([4, 5], sequence[-2:])
        self.assertEqual([1, 2], sequence[:2])
        self.assertEqual([], sequence[10:])
        self.assertEqual([], sequence[:-10])

    def test_setitem(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        for i in range(5):
            sequence[i] = i + 6
        self.assertEqual([6, 7, 8, 9, 10], list(sequence))

        with self.assertRaises(IndexError):
            sequence[10] = 0

        with self.assertRaises(IndexError):
            sequence[-10] = 0

        self.assertEqual([6, 7, 8, 9, 10], list(sequence))

    def test_delitem(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        del sequence[2]
        self.assertEqual([1, 2, 4, 5], list(sequence))
        del sequence[-2]
        self.assertEqual([1, 2, 5], list(sequence))

        with self.assertRaises(IndexError):
            del sequence[10]

        with self.assertRaises(IndexError):
            del sequence[-10]

    def test_len(self) -> None:
        sequence_1 = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertEqual(5, len(sequence_1))
        sequence_2 = TestMutableSequence([3, 4, 5])
        self.assertEqual(3, len(sequence_2))

    def test_insert(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.insert(2, 6)
        self.assertEqual([1, 2, 6, 3, 4, 5], list(sequence))
        sequence.insert(-2, 7)
        self.assertEqual([1, 2, 6, 3, 7, 4, 5], list(sequence))
        sequence.insert(10, 8)
        self.assertEqual([1, 2, 6, 3, 7, 4, 5, 8], list(sequence))
        sequence.insert(-10, 9)
        self.assertEqual([9, 1, 2, 6, 3, 7, 4, 5, 8], list(sequence))

    def test_contains(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertIn(3, sequence)
        self.assertNotIn(6, sequence)
        self.assertNotIn(-6, sequence)

    def test_iter(self) -> None:
        sequence = TestMutableSequence([0, 1, 2, 3, 4])
        it = iter(sequence)
        self.assertEqual(0, next(it))
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(4, next(it))
        with self.assertRaises(StopIteration):
            next(it)

        # test lifespan
        sequence_ref = ref(sequence)
        del sequence
        self.assertIsNotNone(sequence_ref())

    def test_reversed(self) -> None:
        sequence = TestMutableSequence([0, 1, 2, 3, 4])
        it = reversed(sequence)
        self.assertEqual(4, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(1, next(it))
        self.assertEqual(0, next(it))
        with self.assertRaises(StopIteration):
            next(it)

        # test lifespan
        sequence_ref = ref(sequence)
        del sequence
        self.assertIsNotNone(sequence_ref())

    def test_index(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertEqual(2, sequence.index(3))

        with self.assertRaises(ValueError):
            sequence.index(6)

    def test_count(self) -> None:
        sequence = TestMutableSequence([1, 1, 1, 2, 2])
        self.assertEqual(3, sequence.count(1))
        self.assertEqual(2, sequence.count(2))
        self.assertEqual(0, sequence.count(3))

    def test_append(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.append(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], list(sequence))

    def test_clear(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.clear()
        self.assertEqual(0, len(sequence))

    def test_reverse(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.reverse()
        self.assertEqual([5, 4, 3, 2, 1], list(sequence))

    def test_extend(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.extend([6, 7, 8, 9, 10])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], list(sequence))
        sequence.extend(sequence)
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            list(sequence),
        )

    def test_pop(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence.pop()
        self.assertEqual([1, 2, 3, 4], list(sequence))
        sequence.pop(1)
        self.assertEqual([1, 3, 4], list(sequence))
        sequence.pop(-2)
        self.assertEqual([1, 4], list(sequence))

    def test_remove(self) -> None:
        sequence = TestMutableSequence([1, 2, 1, 2])
        sequence.remove(1)
        self.assertEqual([2, 1, 2], list(sequence))
        sequence.remove(1)
        self.assertEqual([2, 2], list(sequence))

    def test_iadd(self) -> None:
        sequence_ = sequence = TestMutableSequence([1, 2, 3, 4, 5])
        sequence += [6, 7]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], list(sequence))
        self.assertIs(sequence_, sequence)

    def test_register(self) -> None:
        sequence = TestMutableSequence([1, 2, 3, 4, 5])
        self.assertIsInstance(sequence, Sequence)
        self.assertIsInstance(sequence, MutableSequence)

    def test_make_mutable_sequence(self) -> None:
        from test_amulet_pybind11_extensions.test_mutable_sequence_ import get_mutable_sequence

        sequence = get_mutable_sequence()
        self.assertIsInstance(sequence, Sequence)
        self.assertIsInstance(sequence, MutableSequence)
        self.assertEqual([1, 2, 3], list(sequence))
        self.assertEqual(1, sequence[0])
        self.assertEqual(2, sequence[1])
        self.assertEqual(3, sequence[2])
        self.assertEqual(1, sequence[-3])
        self.assertEqual(2, sequence[-2])
        self.assertEqual(3, sequence[-1])
        with self.assertRaises(IndexError):
            sequence[-4]
        with self.assertRaises(IndexError):
            sequence[3]

        sequence[0] = 10
        sequence[1] = 20
        sequence[2] = 30
        self.assertEqual([10, 20, 30], list(sequence))
        self.assertEqual([10, 20, 30], list(get_mutable_sequence()))


if __name__ == "__main__":
    unittest.main()
