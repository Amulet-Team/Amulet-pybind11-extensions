from __future__ import annotations

import faulthandler as _faulthandler

from . import (
    _test_amulet_pybind11_extensions,
    test_builtins_,
    test_collections_,
    test_compatibility_1_,
    test_compatibility_2_,
    test_contextlib_,
    test_hash_,
    test_iterator_,
    test_mapping_,
    test_mutable_mapping_,
    test_mutable_sequence_,
    test_nogil_holder_,
    test_numpy_,
    test_py_module_,
    test_py_module__,
    test_pybind11_,
    test_sequence_,
    test_types_,
)

__all__: list[str] = [
    "test_builtins_",
    "test_collections_",
    "test_compatibility_1_",
    "test_compatibility_2_",
    "test_contextlib_",
    "test_hash_",
    "test_iterator_",
    "test_mapping_",
    "test_mutable_mapping_",
    "test_mutable_sequence_",
    "test_nogil_holder_",
    "test_numpy_",
    "test_py_module_",
    "test_py_module__",
    "test_pybind11_",
    "test_sequence_",
    "test_types_",
]

def _init() -> None: ...
