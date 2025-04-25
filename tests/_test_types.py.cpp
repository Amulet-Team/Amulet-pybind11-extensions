#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/types.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

PYBIND11_MODULE(_test_types, m)
{
    m.def("func", []() -> pyext::types::NotImplementedType {
        return py::module::import("types").attr("NotImplementedType");
    });
}
