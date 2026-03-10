# preplify/cleaning/remove_empty_rows.py
from ..utils.dataframe_validator import validate_dataframe
from ..utils.logging import log_info


def remove_empty_rows(df):
    """Remove rows where ALL values are NaN/None."""
    validate_dataframe(df)
    before = len(df)
    df = df.dropna(how="all").reset_index(drop=True)
    removed = before - len(df)
    log_info(f"remove_empty_rows: removed {removed} fully-empty row(s).")
    return df
