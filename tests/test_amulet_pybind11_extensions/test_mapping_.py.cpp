#include <pybind11/pybind11.h>

#include <map>
#include <memory>
#include <string>

#include <amulet/pybind11_extensions/mapping.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestMapping {
public:
    std::map<int, int> map;

    TestMapping(std::map<int, int> map)
        : map(std::move(map))
    {
    }
};
}

static std::map<int, int> GlobalIntMap { { 10, 20 }, { 30, 40 }, { 50, 60 } };

void init_test_mapping(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_mapping_");

    py::class_<detail::TestMapping> TestMapping(m, "TestMapping");
    TestMapping.def(py::init<std::map<int, int>>());
    TestMapping.def(
        "__getitem__",
        [](const detail::TestMapping& self, int key) {
            auto it = self.map.find(key);
            if (it == self.map.end()) {
                throw py::key_error();
            } else {
                return it->second;
            }
        });
    TestMapping.def(
        "__len__",
        [](const detail::TestMapping& self) {
            return self.map.size();
        });
    TestMapping.def(
        "__iter__",
        [](const detail::TestMapping& self) {
            return py::make_key_iterator(self.map);
        },
        py::keep_alive<0, 1>());
    using Map = pyext::collections::Mapping<int, int>;
    Map::def_repr(TestMapping);
    Map::def_contains(TestMapping);
    Map::def_keys(TestMapping);
    Map::def_values(TestMapping);
    Map::def_items(TestMapping);
    Map::def_get(TestMapping);
    Map::def_eq(TestMapping);
    Map::def_hash(TestMapping);
    Map::register_cls(TestMapping);

    m.def("get_global_int_map", []() {
        return pyext::make_mapping(GlobalIntMap);
    });

    m.def("make_int_int_map", []() {
        auto map = std::make_unique<std::map<int, int>>();
        map->emplace(1, 2);
        map->emplace(3, 4);
        map->emplace(5, 6);
        return pyext::make_mapping(*map, std::move(map));
    });

    m.def("make_str_int_map", []() {
        auto map = std::make_unique<std::map<std::string, int>>();
        map->emplace("1", 2);
        map->emplace("3", 4);
        map->emplace("5", 6);
        return pyext::make_mapping(*map, std::move(map));
    });
}
