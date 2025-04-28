#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/py_module.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

PYBIND11_MODULE(_test_py_module_, m)
{
    pyext::def_subpackage(py::module::import("_test_py_module"), "sub");
}
