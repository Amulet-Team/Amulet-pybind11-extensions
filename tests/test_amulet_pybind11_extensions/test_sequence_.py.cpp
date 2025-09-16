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
    using Sequence = pyext::collections::Sequence<int>;
    Sequence::def_getitem_slice(TestSequence);
    Sequence::def_contains(TestSequence);
    Sequence::def_iter(TestSequence);
    Sequence::def_reversed(TestSequence);
    Sequence::def_index(TestSequence);
    Sequence::def_count(TestSequence);
    Sequence::register_cls(TestSequence);
}
