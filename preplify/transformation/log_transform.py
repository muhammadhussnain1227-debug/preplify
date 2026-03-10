# preplify/transformation/log_transform.py
import numpy as np
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info, log_warning


def log_transform(df, columns=None):
    """
    Apply log1p transformation to numeric columns.
    Columns with negative values are skipped with a warning.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to transform. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)

    skipped = []
    transformed = []
    for col in columns:
        if (df[col] < 0).any():
            log_warning(f"log_transform: skipping '{col}' — contains negative values.")
            skipped.append(col)
        else:
            df[col] = np.log1p(df[col])
            transformed.append(col)

    log_info(f"log_transform: transformed {len(transformed)} column(s), skipped {len(skipped)}.")
    return df
