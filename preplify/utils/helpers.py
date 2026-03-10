# preplify/utils/helpers.py
import numpy as np


def safe_divide(a, b, fill=0.0):
    """
    Divide a by b, replacing division-by-zero results with `fill`.
    Works with scalars, lists, and numpy arrays.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.where(b == 0, fill, a / b)
    return result
