# preplify/missing/handle_missing.py
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns, get_categorical_columns
from ..utils.logging import log_info
from .validators import validate_strategy
from .strategies import fill_mean, fill_median, fill_mode, fill_constant


def handle_missing(df, strategy="mean", fill_value=0):
    """
    Handle missing values in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
    strategy : str or dict
        'mean', 'median', 'mode', 'drop', 'constant'
        Or a dict mapping column names to individual strategies.
    fill_value : scalar
        Value used when strategy='constant'.

    Returns
    -------
    pd.DataFrame
    """
    validate_dataframe(df)
    df = df.copy()

    if strategy == "drop":
        before = len(df)
        df = df.dropna().reset_index(drop=True)
        log_info(f"handle_missing: dropped {before - len(df)} row(s) with missing values.")
        return df

    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)

    if isinstance(strategy, dict):
        # Per-column strategy
        for col, strat in strategy.items():
            if col not in df.columns:
                continue
            df[col] = _apply_strategy(df[col], strat, fill_value)
    else:
        validate_strategy(strategy)
        for col in num_cols:
            df[col] = _apply_strategy(df[col], strategy, fill_value)
        # Categorical always filled with mode
        for col in cat_cols:
            df[col] = fill_mode(df[col])

    missing_left = df.isnull().sum().sum()
    log_info(f"handle_missing: strategy='{strategy}'. Remaining missing values: {missing_left}.")
    return df


def _apply_strategy(series, strategy, fill_value):
    if strategy == "mean":
        return fill_mean(series)
    elif strategy == "median":
        return fill_median(series)
    elif strategy == "mode":
        return fill_mode(series)
    elif strategy == "constant":
        return fill_constant(series, fill_value)
    else:
        raise ValueError(f"Unknown strategy '{strategy}' for column '{series.name}'.")
