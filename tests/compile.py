import subprocess
import sys
import shutil
import os

import pybind11
import amulet.pybind11


def main():
    os.chdir(os.path.dirname(__file__))

    if os.path.isdir("build/CMakeFiles"):
        shutil.rmtree("build/CMakeFiles")

    platform_args = []
    if sys.platform == "win32":
        platform_args.extend(["-G", "Visual Studio 17 2022"])
        if sys.maxsize > 2**32:
            platform_args.extend(["-A", "x64"])
        else:
            platform_args.extend(["-A", "Win32"])
        platform_args.extend(["-T", "v143"])

    if subprocess.run(
        [
            "cmake",
            *platform_args,
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-Dpybind11_DIR={pybind11.get_cmake_dir().replace(os.sep, '/')}",
            f"-Damulet_pybind11_extensions_DIR={amulet.pybind11.__path__[0].replace(os.sep, '/')}",
            f"-DCMAKE_INSTALL_PREFIX={os.path.dirname(__file__)}",
            "-B",
            "build",
        ]
    ).returncode:
        raise RuntimeError("Error configuring amulet_pybind11_extensions")
    if subprocess.run(
        ["cmake", "--build", "build", "--config", "RelWithDebInfo"]
    ).returncode:
        raise RuntimeError("Error installing amulet_pybind11_extensions")
    if subprocess.run(
        ["cmake", "--install", "build", "--config", "RelWithDebInfo"]
    ).returncode:
        raise RuntimeError("Error installing amulet_pybind11_extensions")


if __name__ == "__main__":
    main()
