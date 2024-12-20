#pragma once
#include <pybind11/pybind11.h>

// I have found cases where I want to accept or return a python object matching a collections.abc class.
// This extension adds subclasses of py::object with type hints for the collections.abc classes.
// This allows C++ functions to accept or return python objects that match the collection.abc classes.
// Note that these are handled in the same way as py::object thus there is no type validation.

namespace pybind11_extensions {
namespace collections {
    namespace abc {
        template <typename T>
        class Iterator : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(Iterator, object, PyObject_Type)
            using object::object;
        };

        template <typename T>
        class Sequence : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(Sequence, object, PyObject_Type)
            using object::object;
        };

        template <typename K, typename V>
        class Mapping : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(Mapping, object, PyObject_Type)
            using object::object;
        };

        template <typename K, typename V>
        class MutableMapping : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(MutableMapping, object, PyObject_Type)
            using object::object;
        };

        template <typename K>
        class KeysView : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(KeysView, object, PyObject_Type)
            using object::object;
        };

        template <typename V>
        class ValuesView : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(ValuesView, object, PyObject_Type)
            using object::object;
        };

        template <typename K, typename V>
        class ItemsView : public pybind11::object {
            PYBIND11_OBJECT_DEFAULT(ItemsView, object, PyObject_Type)
            using object::object;
        };
    }
}
}

namespace pybind11 {
namespace detail {
    template <typename T>
    struct handle_type_name<pybind11_extensions::collections::abc::Iterator<T>> {
        static constexpr auto name = const_name("collections.abc.Iterator[") + make_caster<T>::name + const_name("]");
    };

    template <typename T>
    struct handle_type_name<pybind11_extensions::collections::abc::Sequence<T>> {
        static constexpr auto name = const_name("collections.abc.Sequence[") + make_caster<T>::name + const_name("]");
    };

    template <typename K, typename V>
    struct handle_type_name<pybind11_extensions::collections::abc::Mapping<K, V>> {
        static constexpr auto name = const_name("collections.abc.Mapping[") + make_caster<K>::name + const_name(", ") + make_caster<V>::name + const_name("]");
    };

    template <typename K, typename V>
    struct handle_type_name<pybind11_extensions::collections::abc::MutableMapping<K, V>> {
        static constexpr auto name = const_name("collections.abc.MutableMapping[") + make_caster<K>::name + const_name(", ")
            + make_caster<V>::name + const_name("]");
    };

    template <typename K>
    struct handle_type_name<pybind11_extensions::collections::abc::KeysView<K>> {
        static constexpr auto name = const_name("collections.abc.KeysView[") + make_caster<K>::name + const_name("]");
    };

    template <typename V>
    struct handle_type_name<pybind11_extensions::collections::abc::ValuesView<V>> {
        static constexpr auto name = const_name("collections.abc.ValuesView[") + make_caster<V>::name + const_name("]");
    };

    template <typename K, typename V>
    struct handle_type_name<pybind11_extensions::collections::abc::ItemsView<K, V>> {
        static constexpr auto name = const_name("collections.abc.ItemsView[") + make_caster<K>::name + const_name(", ")
            + make_caster<V>::name + const_name("]");
    };
}
}
