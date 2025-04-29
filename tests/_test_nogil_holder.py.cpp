#include <pybind11/pybind11.h>

#include <stdexcept>

#include <amulet/pybind11_extensions/nogil_holder.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class NoGILHolderTestClass {
public:
    NoGILHolderTestClass() { }
    ~NoGILHolderTestClass() {
        if (PyGILState_Check()) {
            throw std::runtime_error("GIL should not be held here.");
        }
    }
};

PYBIND11_MODULE(_test_nogil_holder, m)
{
    py::class_<NoGILHolderTestClass, pyext::nogil_shared_ptr<NoGILHolderTestClass>>(m, "NoGILHolderTestClass")
        .def(py::init());
}
