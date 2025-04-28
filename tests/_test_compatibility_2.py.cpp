#include <pybind11/pybind11.h>
#include <amulet/pybind11_extensions/compatibility.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

PYBIND11_MODULE(_test_compatibility_2, m)
{
    pyext::init_compiler_config(m);
    auto test_compatibility_1 = py::module::import("_test_compatibility_1");
    pyext::check_compatibility(m, test_compatibility_1);
}
