#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/hash.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestHashIdentity { };
class TestUnhashable { };
}

void init_test_hash(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_hash_");

    py::class_<detail::TestHashIdentity> TestHashIdentity(m, "TestHashIdentity");
    TestHashIdentity.def(py::init());
    Amulet::pybind11_extensions::def_hash_identity(TestHashIdentity);

    py::class_<detail::TestUnhashable> TestUnhashable(m, "TestUnhashable");
    TestUnhashable.def(py::init());
    Amulet::pybind11_extensions::def_unhashable(TestUnhashable);
}
