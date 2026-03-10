# preplify/outliers/zscore_detector.py
import numpy as np
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def remove_outliers_zscore(df, columns=None, threshold=3):
    """
    Remove rows where the Z-score of any numeric column exceeds `threshold`.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to check. Defaults to all numeric columns.
    threshold : float
        Z-score cutoff (default 3).
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)
    before = len(df)
    for col in columns:
        mean = df[col].mean()
        std = df[col].std()
        if std == 0:
            continue
        z_scores = np.abs((df[col] - mean) / std)
        df = df[z_scores < threshold]
    df = df.reset_index(drop=True)
    log_info(f"remove_outliers_zscore: removed {before - len(df)} outlier row(s).")
    return df
