# Purpose:
# Central place for all effect size calculations.

import numpy as np
from typing import Tuple


def cohens_d_one_sample(sample: np.ndarray, mu: float) -> float:
    """
    Compute Cohen's d for a one-sample test.
    """
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    return (mean - mu) / std


def cohens_d_two_sample(x: np.ndarray, y: np.ndarray) -> float:
    """
    Compute Cohen's d for two independent samples.
    """
    nx, ny = len(x), len(y)
    sx, sy = np.std(x, ddof=1), np.std(y, ddof=1)

    pooled_std = np.sqrt(
        ((nx - 1) * sx**2 + (ny - 1) * sy**2) / (nx + ny - 2)
    )

    return (np.mean(x) - np.mean(y)) / pooled_std


def eta_squared(ss_between: float, ss_total: float) -> float:
    """
    Compute eta squared (η²) for ANOVA.
    """
    return ss_between / ss_total


def interpret_cohens_d(d: float) -> str:
    """
    Qualitative interpretation of Cohen's d.
    """
    d = abs(d)
    if d < 0.2:
        return "negligible"
    elif d < 0.5:
        return "small"
    elif d < 0.8:
        return "medium"
    else:
        return "large"
