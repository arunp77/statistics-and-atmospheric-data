# Purpose:
# Common statistical helpers used across notebooks.


import numpy as np
from scipy import stats
from typing import Tuple


def confidence_interval_mean(
    data: np.ndarray,
    confidence: float = 0.95
) -> Tuple[float, float]:
    """
    Compute confidence interval for the mean using t-distribution.
    """
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    se = std / np.sqrt(n)

    return stats.t.interval(
        confidence=confidence,
        df=n - 1,
        loc=mean,
        scale=se
    )


def confidence_interval_diff_means(
    x: np.ndarray,
    y: np.ndarray,
    confidence: float = 0.95
) -> Tuple[float, float]:
    """
    Confidence interval for difference of means (Welch).
    """
    nx, ny = len(x), len(y)
    mx, my = np.mean(x), np.mean(y)
    sx, sy = np.std(x, ddof=1), np.std(y, ddof=1)

    se = np.sqrt(sx**2 / nx + sy**2 / ny)
    df = min(nx, ny) - 1

    return stats.t.interval(
        confidence=confidence,
        df=df,
        loc=mx - my,
        scale=se
    )


def check_normality(data: np.ndarray, alpha: float = 0.05) -> bool:
    """
    Shapiro-Wilk normality test.
    Returns True if data is approximately normal.
    """
    _, p = stats.shapiro(data)
    return p > alpha


def check_equal_variance(x: np.ndarray, y: np.ndarray, alpha: float = 0.05) -> bool:
    """
    Levene test for equal variances.
    """
    _, p = stats.levene(x, y)
    return p > alpha
