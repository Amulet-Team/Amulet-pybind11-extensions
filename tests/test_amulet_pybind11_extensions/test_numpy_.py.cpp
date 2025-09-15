#include <pybind11/pybind11.h>

#include <cstdint>

#include <amulet/pybind11_extensions/numpy.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

void init_test_numpy(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_numpy_");

    m.def("func_uint8", [](pyext::numpy::array_t<std::uint8_t>) { });
    m.def("func_uint16", [](pyext::numpy::array_t<std::uint16_t>) { });
    m.def("func_uint32", [](pyext::numpy::array_t<std::uint32_t>) { });
    m.def("func_uint64", [](pyext::numpy::array_t<std::uint64_t>) { });
    m.def("func_int8", [](pyext::numpy::array_t<std::int8_t>) { });
    m.def("func_int16", [](pyext::numpy::array_t<std::int16_t>) { });
    m.def("func_int32", [](pyext::numpy::array_t<std::int32_t>) { });
    m.def("func_int64", [](pyext::numpy::array_t<std::int64_t>) { });
    m.def("func_float", [](pyext::numpy::array_t<float>) { });
    m.def("func_double", [](pyext::numpy::array_t<double>) { });
}
