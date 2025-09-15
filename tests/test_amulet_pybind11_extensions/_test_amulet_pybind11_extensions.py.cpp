#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/compatibility.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

void init_test_builtins(py::module);
void init_test_collections(py::module);
void init_test_compatibility_1(py::module);
void init_test_compatibility_2(py::module);
void init_test_contextlib(py::module);
void init_test_hash(py::module);
void init_test_iterator(py::module);
void init_test_mapping(py::module);
void init_test_mutable_mapping(py::module);
void init_test_nogil_holder(py::module);
void init_test_numpy(py::module);
void init_test_py_module(py::module);
void init_test_pybind11(py::module);
void init_test_sequence(py::module);
void init_test_types(py::module);

void init_module(py::module m){
    init_test_builtins(m);
    init_test_collections(m);
    init_test_compatibility_1(m);
    init_test_compatibility_2(m);
    init_test_contextlib(m);
    init_test_hash(m);
    init_test_iterator(m);
    init_test_mapping(m);
    init_test_mutable_mapping(m);
    init_test_nogil_holder(m);
    init_test_numpy(m);
    init_test_py_module(m);
    init_test_pybind11(m);
    init_test_sequence(m);
    init_test_types(m);
}

PYBIND11_MODULE(_test_amulet_pybind11_extensions, m) {
    py::options options;
    options.disable_function_signatures();
    m.def("init", &init_module, py::doc("init(arg0: types.ModuleType) -> None"));
    options.enable_function_signatures();
}
