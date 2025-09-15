#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/py_module.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

void init_test_py_module(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_py_module__");

    pyext::def_subpackage(py::module::import("test_amulet_pybind11_extensions.test_py_module_"), "sub");
}
