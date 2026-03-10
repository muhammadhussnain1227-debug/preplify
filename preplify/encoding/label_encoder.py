# preplify/encoding/label_encoder.py
from sklearn.preprocessing import LabelEncoder
from ..utils.dataframe_validator import validate_dataframe, get_categorical_columns
from ..utils.logging import log_info


def label_encode(df, columns=None):
    """
    Label-encode categorical columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to encode. Defaults to all categorical columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_categorical_columns(df)
    le = LabelEncoder()
    for col in columns:
        df[col] = le.fit_transform(df[col].astype(str))
    log_info(f"label_encode: encoded {len(columns)} column(s).")
    return df
