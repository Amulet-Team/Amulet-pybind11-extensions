#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/sequence.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestSequence {
public:
    int get(int index)
    {
        return index;
    }
    size_t size()
    {
        return 5;
    }
};
}

void init_test_sequence(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_sequence_");

    py::class_<detail::TestSequence> TestSequence(m, "TestSequence");
    TestSequence.def(py::init());
    TestSequence.def("__getitem__", &detail::TestSequence::get);
    TestSequence.def("__len__", &detail::TestSequence::size);
    pyext::collections::def_Sequence_getitem_slice(TestSequence);
    pyext::collections::def_Sequence_contains(TestSequence);
    pyext::collections::def_Sequence_iter(TestSequence);
    pyext::collections::def_Sequence_reversed(TestSequence);
    pyext::collections::def_Sequence_index(TestSequence);
    pyext::collections::def_Sequence_count(TestSequence);
    pyext::collections::register_Sequence(TestSequence);
}
