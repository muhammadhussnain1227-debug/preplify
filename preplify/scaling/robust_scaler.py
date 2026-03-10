# preplify/scaling/robust_scaler.py
from .standard_scaler import scale_features


def robust_scale(df, columns=None):
    """Apply Robust scaling to numeric columns (handles outliers well)."""
    return scale_features(df, method="robust", columns=columns)
