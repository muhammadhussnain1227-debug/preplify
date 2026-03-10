# preplify/utils/column_detector.py
from .dataframe_validator import get_numeric_columns, get_categorical_columns


def detect_numeric_columns(df):
    """Detect and return numeric column names."""
    return get_numeric_columns(df)


def detect_categorical_columns(df):
    """Detect and return categorical/object column names."""
    return get_categorical_columns(df)
