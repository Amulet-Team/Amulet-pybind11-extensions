import unittest
from collections.abc import Mapping, MutableMapping
from weakref import ref


class MutableMappingTestCase(unittest.TestCase):
    def test_mutable_mapping(self) -> None:
        from _test_mutable_mapping import TestMutableMapping

        mapping = TestMutableMapping({"1": 2, "3": 4, "5": 6})

        self.assertEqual(2, mapping["1"])
        self.assertEqual(4, mapping["3"])
        self.assertEqual(6, mapping["5"])
        with self.assertRaises(KeyError):
            _ = mapping["0"]

        self.assertEqual(3, len(mapping))

        it = iter(mapping)
        self.assertEqual("1", next(it))
        self.assertEqual("3", next(it))
        self.assertEqual("5", next(it))
        with self.assertRaises(StopIteration):
            next(it)

        self.assertEqual("{'1': 2, '3': 4, '5': 6}", repr(mapping))

        self.assertNotIn("0", mapping)
        self.assertIn("1", mapping)
        self.assertNotIn("2", mapping)
        self.assertIn("3", mapping)
        self.assertNotIn("4", mapping)
        self.assertIn("5", mapping)
        self.assertNotIn("6", mapping)

        self.assertEqual({"1", "3", "5"}, mapping.keys())
        self.assertEqual({2, 4, 6}, set(mapping.values()))
        self.assertEqual({("1", 2), ("3", 4), ("5", 6)}, set(mapping.items()))

        self.assertIsNone(mapping.get("0"))
        self.assertEqual(2, mapping.get("1"))
        self.assertIsNone(mapping.get("2"))
        self.assertEqual(4, mapping.get("3"))
        self.assertIsNone(mapping.get("4"))
        self.assertEqual(6, mapping.get("5"))
        self.assertIsNone(mapping.get("6"))
        self.assertEqual("hello world", mapping.get("6", "hello world"))

        self.assertEqual(
            TestMutableMapping({"1": 2, "3": 4, "5": 6}),
            TestMutableMapping({"1": 2, "3": 4, "5": 6}),
        )
        self.assertNotEqual(
            TestMutableMapping({"1": 2, "3": 4, "5": 6}),
            TestMutableMapping({"1": 2, "3": 4, "5": 7}),
        )
        self.assertNotEqual(
            TestMutableMapping({"1": 2, "3": 4, "5": 6}), TestMutableMapping({})
        )
        self.assertNotEqual(
            TestMutableMapping({}), TestMutableMapping({"1": 2, "3": 4, "5": 7})
        )

        with self.assertRaises(TypeError):
            hash(mapping)

        self.assertIsInstance(mapping, Mapping)
        self.assertIsInstance(mapping, MutableMapping)

        mapping["7"] = 8
        self.assertEqual(TestMutableMapping({"1": 2, "3": 4, "5": 6, "7": 8}), mapping)
        self.assertEqual(8, mapping["7"])
        del mapping["7"]
        self.assertEqual(TestMutableMapping({"1": 2, "3": 4, "5": 6}), mapping)

        with self.assertRaises(KeyError):
            mapping.pop("0")
        self.assertEqual("hello world", mapping.pop("0", "hello world"))
        self.assertEqual(2, mapping.pop("1"))
        self.assertEqual(TestMutableMapping({"3": 4, "5": 6}), mapping)
        self.assertEqual(6, mapping.pop("5"))
        self.assertEqual(TestMutableMapping({"3": 4}), mapping)
        self.assertEqual(("3", 4), mapping.popitem())
        with self.assertRaises(KeyError):
            mapping.popitem()

        mapping = TestMutableMapping({"1": 2, "3": 4, "5": 6})
        mapping.clear()
        self.assertEqual(TestMutableMapping({}), mapping)

        mapping.update({"10": 20}, a=15)
        mapping.update([("30", 40)], b=35)
        self.assertEqual(
            TestMutableMapping({"10": 20, "30": 40, "a": 15, "b": 35}), mapping
        )
        mapping.update({"10": 21}, a=16)
        mapping.update([("30", 41)], b=36)
        self.assertEqual(
            TestMutableMapping({"10": 21, "30": 41, "a": 16, "b": 36}), mapping
        )

        mapping.setdefault("10", 22)
        mapping.setdefault("11", 11)
        self.assertEqual(
            TestMutableMapping({"10": 21, "30": 41, "a": 16, "b": 36, "11": 11}),
            mapping,
        )

    def test_iter_lifespan(self) -> None:
        from _test_mutable_mapping import TestMutableMapping

        mapping = TestMutableMapping({"1": 2, "3": 4, "5": 6})
        it = iter(mapping)
        mapping_ref = ref(mapping)
        del mapping
        self.assertIsNotNone(mapping_ref())


if __name__ == "__main__":
    unittest.main()
