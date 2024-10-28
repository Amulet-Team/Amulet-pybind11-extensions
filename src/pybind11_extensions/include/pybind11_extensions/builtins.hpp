#pragma once
#include <pybind11/pybind11.h>
#include <pybind11/detail/descr.h>

// Type hints for builtin types.


namespace pybind11_extensions {
    // Type hint for a native python object.
    namespace builtins {
        namespace detail {
            template<size_t N>
            struct FixedString {
                char buf[N + 1]{};
                constexpr FixedString(char const* s) {
                    for (unsigned i = 0; i != N; ++i) buf[i] = s[i];
                }
            };
            template<unsigned N>
            FixedString(char const (&)[N])->FixedString<N - 1>;
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

        template <typename T>
        class Args : public pybind11::args {
            using args::args;
        };

        template <typename T>
        class KWArgs : public pybind11::kwargs {
            using kwargs::kwargs;
        };
    }
}


namespace pybind11 {
	namespace detail {
		template <pybind11_extensions::builtins::detail::FixedString T>
		struct handle_type_name<pybind11_extensions::builtins::PyObjectStr<T>> {
			static constexpr auto name = pybind11::detail::const_name(T.buf);
		};

		template <typename cppT>
		struct handle_type_name<pybind11_extensions::builtins::PyObjectCpp<cppT>> {
			static constexpr auto name = make_caster<cppT>::name;
		};

        template <typename T>
        struct handle_type_name<pybind11_extensions::builtins::Args<T>> {
            static constexpr auto name = const_name("*args: ") + make_caster<T>::name;
        };

        template <typename T>
        struct handle_type_name<pybind11_extensions::builtins::KWArgs<T>> {
            static constexpr auto name = const_name("**kwargs: ") + make_caster<T>::name;
        };
	}
}