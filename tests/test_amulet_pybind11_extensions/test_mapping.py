import unittest
from collections.abc import Mapping
from weakref import ref


class MappingTestCase(unittest.TestCase):
    def test_mapping(self) -> None:
        from test_amulet_pybind11_extensions.test_mapping_ import TestMapping

        mapping = TestMapping({1: 2, 3: 4, 5: 6})

        self.assertEqual(2, mapping[1])
        self.assertEqual(4, mapping[3])
        self.assertEqual(6, mapping[5])
        with self.assertRaises(KeyError):
            _ = mapping[0]

        self.assertEqual(3, len(mapping))

        it = iter(mapping)
        self.assertEqual(1, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(5, next(it))
        with self.assertRaises(StopIteration):
            next(it)

        self.assertEqual("{1: 2, 3: 4, 5: 6}", repr(mapping))

        self.assertNotIn(0, mapping)
        self.assertIn(1, mapping)
        self.assertNotIn(2, mapping)
        self.assertIn(3, mapping)
        self.assertNotIn(4, mapping)
        self.assertIn(5, mapping)
        self.assertNotIn(6, mapping)

        self.assertEqual({1, 3, 5}, mapping.keys())
        self.assertEqual({2, 4, 6}, set(mapping.values()))
        self.assertEqual({(1, 2), (3, 4), (5, 6)}, set(mapping.items()))

        self.assertIsNone(mapping.get(0))
        self.assertEqual(2, mapping.get(1))
        self.assertIsNone(mapping.get(2))
        self.assertEqual(4, mapping.get(3))
        self.assertIsNone(mapping.get(4))
        self.assertEqual(6, mapping.get(5))
        self.assertIsNone(mapping.get(6))
        self.assertEqual("hello world", mapping.get(6, "hello world"))

        self.assertEqual(
            TestMapping({1: 2, 3: 4, 5: 6}), TestMapping({1: 2, 3: 4, 5: 6})
        )
        self.assertNotEqual(
            TestMapping({1: 2, 3: 4, 5: 6}), TestMapping({1: 2, 3: 4, 5: 7})
        )
        self.assertNotEqual(TestMapping({1: 2, 3: 4, 5: 6}), TestMapping({}))
        self.assertNotEqual(TestMapping({}), TestMapping({1: 2, 3: 4, 5: 7}))

        with self.assertRaises(TypeError):
            hash(mapping)

        self.assertIsInstance(mapping, Mapping)

    def test_iter_lifespan(self) -> None:
        from test_amulet_pybind11_extensions.test_mapping_ import TestMapping

        mapping = TestMapping({1: 2, 3: 4, 5: 6})
        it = iter(mapping)
        mapping_ref = ref(mapping)
        del mapping
        self.assertIsNotNone(mapping_ref())

    def test_make_mapping(self):
        from test_amulet_pybind11_extensions.test_mapping_ import (
            get_global_int_map,
            make_int_int_map,
            make_str_int_map,
        )

        m = get_global_int_map()
        self.assertEqual(20, m[10])
        self.assertEqual(40, m[30])
        self.assertEqual(60, m[50])
        it = iter(m)
        self.assertEqual(10, next(it))
        self.assertEqual(30, next(it))
        self.assertEqual(50, next(it))
        with self.assertRaises(StopIteration):
            next(it)
        self.assertEqual(3, len(m))
        self.assertIn(10, m)
        self.assertNotIn(20, m)
        self.assertIn(30, m)
        self.assertNotIn(40, m)
        self.assertIn(50, m)
        self.assertNotIn(60, m)

        m = make_int_int_map()
        self.assertEqual(2, m[1])
        self.assertEqual(4, m[3])
        self.assertEqual(6, m[5])
        it = iter(m)
        self.assertEqual(1, next(it))
        self.assertEqual(3, next(it))
        self.assertEqual(5, next(it))
        with self.assertRaises(StopIteration):
            next(it)
        self.assertEqual(3, len(m))
        self.assertIn(1, m)
        self.assertNotIn(2, m)
        self.assertIn(3, m)
        self.assertNotIn(4, m)
        self.assertIn(5, m)
        self.assertNotIn(6, m)

        m = make_str_int_map()
        self.assertEqual(2, m["1"])
        self.assertEqual(4, m["3"])
        self.assertEqual(6, m["5"])
        it = iter(m)
        self.assertEqual("1", next(it))
        self.assertEqual("3", next(it))
        self.assertEqual("5", next(it))
        with self.assertRaises(StopIteration):
            next(it)
        self.assertEqual(3, len(m))
        self.assertIn("1", m)
        self.assertNotIn("2", m)
        self.assertIn("3", m)
        self.assertNotIn("4", m)
        self.assertIn("5", m)
        self.assertNotIn("6", m)

    def test_make_mapping_lifespan(self) -> None:
        from test_amulet_pybind11_extensions.test_mapping_ import (
            get_global_int_map,
            make_int_int_map,
            make_str_int_map,
        )

        m = get_global_int_map()
        m_ref = ref(m)
        it = iter(m)
        del m
        self.assertIsNotNone(m_ref())
        self.assertEqual(10, next(it))

        m = make_int_int_map()
        m_ref = ref(m)
        it = iter(m)
        del m
        self.assertIsNotNone(m_ref())
        self.assertEqual(1, next(it))

        m = make_str_int_map()
        m_ref = ref(m)
        it = iter(m)
        del m
        self.assertIsNotNone(m_ref())
        self.assertEqual("1", next(it))


if __name__ == "__main__":
    unittest.main()
