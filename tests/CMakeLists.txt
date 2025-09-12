cmake_minimum_required(VERSION 3.13)

project(amulet_pybind11_extensions_tests LANGUAGES CXX)

# Set C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set platform variables
if (WIN32)
	# set windows 7 as the minimum version
	add_definitions(-D_WIN32_WINNT=0x0601)
elseif(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15")
else()
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

# Add pybind11
if (NOT TARGET pybind11::module)
    find_package(pybind11 CONFIG REQUIRED)
endif()
if (NOT TARGET amulet_pybind11_extensions)
    find_package(amulet_pybind11_extensions CONFIG REQUIRED)
endif()

function(add_text_ext name)
    pybind11_add_module(${name})
    target_link_libraries(${name} PRIVATE amulet_pybind11_extensions)
    target_compile_definitions(${name} PRIVATE PYBIND11_DETAILED_ERROR_MESSAGES)
    target_compile_definitions(${name} PRIVATE PYBIND11_VERSION="${pybind11_VERSION}")
    target_compile_definitions(${name} PRIVATE COMPILER_ID="${CMAKE_CXX_COMPILER_ID}")
    target_compile_definitions(${name} PRIVATE COMPILER_VERSION="${CMAKE_CXX_COMPILER_VERSION}")
    target_sources(${name} PRIVATE ${name}.py.cpp)
    install(TARGETS ${name} DESTINATION "${CMAKE_CURRENT_LIST_DIR}")
endfunction()

# Add python extensions
add_text_ext(_test_builtins)
add_text_ext(_test_collections)
add_text_ext(_test_compatibility_1)
add_text_ext(_test_compatibility_2)
add_text_ext(_test_contextlib)
add_text_ext(_test_hash)
add_text_ext(_test_iterator)
add_text_ext(_test_mapping)
add_text_ext(_test_mutable_mapping)
add_text_ext(_test_nogil_holder)
add_text_ext(_test_numpy)
add_text_ext(_test_py_module_)
add_text_ext(_test_pybind11)
add_text_ext(_test_sequence)
add_text_ext(_test_types)
