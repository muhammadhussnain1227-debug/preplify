# preplify/feature_selection/variance_filter.py
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def variance_filter(df, threshold=0.01, columns=None):
    """
    Remove numeric columns with variance below `threshold`.

    Parameters
    ----------
    df : pd.DataFrame
    threshold : float
        Minimum variance to keep a column (default 0.01).
    columns : list, optional
        Columns to check. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)

    selector = VarianceThreshold(threshold=threshold)
    selector.fit(df[columns])
    kept_mask = selector.get_support()
    kept_cols = [col for col, keep in zip(columns, kept_mask) if keep]
    dropped_cols = [col for col, keep in zip(columns, kept_mask) if not keep]

    non_numeric = [c for c in df.columns if c not in columns]
    df = df[non_numeric + kept_cols]
    log_info(f"variance_filter: dropped {len(dropped_cols)} low-variance column(s): {dropped_cols}.")
    return df
