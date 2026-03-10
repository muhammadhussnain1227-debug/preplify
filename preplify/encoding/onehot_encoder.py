# preplify/encoding/onehot_encoder.py
import pandas as pd
from ..utils.dataframe_validator import validate_dataframe, get_categorical_columns
from ..utils.logging import log_info


def onehot_encode(df, columns=None, drop_first=True):
    """
    One-hot encode categorical columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to encode. Defaults to all categorical columns.
    drop_first : bool
        Drop the first dummy to avoid multicollinearity.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_categorical_columns(df)
    df = pd.get_dummies(df, columns=columns, drop_first=drop_first)
    log_info(f"onehot_encode: encoded {len(columns)} column(s).")
    return df
