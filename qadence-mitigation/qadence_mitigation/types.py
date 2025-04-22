from __future__ import annotations
from qadence_commons import StrEnum


class ReadOutOptimization(StrEnum):
    # Basic inversion and maximum likelihood estimate
    MLE = "mle"
    # Constrained inverse optimization
    CONSTRAINED = "constrained"
    # Matrix free measurement mitigation
    MTHREE = "mthree"
    # Majority voting
    MAJ_VOTE = "majority_vote"
