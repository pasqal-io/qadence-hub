from __future__ import annotations

"""Fetch the functions defined in the __all__ of each sub-module.

Import to the qadence name space. Make sure each added submodule has the respective definition:

    - `__all__ = ["function0", "function1", ...]`

Furthermore, add the submodule to the list below to automatically build
the __all__ of the qadence namespace. Make sure to keep alphabetical ordering.
"""

from .models import (
    FeatureMapConfig,
    AnsatzConfig,
    create_fm_blocks,
    create_ansatz,
    create_observable,
    build_qnn_from_configs,
    QNN,
    QCNN,
    get_parameters,
    set_parameters,
    num_parameters,
)

from .optimizers import (
    QuantumNaturalGradient,
    get_quantum_fisher,
    get_quantum_fisher_spsa,
)

__all__ = [
    "FeatureMapConfig",
    "AnsatzConfig",
    "create_fm_blocks",
    "create_ansatz",
    "create_observable",
    "build_qnn_from_configs",
    "QNN",
    "QCNN",
    "get_parameters",
    "set_parameters",
    "num_parameters",
    "QuantumNaturalGradient",
    "get_quantum_fisher",
    "get_quantum_fisher_spsa",
]
