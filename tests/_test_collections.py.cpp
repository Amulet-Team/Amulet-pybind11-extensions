#include <pybind11/pybind11.h>

#include <pybind11/operators.h>

#include <iostream>
#include <stdexcept>
#include <string>

#include <amulet/pybind11_extensions/collections.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class IterTest {
public:
    int value;
    IterTest(int value)
        : value(value)
    {
    }
    bool operator==(const IterTest& other) const
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

    py::class_<IterTest> PyIterTest(m, "IterTest");
    PyIterTest.def(py::init<int>());
    PyIterTest.def_readwrite("value", &IterTest::value);
    PyIterTest.def(py::self == py::self);
    auto PyId = py::module::import("builtins").attr("id");
    PyIterTest.def("__hash__", [PyId](py::object self) -> py::int_ { return PyId(self); });

    m.def("test_iterable_cls", [](pyext::collections::Iterable<IterTest> iterable, py::list objs) {
        for (const IterTest& obj : iterable) {
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
}
