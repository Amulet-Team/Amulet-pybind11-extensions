#include <pybind11/pybind11.h>

#include <iostream>

#include <amulet/pybind11_extensions/pybind11.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class MyIterator {
public:
    int next()
    {
        return 1;
    }
};

PYBIND11_MODULE(_test_pybind11, m)
{
    m.def("get_iterator", []() { return pyext::make_iterator(MyIterator()); });
}
