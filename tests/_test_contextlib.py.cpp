#include <pybind11/pybind11.h>

#include <string>
#include <optional>

#include <amulet/pybind11_extensions/contextlib.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

PYBIND11_MODULE(_test_contextlib, m)
{
    m.attr("state") = 0;
    m.def("func", [m]() {
        return pyext::contextlib::make_context_manager<std::string, std::optional<bool>>(
            [m]() -> std::string { 
                m.attr("state") = 1;
                return "hello world"; 
            },
            [m](py::object, py::object, py::object) -> std::optional<bool> {
                m.attr("state") = 0;
                return false;
            }
        );
    });
    m.def("suppress", [m]() {
        return pyext::contextlib::make_context_manager<void, std::optional<bool>>(
            [](){},
            [](py::object, py::object, py::object) -> std::optional<bool> {
                return true;
            }
        );
    });
}
