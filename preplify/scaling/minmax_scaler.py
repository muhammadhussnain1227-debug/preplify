# preplify/scaling/minmax_scaler.py
from .standard_scaler import scale_features


def minmax_scale(df, columns=None):
    """Apply Min-Max scaling to numeric columns."""
    return scale_features(df, method="minmax", columns=columns)
