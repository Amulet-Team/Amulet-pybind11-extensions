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
find_package(pybind11 CONFIG REQUIRED)
find_package(amulet_pybind11_extensions CONFIG REQUIRED)

function(add_text_ext name)
    pybind11_add_module(${name})
    target_link_libraries(${name} PRIVATE amulet_pybind11_extensions)
    target_compile_definitions(${name} PRIVATE PYBIND11_DETAILED_ERROR_MESSAGES)
    target_sources(${name} PRIVATE ${name}.py.cpp)
    install(TARGETS ${name} DESTINATION ".")
endfunction()

# Add python extensions
add_text_ext(_test_collections)
