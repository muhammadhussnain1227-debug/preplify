# preplify/outliers/iqr_detector.py
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def remove_outliers_iqr(df, columns=None):
    """
    Remove rows where numeric column values fall outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR].

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to check. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)
    before = len(df)
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    df = df.reset_index(drop=True)
    log_info(f"remove_outliers_iqr: removed {before - len(df)} outlier row(s).")
    return df
