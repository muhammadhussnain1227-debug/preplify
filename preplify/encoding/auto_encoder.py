# preplify/encoding/auto_encoder.py
from .onehot_encoder import onehot_encode
from .label_encoder import label_encode
from ..utils.dataframe_validator import validate_dataframe, get_categorical_columns
from ..utils.logging import log_info


def encode_features(df, method="onehot", columns=None):
    """
    Automatically encode categorical features.

    Parameters
    ----------
    df : pd.DataFrame
    method : str
        'onehot' or 'label'
    columns : list, optional
        Columns to encode. Defaults to all categorical columns.
    """
    validate_dataframe(df)
    if columns is None:
        columns = get_categorical_columns(df)
    if not columns:
        log_info("encode_features: no categorical columns found, skipping.")
        return df

    if method == "onehot":
        return onehot_encode(df, columns=columns)
    elif method == "label":
        return label_encode(df, columns=columns)
    else:
        raise ValueError(f"Invalid encoding method '{method}'. Choose 'onehot' or 'label'.")
