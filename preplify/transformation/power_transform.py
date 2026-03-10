# preplify/transformation/power_transform.py
from sklearn.preprocessing import PowerTransformer
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def power_transform(df, method="yeo-johnson", columns=None):
    """
    Apply power transformation (Yeo-Johnson or Box-Cox) to normalize distributions.

    Parameters
    ----------
    df : pd.DataFrame
    method : str
        'yeo-johnson' (supports negative values) or 'box-cox' (requires positive values).
    columns : list, optional
        Columns to transform. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)
    if not columns:
        return df

    pt = PowerTransformer(method=method)
    df[columns] = pt.fit_transform(df[columns])
    log_info(f"power_transform: applied '{method}' to {len(columns)} column(s).")
    return df
