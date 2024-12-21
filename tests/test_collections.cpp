#include <iostream>
#include <string>

#include <pybind11/pybind11.h>

#include <pybind11_extensions/collections.hpp>

namespace py = pybind11;

#undef NDEBUG

class IterTest {
public:
    int value;
    IterTest(int value)
        : value(value)
    {
    }
};

PYBIND11_MODULE(collections, m)
{
    m.def("test_iter_obj", [](pybind11_extensions::Iterable<py::object> iterable) {
        for (const py::object& obj : iterable) {
            std::cout << obj.attr("__repr__")().cast<std::string>() << std::endl;
        }
        return iterable;
    });
    m.def("test_iter_int", [](pybind11_extensions::Iterable<int> iterable) {
        for (const int& obj : iterable) {
            std::cout << obj << std::endl;
        }
        return iterable;
        });
    py::class_<IterTest> PyIterTest(m, "IterTest");
    PyIterTest.def(py::init<int>());
    PyIterTest.def_readwrite("value", &IterTest::value);
    m.def("test_iter_cls", [](pybind11_extensions::Iterable<IterTest> iterable) {
        for (const IterTest& obj : iterable) {
            std::cout << obj.value << std::endl;
        }
        auto it = iterable.begin();
        assert((*it).value == 1);
        assert(it->value == 1);
        it++;
        assert((*it).value == 2);
        assert(it->value == 2);
        ++it;
        assert((*it).value == 3);
        assert(it->value == 3);
        assert(it == iterable.end());
        return iterable;
        });
}
