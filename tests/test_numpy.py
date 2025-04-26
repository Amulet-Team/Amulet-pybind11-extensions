import unittest

from _test_numpy import (
    func_uint8,
    func_uint16,
    func_uint32,
    func_uint64,
    func_int8,
    func_int16,
    func_int32,
    func_int64,
    func_float,
    func_double,
)


class NumpyTestCase(unittest.TestCase):
    def test_numpy(self) -> None:
        self.assertEqual(
            "func_uint8(arg0: numpy.typing.NDArray[numpy.uint8]) -> None",
            func_uint8.__doc__.strip(),
        )
        self.assertEqual(
            "func_uint16(arg0: numpy.typing.NDArray[numpy.uint16]) -> None",
            func_uint16.__doc__.strip(),
        )
        self.assertEqual(
            "func_uint32(arg0: numpy.typing.NDArray[numpy.uint32]) -> None",
            func_uint32.__doc__.strip(),
        )
        self.assertEqual(
            "func_uint64(arg0: numpy.typing.NDArray[numpy.uint64]) -> None",
            func_uint64.__doc__.strip(),
        )
        self.assertEqual(
            "func_int8(arg0: numpy.typing.NDArray[numpy.int8]) -> None",
            func_int8.__doc__.strip(),
        )
        self.assertEqual(
            "func_int16(arg0: numpy.typing.NDArray[numpy.int16]) -> None",
            func_int16.__doc__.strip(),
        )
        self.assertEqual(
            "func_int32(arg0: numpy.typing.NDArray[numpy.int32]) -> None",
            func_int32.__doc__.strip(),
        )
        self.assertEqual(
            "func_int64(arg0: numpy.typing.NDArray[numpy.int64]) -> None",
            func_int64.__doc__.strip(),
        )
        self.assertEqual(
            "func_float(arg0: numpy.typing.NDArray[numpy.float32]) -> None",
            func_float.__doc__.strip(),
        )
        self.assertEqual(
            "func_double(arg0: numpy.typing.NDArray[numpy.float64]) -> None",
            func_double.__doc__.strip(),
        )


if __name__ == "__main__":
    unittest.main()
