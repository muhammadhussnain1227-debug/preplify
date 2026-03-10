# preplify/profiling/summary_stats.py
import pandas as pd
from ..utils.dataframe_validator import validate_dataframe


def summary_stats(df):
    """
    Return a summary statistics dictionary for the DataFrame.

    Includes: shape, dtypes, describe, missing counts, unique counts.
    """
    validate_dataframe(df)
    stats = {
        "shape": df.shape,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_counts": df.isnull().sum().to_dict(),
        "missing_pct": (df.isnull().mean() * 100).round(2).to_dict(),
        "unique_counts": df.nunique().to_dict(),
        "numeric_summary": df.describe().round(4).to_dict(),
    }
    return stats
