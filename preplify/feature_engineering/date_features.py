# preplify/feature_engineering/date_features.py
import pandas as pd
from ..utils.dataframe_validator import validate_dataframe
from ..utils.logging import log_info, log_warning


def extract_date_features(df, date_columns, drop_original=False):
    """
    Extract year, month, day, weekday, hour, and is_weekend from datetime columns.

    Parameters
    ----------
    df : pd.DataFrame
    date_columns : list
        Column names containing datetime data.
    drop_original : bool
        If True, drop the original datetime column after extraction.
    """
    validate_dataframe(df)
    df = df.copy()
    for col in date_columns:
        if col not in df.columns:
            log_warning(f"extract_date_features: column '{col}' not found, skipping.")
            continue
        try:
            df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
        except Exception as e:
            log_warning(f"extract_date_features: could not parse '{col}' as datetime: {e}")
            continue

        df[f"{col}_year"]       = df[col].dt.year
        df[f"{col}_month"]      = df[col].dt.month
        df[f"{col}_day"]        = df[col].dt.day
        df[f"{col}_weekday"]    = df[col].dt.weekday
        df[f"{col}_is_weekend"] = (df[col].dt.weekday >= 5).astype(int)
        if df[col].dt.hour.any():
            df[f"{col}_hour"]   = df[col].dt.hour

        if drop_original:
            df = df.drop(columns=[col])

    log_info(f"extract_date_features: processed {len(date_columns)} date column(s).")
    return df
