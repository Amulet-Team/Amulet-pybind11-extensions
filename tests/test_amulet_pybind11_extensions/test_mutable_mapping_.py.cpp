#include <pybind11/pybind11.h>

#include <map>
#include <memory>
#include <string>

#include <amulet/pybind11_extensions/mapping.hpp>
#include <amulet/pybind11_extensions/mutable_mapping.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestMutableMapping {
public:
    std::map<std::string, int> map;

    TestMutableMapping(std::map<std::string, int> map)
        : map(std::move(map))
    {
    }
};
}

static std::map<int, int> GlobalIntMap { { 10, 20 }, { 30, 40 }, { 50, 60 } };

void init_test_mutable_mapping(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_mutable_mapping_");

    py::class_<detail::TestMutableMapping> TestMutableMapping(m, "TestMutableMapping");
    TestMutableMapping.def(py::init<std::map<std::string, int>>());
    TestMutableMapping.def(
        "__getitem__",
        [](const detail::TestMutableMapping& self, std::string key) {
            auto it = self.map.find(key);
            if (it == self.map.end()) {
                throw py::key_error();
            } else {
                return it->second;
            }
        });
    TestMutableMapping.def(
        "__setitem__",
        [](detail::TestMutableMapping& self, std::string key, int value) {
            self.map.insert_or_assign(key, value);
        });
    TestMutableMapping.def(
        "__delitem__",
        [](detail::TestMutableMapping& self, std::string key) {
            self.map.erase(key);
        });
    TestMutableMapping.def(
        "__len__",
        [](const detail::TestMutableMapping& self) {
            return self.map.size();
        });
    TestMutableMapping.def(
        "__iter__",
        [](const detail::TestMutableMapping& self) {
            return py::make_key_iterator(self.map);
        },
        py::keep_alive<0, 1>());
    using Map = pyext::collections::MutableMapping<std::string, int>;
    Map::def_repr(TestMutableMapping);
    Map::def_contains(TestMutableMapping);
    Map::def_keys(TestMutableMapping);
    Map::def_values(TestMutableMapping);
    Map::def_items(TestMutableMapping);
    Map::def_get(TestMutableMapping);
    Map::def_eq(TestMutableMapping);
    Map::def_hash(TestMutableMapping);
    Map::def_pop(TestMutableMapping);
    Map::def_popitem(TestMutableMapping);
    Map::def_clear(TestMutableMapping);
    Map::def_update(TestMutableMapping);
    Map::def_setdefault(TestMutableMapping);
    Map::register_cls(TestMutableMapping);

    m.def("get_global_int_map", []() {
        return pyext::make_mutable_mapping(GlobalIntMap);
    });

    m.def("make_int_int_map", []() {
        auto map = std::make_unique<std::map<int, int>>();
        map->emplace(1, 2);
        map->emplace(3, 4);
        map->emplace(5, 6);
        return pyext::make_mutable_mapping(*map, std::move(map));
    });

    m.def("make_str_int_map", []() {
        auto map = std::make_unique<std::map<std::string, int>>();
        map->emplace("1", 2);
        map->emplace("3", 4);
        map->emplace("5", 6);
        return pyext::make_mutable_mapping(*map, std::move(map));
    });
}
