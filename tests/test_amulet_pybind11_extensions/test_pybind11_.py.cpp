#include <pybind11/pybind11.h>

#include <stdexcept>

#include <amulet/pybind11_extensions/pybind11.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class RefTest { };
}

void init_test_pybind11(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_pybind11_");

    if (pyext::is_class_bound<detail::RefTest>()) {
        throw std::runtime_error("RefTest has not been bound yet but is_class_bound thinks it has.");
    }
    py::class_<detail::RefTest>(m, "RefTest");
    if (!pyext::is_class_bound<detail::RefTest>()) {
        throw std::runtime_error("RefTest has been bound but is_class_bound thinks it has not.");
    }
    m.def("get_keep_alive", []() {
        py::object a = py::cast(detail::RefTest());
        py::object b = py::cast(detail::RefTest());
        pyext::keep_alive(a, b);
        return py::make_tuple(a, b);
    });
}
