#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/types.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

void init_test_types(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_types_");

    m.def("func", []() -> pyext::types::NotImplementedType {
        return py::module::import("types").attr("NotImplementedType");
    });
}
