#pragma once
#include "builtins.hpp"
#include <pybind11/pybind11.h>

// This extension adds a py::object subclass for types.NotImplementedType.
// This is used as a return in comparison operators.

namespace Amulet {
namespace pybind11_extensions {
    namespace types {
        using NotImplementedType = pybind11_extensions::PyObjectStr<"types.NotImplementedType">;
    }
} // namespace pybind11_extensions
} // namespace Amulet
