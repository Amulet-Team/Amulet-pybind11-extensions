#include <pybind11/pybind11.h>

#include <pybind11/operators.h>

#include <iostream>
#include <stdexcept>
#include <string>

#include <amulet/pybind11_extensions/collections.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class TestToken {
public:
    int value;
    TestToken(int value)
        : value(value)
    {
    }
    bool operator==(const TestToken& other) const
    {
        return value == other.value;
    }
};

#define ENSURE(condition)                \
    if (!(condition)) {                  \
        std::string msg;                 \
        msg.reserve(200);                \
        msg += "Test failed in file ";   \
        msg += __FILE__;                 \
        msg += " at line ";              \
        msg += std::to_string(__LINE__); \
        msg += ". ";                     \
        msg += #condition;               \
        throw std::runtime_error(msg);   \
    }

PYBIND11_MODULE(_test_collections, m)
{
    py::class_<TestToken> PyTestToken(m, "TestToken");
    PyTestToken.def(py::init<int>());
    PyTestToken.def_readwrite("value", &TestToken::value);
    PyTestToken.def(py::self == py::self);
    auto PyId = py::module::import("builtins").attr("id");
    PyTestToken.def("__hash__", [PyId](py::object self) -> py::int_ { return PyId(self); });

    m.def("test_iterator_obj", [](pyext::collections::Iterator<py::object> iterator, py::list objs) {
        for (; iterator != iterator.sentinel(); iterator++) {
            objs.append(*iterator);
        }
        return iterator;
    });
    m.def("test_iterator_int", [](pyext::collections::Iterator<int> iterator, py::list objs) {
        for (; iterator != iterator.sentinel(); iterator++) {
            objs.append(*iterator);
        }
        return iterator;
    });
    m.def("test_iterator_cls", [](pyext::collections::Iterator<TestToken> iterator, py::list objs) {
        for (; iterator != iterator.sentinel(); iterator++) {
            objs.append(*iterator);
        }
        return iterator;
    });
    m.def("test_iterable_obj", [](pyext::collections::Iterable<py::object> iterable, py::list objs) {
        for (const py::object& obj : iterable) {
            objs.append(obj);
        }
        auto it = iterable.begin();
        ENSURE((*it).is_none())
        ENSURE(it->is_none())
        ENSURE(it != iterable.end())
        it++;
        ENSURE(py::isinstance<py::int_>(*it))
        ENSURE(it->cast<int>() == 1)
        ENSURE(it != iterable.end())
        ++it;
        ENSURE(py::isinstance<py::str>(*it))
        ENSURE(it->cast<std::string>() == "2")
        ENSURE(it != iterable.end())
        it++;
        ENSURE(py::isinstance<py::float_>(*it))
        ENSURE(it->cast<float>() == 3.0)
        ENSURE(it != iterable.end())
        ++it;
        ENSURE(it == iterable.end())
        return iterable;
    });

    m.def("test_iterable_int", [](pyext::collections::Iterable<int> iterable, py::list objs) {
        for (const int& obj : iterable) {
            objs.append(obj);
        }
        auto it = iterable.begin();
        ENSURE(*it == 1)
        ENSURE(it != iterable.end())
        it++;
        ENSURE(*it == 2)
        ENSURE(it != iterable.end())
        ++it;
        ENSURE(*it == 3)
        ENSURE(it != iterable.end())
        it++;
        ENSURE(it == iterable.end())
        return iterable;
    });

    m.def("test_iterable_cls", [](pyext::collections::Iterable<TestToken> iterable, py::list objs) {
        for (const TestToken& obj : iterable) {
            objs.append(obj);
        }
        auto it = iterable.begin();
        ENSURE((*it).value == 1)
        ENSURE(it->value == 1)
        ENSURE(it != iterable.end())
        it++;
        ENSURE((*it).value == 2)
        ENSURE(it->value == 2)
        ENSURE(it != iterable.end())
        ++it;
        ENSURE((*it).value == 3)
        ENSURE(it->value == 3)
        ENSURE(it != iterable.end())
        it++;
        ENSURE(it == iterable.end())
        return iterable;
    });

    m.def("test_sequence_obj", [](pyext::collections::Sequence<py::object> obj) { return obj; });
    m.def("test_sequence_int", [](pyext::collections::Sequence<int> obj) { return obj; });
    m.def("test_sequence_cls", [](pyext::collections::Sequence<TestToken> obj) { return obj; });
    
    m.def("test_map_obj", [](pyext::collections::Mapping<int, py::object> obj) { return obj; });
    m.def("test_map_int", [](pyext::collections::Mapping<int, int> obj) { return obj; });
    m.def("test_map_cls", [](pyext::collections::Mapping<int, TestToken> obj) { return obj; });

    m.def("test_mutable_map_obj", [](pyext::collections::MutableMapping<int, py::object> obj) { return obj; });
    m.def("test_mutable_map_int", [](pyext::collections::MutableMapping<int, int> obj) { return obj; });
    m.def("test_mutable_map_cls", [](pyext::collections::MutableMapping<int, TestToken> obj) { return obj; });

    m.def("test_keys_view_obj", [](pyext::collections::KeysView<py::object> obj) { return obj; });
    m.def("test_keys_view_int", [](pyext::collections::KeysView<int> obj) { return obj; });
    m.def("test_keys_view_cls", [](pyext::collections::KeysView<TestToken> obj) { return obj; });

    m.def("test_values_view_obj", [](pyext::collections::ValuesView<py::object> obj) { return obj; });
    m.def("test_values_view_int", [](pyext::collections::ValuesView<int> obj) { return obj; });
    m.def("test_values_view_cls", [](pyext::collections::ValuesView<TestToken> obj) { return obj; });

    m.def("test_items_view_obj", [](pyext::collections::ItemsView<int, py::object> obj) { return obj; });
    m.def("test_items_view_int", [](pyext::collections::ItemsView<int, int> obj) { return obj; });
    m.def("test_items_view_cls", [](pyext::collections::ItemsView<int, TestToken> obj) { return obj; });
}
