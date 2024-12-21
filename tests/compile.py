import subprocess
import sys
import shutil
import os

import pybind11
import pybind11_extensions

if os.path.isdir("build/CMakeFiles"):
    shutil.rmtree("build/CMakeFiles")

if subprocess.run(
    [
        "cmake",
        "-G",
        "Visual Studio 17 2022",
        "-A",
        "x64",
        f"-DPYTHON_EXECUTABLE={sys.executable}",
        f"-Dpybind11_DIR={pybind11.get_cmake_dir().replace(os.sep, '/')}",
        f"-Dpybind11_extensions_DIR={pybind11_extensions.__path__[0].replace(os.sep, '/')}",
        f"-DCMAKE_INSTALL_PREFIX={os.path.dirname(__file__)}",
        "-B",
        "build",
    ]
).returncode:
    raise RuntimeError("Error configuring pybind11_extensions")
if subprocess.run(
    ["cmake", "--build", "build", "--config", "RelWithDebInfo"]
).returncode:
    raise RuntimeError("Error installing pybind11_extensions")
if subprocess.run(
    ["cmake", "--install", "build", "--config", "RelWithDebInfo"]
).returncode:
    raise RuntimeError("Error installing pybind11_extensions")
