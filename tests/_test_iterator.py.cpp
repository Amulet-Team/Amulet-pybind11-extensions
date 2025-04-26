#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/iterator.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class MyIterator {
public:
    int next()
    {
        return 1;
    }
};

PYBIND11_MODULE(_test_iterator, m)
{
    m.def("get_iterator", []() { return pyext::make_iterator(MyIterator()); });
}
