#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <algorithm>
#include <vector>

#include <amulet/pybind11_extensions/mutable_sequence.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestMutableSequence {
private:
    std::vector<int> _v;

public:
    TestMutableSequence() { }
    TestMutableSequence(std::vector<int> v)
        : _v(std::move(v))
    {
    }
    int get(Py_ssize_t index) const
    {
        if (index < 0) {
            index += size();
            if (index < 0) {
                throw py::index_error("");
            }
        } else if (index >= size()) {
            throw py::index_error("");
        }
        return _v[index];
    }
    void set(Py_ssize_t index, int value)
    {
        if (index < 0) {
            index += size();
            if (index < 0) {
                throw py::index_error("");
            }
        } else if (index >= size()) {
            throw py::index_error("");
        }
        _v[index] = value;
    }
    void insert(Py_ssize_t index, int value)
    {
        if (index < 0) {
            index += size();
        }
        index = std::max(static_cast<Py_ssize_t>(0), std::min(static_cast<Py_ssize_t>(size()), index));
        _v.insert(_v.begin() + index, value);
    }
    void del(Py_ssize_t index)
    {
        if (index < 0) {
            index += size();
            if (index < 0) {
                throw py::index_error("");
            }
        } else if (index >= size()) {
            throw py::index_error("");
        }
        _v.erase(_v.begin() + index);
    }
    size_t size() const
    {
        return _v.size();
    }
};
}

void init_test_mutable_sequence(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_mutable_sequence_");

    py::class_<detail::TestMutableSequence> TestMutableSequence(m, "TestMutableSequence");
    TestMutableSequence.def(py::init());
    TestMutableSequence.def(py::init<std::vector<int>>());
    TestMutableSequence.def("__getitem__", &detail::TestMutableSequence::get);
    TestMutableSequence.def("__setitem__", &detail::TestMutableSequence::set);
    TestMutableSequence.def("__delitem__", &detail::TestMutableSequence::del);
    TestMutableSequence.def("__len__", &detail::TestMutableSequence::size);
    TestMutableSequence.def("insert", &detail::TestMutableSequence::insert);
    using Sequence = pyext::collections::MutableSequence<int>;
    Sequence::def_getitem_slice(TestMutableSequence);
    Sequence::def_contains(TestMutableSequence);
    Sequence::def_iter(TestMutableSequence);
    Sequence::def_reversed(TestMutableSequence);
    Sequence::def_index(TestMutableSequence);
    Sequence::def_count(TestMutableSequence);
    Sequence::def_append(TestMutableSequence);
    Sequence::def_clear(TestMutableSequence);
    Sequence::def_reverse(TestMutableSequence);
    Sequence::def_extend(TestMutableSequence);
    Sequence::def_pop(TestMutableSequence);
    Sequence::def_remove(TestMutableSequence);
    Sequence::def_iadd(TestMutableSequence);
    Sequence::register_cls(TestMutableSequence);
}
