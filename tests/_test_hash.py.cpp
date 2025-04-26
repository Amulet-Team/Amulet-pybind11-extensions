#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/hash.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

namespace detail {
class TestHashIdentity { };
class TestUnhashable { };
}

PYBIND11_MODULE(_test_hash, m)
{
    py::class_<detail::TestHashIdentity> TestHashIdentity(m, "TestHashIdentity");
    TestHashIdentity.def(py::init());
    Amulet::pybind11_extensions::def_hash_identity(TestHashIdentity);

    py::class_<detail::TestUnhashable> TestUnhashable(m, "TestUnhashable");
    TestUnhashable.def(py::init());
    Amulet::pybind11_extensions::def_hash_disable(TestUnhashable);
}
