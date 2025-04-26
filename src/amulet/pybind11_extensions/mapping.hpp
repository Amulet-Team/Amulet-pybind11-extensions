#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/typing.h>

#include <variant>

#include <amulet/pybind11_extensions/hash.hpp>
#include <amulet/pybind11_extensions/builtins.hpp>
#include <amulet/pybind11_extensions/collections.hpp>
#include <amulet/pybind11_extensions/types.hpp>

namespace Amulet {
namespace pybind11_extensions {
    namespace collections {
        template <typename clsT>
        void def_Mapping_repr(clsT cls)
        {
            cls.def(
                "__repr__",
                [](pybind11::object self) {
                    std::string repr = "{";
                    bool is_first = true;
                    for (auto it = self.begin(); it != self.end(); it++) {
                        if (is_first) {
                            is_first = false;
                        } else {
                            repr += ", ";
                        }
                        repr += pybind11::repr(*it);
                        repr += ": ";
                        repr += pybind11::repr(self.attr("__getitem__")(*it));
                    }
                    repr += "}";
                    return repr;
                });
        }

        template <typename KT = pybind11::object, typename clsT>
        void def_Mapping_contains(clsT cls)
        {
            cls.def(
                "__contains__",
                [](pybind11::object self, pybind11_extensions::PyObjectCpp<KT> key) {
                    try {
                        self.attr("__getitem__")(key);
                        return true;
                    } catch (const pybind11::error_already_set& e) {
                        if (e.matches(PyExc_KeyError)) {
                            return false;
                        } else {
                            throw;
                        }
                    }
                });
        }

        template <typename KT = pybind11::object, typename clsT>
        void def_Mapping_keys(clsT cls)
        {
            pybind11::object KeysView = pybind11::module::import("collections.abc").attr("KeysView");
            cls.def(
                "keys",
                [KeysView](pybind11::object self) -> pybind11_extensions::collections::KeysView<KT> { return KeysView(self); });
        }

        template <typename VT = pybind11::object, typename clsT>
        void def_Mapping_values(clsT cls)
        {
            pybind11::object ValuesView = pybind11::module::import("collections.abc").attr("ValuesView");
            cls.def(
                "values",
                [ValuesView](pybind11::object self) -> pybind11_extensions::collections::ValuesView<VT> { return ValuesView(self); });
        }

        template <typename KT = pybind11::object, typename VT = pybind11::object, typename clsT>
        void def_Mapping_items(clsT cls)
        {
            pybind11::object ItemsView = pybind11::module::import("collections.abc").attr("ItemsView");
            cls.def(
                "items",
                [ItemsView](pybind11::object self) -> pybind11_extensions::collections::ItemsView<KT, VT> { return ItemsView(self); });
        }

        template <typename KT = pybind11::object, typename VT = pybind11::object, typename clsT>
        void def_Mapping_get(clsT cls)
        {
            cls.def(
                "get",
                [](
                    pybind11::object self,
                    pybind11_extensions::PyObjectCpp<KT> key,
                    pybind11::typing::Optional<VT> default_) -> pybind11::typing::Optional<VT> {
                    try {
                        return self.attr("__getitem__")(key);
                    } catch (const pybind11::error_already_set& e) {
                        if (e.matches(PyExc_KeyError)) {
                            return default_;
                        } else {
                            throw;
                        }
                    }
                },
                pybind11::arg("key"),
                pybind11::arg("default") = pybind11::none());
        }

        template <typename clsT>
        void def_Mapping_eq(clsT cls)
        {
            pybind11::object dict = pybind11::module::import("builtins").attr("dict");
            pybind11::object isinstance = pybind11::module::import("builtins").attr("isinstance");
            pybind11::object NotImplemented = pybind11::module::import("builtins").attr("NotImplemented");
            pybind11::object PyMapping = pybind11::module::import("collections.abc").attr("Mapping");
            cls.def(
                "__eq__",
                [dict,
                    isinstance,
                    NotImplemented,
                    PyMapping](
                    pybind11::object self,
                    pybind11::object other) -> std::variant<bool, pybind11_extensions::types::NotImplementedType> {
                    if (!isinstance(other, PyMapping)) {
                        return NotImplemented;
                    }
                    return dict(self.attr("items")()).equal(dict(other.attr("items")()).cast<pybind11::dict>());
                });
        }

        template <typename clsT>
        void def_Mapping_hash(clsT cls)
        {
            Amulet::pybind11_extensions::def_unhashable(cls);
        }

        template <typename clsT>
        void register_Mapping(clsT cls)
        {
            pybind11::module::import("collections.abc").attr("Mapping").attr("register")(cls);
        }

    } // namespace collections
} // namespace pybind11_extensions
} // namespace Amulet
