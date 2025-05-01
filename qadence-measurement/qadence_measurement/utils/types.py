from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from qadence_commons import StrEnum

import torch
from torch import Tensor


@dataclass
class MeasurementData:
    samples: Tensor | list[Counter] = dataclass_field(default_factory=list)
    """Samples from protocol."""
    unitaries: Tensor = torch.empty(0)
    """Random unitaries used in shadows."""


class MeasurementProtocol(StrEnum):
    TOMOGRAPHY = "tomography"
    """Tomography of a quantum state."""
    SHADOW = "shadow"
    """Snapshots of a state via shadows."""
    ROBUST_SHADOW = "robust_shadow"
    """Snapshots of a state via shadows for noisy settings."""
