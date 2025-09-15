#include <pybind11/pybind11.h>
#include <amulet/pybind11_extensions/compatibility.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

void init_test_compatibility_1(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_compatibility_1_");

    pyext::init_compiler_config(m);
}
