# preplify/feature_engineering/auto_feature_engineering.py
from .interaction_features import interaction_features
from .ratio_features import ratio_features
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def auto_feature_engineering(df, max_pairs=30):
    """
    Automatically generate interaction and ratio features for numeric columns.

    Parameters
    ----------
    df : pd.DataFrame
    max_pairs : int
        Maximum number of pairs for each feature type (interaction + ratio).
    """
    validate_dataframe(df)
    num_cols = get_numeric_columns(df)
    if len(num_cols) < 2:
        log_info("auto_feature_engineering: fewer than 2 numeric columns, skipping.")
        return df

    df = interaction_features(df, columns=num_cols, max_pairs=max_pairs)
    df = ratio_features(df, columns=num_cols, max_pairs=max_pairs)
    log_info(f"auto_feature_engineering: completed. New shape: {df.shape}.")
    return df
