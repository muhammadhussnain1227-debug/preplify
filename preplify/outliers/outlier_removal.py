# preplify/outliers/outlier_removal.py
from .iqr_detector import remove_outliers_iqr
from .zscore_detector import remove_outliers_zscore


def remove_outliers(df, method="iqr", columns=None, threshold=3):
    """
    Unified outlier removal wrapper.

    Parameters
    ----------
    df : pd.DataFrame
    method : str
        'iqr' or 'zscore'
    columns : list, optional
        Columns to check. Defaults to all numeric.
    threshold : float
        Only used for Z-score method.
    """
    if method == "iqr":
        return remove_outliers_iqr(df, columns=columns)
    elif method == "zscore":
        return remove_outliers_zscore(df, columns=columns, threshold=threshold)
    else:
        raise ValueError(f"Invalid method '{method}'. Choose 'iqr' or 'zscore'.")
