# preplify/scaling/standard_scaler.py
from sklearn.preprocessing import StandardScaler
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def scale_features(df, method="standard", columns=None):
    """
    Scale numeric features.

    Parameters
    ----------
    df : pd.DataFrame
    method : str
        'standard', 'minmax', or 'robust'
    columns : list, optional
        Columns to scale. Defaults to all numeric columns.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)
    if not columns:
        return df

    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
    scalers = {
        "standard": StandardScaler(),
        "minmax": MinMaxScaler(),
        "robust": RobustScaler(),
    }
    if method not in scalers:
        raise ValueError(f"Invalid scaling method '{method}'. Choose from: {list(scalers.keys())}.")

    scaler = scalers[method]
    df[columns] = scaler.fit_transform(df[columns])
    log_info(f"scale_features: applied '{method}' scaling to {len(columns)} column(s).")
    return df
