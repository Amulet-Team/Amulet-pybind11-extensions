#include <iostream>
#include <stdexcept>
#include <string>

#include <pybind11/pybind11.h>

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
};

#define ENSURE(condition)                                     \
    if (!(condition)) {                                       \
        throw std::runtime_error("Test failed. " #condition); \
    }

PYBIND11_MODULE(_test_collections, m)
{
    m.def("test_iter_obj", [](pyext::collections::Iterable<py::object> iterable) {
        for (const py::object& obj : iterable) {
            std::cout << obj.attr("__repr__")().cast<std::string>() << std::endl;
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
    m.def("test_iter_int", [](pyext::collections::Iterable<int> iterable) {
        for (const int& obj : iterable) {
            std::cout << obj << std::endl;
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
    m.def("test_iter_cls", [](pyext::collections::Iterable<IterTest> iterable) {
        for (const IterTest& obj : iterable) {
            std::cout << obj.value << std::endl;
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
