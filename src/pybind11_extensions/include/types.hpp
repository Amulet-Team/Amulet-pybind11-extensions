#pragma once
#include <pybind11/pybind11.h>

// This extension adds a py::object subclass for types.NotImplementedType.
// This is used as a return in comparison operators.


namespace pybind11_extensions {
    namespace types {
        class NotImplementedType : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(NotImplementedType, object, PyObject_Type)
            using object::object;
        };
    }
}


namespace pybind11 {
	namespace detail {
		template <>
		struct handle_type_name<pybind11_extensions::types::NotImplementedType> {
			static constexpr auto name = const_name("types.NotImplementedType");
		};
	}
}
