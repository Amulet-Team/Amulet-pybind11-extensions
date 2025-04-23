#include <pybind11/pybind11.h>
#include <amulet/pybind11_extensions/compatibility.hpp>

namespace pyext = Amulet::pybind11_extensions;

PYBIND11_MODULE(_test_compatibility_1, m)
{
    pyext::init_compiler_config(m);
}
