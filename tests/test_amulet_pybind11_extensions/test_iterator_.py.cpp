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

void init_test_iterator(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_iterator_");

    m.def("get_iterator", []() { return pyext::make_iterator(MyIterator()); });
}
