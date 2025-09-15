#include <pybind11/pybind11.h>

#include <amulet/pybind11_extensions/builtins.hpp>

namespace py = pybind11;
namespace pyext = Amulet::pybind11_extensions;

class MyCppClass {
public:
    int value;

    MyCppClass(int value)
        : value(value)
    {
    }
};

MyCppClass func1(const MyCppClass& other)
{
    return other;
}

pyext::PyObjectStr<"test_amulet_pybind11_extensions.test_builtins_.MyPyClass"> func2(pyext::PyObjectStr<"test_amulet_pybind11_extensions.test_builtins_.MyPyClass"> other)
{
    return other;
}

pyext::PyObjectCpp<MyCppClass> func3(pyext::PyObjectCpp<MyCppClass> other)
{
    return other;
}

void init_test_builtins(py::module m_parent)
{
    auto m = m_parent.def_submodule("test_builtins_");

    py::class_<MyCppClass> MyPyClass(m, "MyPyClass");
    MyPyClass.def(py::init<int>());
    MyPyClass.def_readonly("value", &MyCppClass::value);

    m.def("func1", &func1);
    m.def("func2", &func2);
    m.def("func3", &func3);
}
