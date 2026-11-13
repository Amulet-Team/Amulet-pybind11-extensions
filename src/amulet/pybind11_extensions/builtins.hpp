#pragma once
#include <pybind11/detail/descr.h>
#include <pybind11/pybind11.h>

// Type hints for builtin types.

namespace Amulet {
namespace pybind11_extensions {
    // Type hint for a native python object.
    namespace detail {
        template <size_t N>
        struct FixedString {
            char buf[N + 1] { };
            constexpr FixedString(char const* s)
            {
                for (unsigned i = 0; i != N; ++i)
                    buf[i] = s[i];
            }
        };
        template <unsigned N>
        FixedString(char const (&)[N]) -> FixedString<N - 1>;
    }

    // A python object with a user defined string type hint for an arbitrary python object.
    // This is useful if a C++ function needs to interact with a native python object.
    template <detail::FixedString T>
    class PyObjectStr : public pybind11::object {
        PYBIND11_OBJECT_DEFAULT(PyObjectStr, object, PyObject_Type)
        using object::object;
    };

    // A python object with a type hint from a C++ object.
    // This is useful if you don't want to cast the python object to the C++ object and want to keep the type hint.
    template <typename cppT>
    class PyObjectCpp : public pybind11::object {
        PYBIND11_OBJECT_DEFAULT(PyObjectCpp, object, PyObject_Type)
        using object::object;
    };

    template <typename T, detail::FixedString Var = "args">
    class Args : public pybind11::args {
        using pybind11::args::args;
    };

    template <typename T, detail::FixedString Var = "kwargs">
    class KWArgs : public pybind11::kwargs {
        using pybind11::kwargs::kwargs;
    };
} // namespace pybind11_extensions
} // namespace Amulet

namespace pybind11 {
namespace detail {
    template <Amulet::pybind11_extensions::detail::FixedString T>
    struct handle_type_name<Amulet::pybind11_extensions::PyObjectStr<T>> {
        static constexpr auto name = pybind11::detail::const_name(T.buf);
    };

    template <typename cppT>
    struct handle_type_name<Amulet::pybind11_extensions::PyObjectCpp<cppT>> {
        static constexpr auto name = make_caster<cppT>::name;
    };

    template <typename T, Amulet::pybind11_extensions::detail::FixedString Var>
    struct handle_type_name<Amulet::pybind11_extensions::Args<T, Var>> {
        static constexpr auto name
            = io_name("*", "")
            + io_name(Var.buf, "")
            + io_name(": ", "tuple[")
            + make_caster<T>::name 
            + io_name("", ", ...]");
    };

    template <typename T, Amulet::pybind11_extensions::detail::FixedString Var>
    struct handle_type_name<Amulet::pybind11_extensions::KWArgs<T, Var>> {
        static constexpr auto name
            = io_name("**", "") 
            + io_name(Var.buf, "") 
            + io_name(": ", "dict[str, ") 
            + make_caster<T>::name 
            + io_name("", "]");
    };
} // namespace detail
} // namespace pybind11
