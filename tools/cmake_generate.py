import sys
import subprocess
import os
import shutil

import pybind11


def fix_path(path: str) -> str:
    return os.path.realpath(path).replace(os.sep, "/")


RootDir = fix_path(os.path.dirname(os.path.dirname(__file__)))


def main():
    platform_args = []
    if sys.platform == "win32":
        platform_args.extend(["-G", "Visual Studio 17 2022"])
        if sys.maxsize > 2**32:
            platform_args.extend(["-A", "x64"])
        else:
            platform_args.extend(["-A", "Win32"])
        platform_args.extend(["-T", "v143"])

    os.chdir(RootDir)
    shutil.rmtree(os.path.join(RootDir, "build", "CMakeFiles"), ignore_errors=True)

    if subprocess.run(
        [
            "cmake",
            *platform_args,
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-Dpybind11_DIR={fix_path(pybind11.get_cmake_dir())}",
            f"-Damulet_pybind11_extensions_DIR={os.path.join(RootDir, 'src', 'amulet', 'pybind11_extensions')}",
            f"-DCMAKE_INSTALL_PREFIX=install",
            # test args
            f"-DTEST_AMULET_PYBIND11_EXTENSIONS_DIR={os.path.join(RootDir, 'tests')}",
            "-B",
            "build",
        ]
    ).returncode:
        raise RuntimeError("Error configuring amulet_pybind11_extensions")


if __name__ == "__main__":
    main()
