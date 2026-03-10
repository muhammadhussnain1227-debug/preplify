# preplify/cleaning/remove_duplicates.py
from ..utils.dataframe_validator import validate_dataframe
from ..utils.logging import log_info


def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    validate_dataframe(df)
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    removed = before - len(df)
    log_info(f"remove_duplicates: removed {removed} duplicate row(s).")
    return df
