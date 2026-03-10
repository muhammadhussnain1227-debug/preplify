# preplify/utils/dataframe_validator.py
import pandas as pd


def validate_dataframe(df):
    """Raise ValueError if df is not a pandas DataFrame."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    if df.empty:
        raise ValueError("DataFrame is empty.")
    return df


def get_numeric_columns(df):
    """Return list of numeric column names (int or float)."""
    return df.select_dtypes(include=["int8", "int16", "int32", "int64",
                                     "float16", "float32", "float64"]).columns.tolist()


def get_categorical_columns(df):
    """Return list of categorical/object column names."""
    return df.select_dtypes(include=["object", "category"]).columns.tolist()
