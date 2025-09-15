#include <pybind11/pybind11.h>

#include <stdexcept>

#include <amulet/pybind11_extensions/nogil_holder.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class NoGILHolderTestClass {
private:
    bool& gil_held;

public:
    NoGILHolderTestClass(bool& gil_held)
        : gil_held(gil_held)
    {
    }
    ~NoGILHolderTestClass()
    {
        gil_held = PyGILState_Check();
    }
};

class Bool {
public:
    bool value;

    Bool(bool value)
        : value(value)
    {
    }

    operator bool()
    {
        return value;
    }
};

void init_test_nogil_holder(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_nogil_holder_");

    py::class_<Bool>(m, "Bool")
        .def(py::init<bool>())
        .def("__bool__", &Bool::operator bool);
    py::class_<NoGILHolderTestClass, pyext::nogil_shared_ptr<NoGILHolderTestClass>>(m, "NoGILHolderTestClass")
        .def(py::init([](Bool& b) { return NoGILHolderTestClass(b.value); }));
}
