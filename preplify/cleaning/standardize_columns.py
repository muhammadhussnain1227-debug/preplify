# preplify/cleaning/standardize_columns.py
import re
from ..utils.dataframe_validator import validate_dataframe
from ..utils.logging import log_info


def standardize_columns(df):
    """
    Standardize column names:
    - Strip whitespace
    - Lowercase
    - Replace spaces and special characters with underscores
    - Remove consecutive underscores
    """
    validate_dataframe(df)
    df = df.copy()
    new_cols = []
    for col in df.columns:
        col = str(col).strip().lower()
        col = re.sub(r"[^a-z0-9]+", "_", col)
        col = re.sub(r"_+", "_", col).strip("_")
        new_cols.append(col)
    df.columns = new_cols
    log_info("standardize_columns: column names standardized.")
    return df
