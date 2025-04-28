#pragma once

#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/mapping.hpp>

namespace py = pybind11;

namespace Amulet {
namespace pybind11_extensions {
    namespace collections {
        template <typename KT = pybind11::object, typename VT = pybind11::object, typename clsT>
        void def_MutableMapping_pop(clsT cls)
        {
            pybind11::object marker = pybind11::module::import("builtins").attr("Ellipsis");
            cls.def(
                "pop",
                [marker](
                    pybind11::object self,
                    pybind11_extensions::PyObjectCpp<KT> key,
                    pybind11_extensions::PyObjectCpp<VT> default_) -> pybind11_extensions::PyObjectCpp<VT> {
                    pybind11::object value;
                    try {
                        value = self.attr("__getitem__")(key);
                    } catch (const pybind11::error_already_set& e) {
                        if (e.matches(PyExc_KeyError)) {
                            if (default_.is(marker)) {
                                throw;
                            }
                            return default_;
                        } else {
                            throw;
                        }
                    }
                    self.attr("__delitem__")(key);
                    return value;
                },
                pybind11::arg("key"),
                pybind11::arg("default") = marker);
        }

        template <typename KT = pybind11::object, typename VT = pybind11::object, typename clsT>
        void def_MutableMapping_popitem(clsT cls)
        {
            pybind11::object iter = pybind11::module::import("builtins").attr("iter");
            pybind11::object next = pybind11::module::import("builtins").attr("next");
            cls.def(
                "popitem",
                [iter, next](pybind11::object self) -> std::pair<
                                                        pybind11_extensions::PyObjectCpp<KT>,
                                                        pybind11_extensions::PyObjectCpp<VT>> {
                    pybind11::object key;
                    try {
                        key = next(iter(self));
                    } catch (const pybind11::error_already_set& e) {
                        if (e.matches(PyExc_StopIteration)) {
                            throw pybind11::key_error();
                        } else {
                            throw;
                        }
                    }
                    pybind11::object value = self.attr("__getitem__")(key);
                    self.attr("__delitem__")(key);
                    return std::make_pair(key, value);
                });
        }

        template <typename clsT>
        void def_MutableMapping_clear(clsT cls)
        {
            cls.def(
                "clear",
                [](pybind11::object self) {
                    try {
                        while (true) {
                            self.attr("popitem")();
                        }
                    } catch (const pybind11::error_already_set& e) {
                        if (!e.matches(PyExc_KeyError)) {
                            throw;
                        }
                    }
                });
        }

        template <typename clsT>
        void def_MutableMapping_update(clsT cls)
        {
            pybind11::object isinstance = pybind11::module::import("builtins").attr("isinstance");
            pybind11::object hasattr = pybind11::module::import("builtins").attr("hasattr");
            pybind11::object PyMapping = pybind11::module::import("collections.abc").attr("Mapping");
            cls.def(
                "update",
                [isinstance,
                    hasattr,
                    PyMapping](
                    pybind11::object self,
                    pybind11::object other,
                    pybind11::kwargs kwargs) {
                    if (py::hasattr(other, "keys")) {
                        pybind11::object keys = other.attr("keys")();
                        for (auto it = keys.begin(); it != keys.end(); it++) {
                            self.attr("__setitem__")(*it, other.attr("__getitem__")(*it));
                        }
                    } else {
                        for (auto it = other.begin(); it != other.end(); it++) {
                            self.attr("__setitem__")(
                                it->attr("__getitem__")(0),
                                it->attr("__getitem__")(1));
                        }
                    }
                    pybind11::object items = kwargs.attr("items")();
                    for (auto it = items.begin(); it != items.end(); it++) {
                        self.attr("__setitem__")(
                            it->attr("__getitem__")(0),
                            it->attr("__getitem__")(1));
                    }
                },
                pybind11::arg("other") = pybind11::tuple());
        }

        template <typename KT = pybind11::object, typename VT = pybind11::object, typename clsT>
        void def_MutableMapping_setdefault(clsT cls)
        {
            cls.def(
                "setdefault",
                [](
                    pybind11::object self,
                    pybind11_extensions::PyObjectCpp<KT> key,
                    pybind11::typing::Optional<VT> default_ = pybind11::none()) -> pybind11::typing::Optional<VT> {
                    try {
                        return self.attr("__getitem__")(key);
                    } catch (const pybind11::error_already_set& e) {
                        if (e.matches(PyExc_KeyError)) {
                            self.attr("__setitem__")(key, default_);
                        } else {
                            throw;
                        }
                    }
                    return default_;
                });
        }

        template <typename clsT>
        void register_MutableMapping(clsT cls)
        {
            pybind11::module::import("collections.abc").attr("MutableMapping").attr("register")(cls);
        }

    } // namespace collections
} // namespace pybind11_extensions
} // namespace Amulet
