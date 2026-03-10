# preplify/feature_selection/correlation_filter.py
import numpy as np
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def correlation_filter(df, threshold=0.9, columns=None):
    """
    Remove highly correlated numeric features (keeps one from each correlated pair).

    Parameters
    ----------
    df : pd.DataFrame
    threshold : float
        Correlation coefficient above which one column is dropped (default 0.9).
    columns : list, optional
        Subset of columns to check. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)

    corr_matrix = df[columns].corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    drop_cols = [col for col in upper.columns if any(upper[col] > threshold)]
    df = df.drop(columns=drop_cols)
    log_info(f"correlation_filter: dropped {len(drop_cols)} highly correlated column(s): {drop_cols}.")
    return df
