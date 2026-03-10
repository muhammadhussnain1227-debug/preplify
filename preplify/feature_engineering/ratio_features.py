# preplify/feature_engineering/ratio_features.py
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.helpers import safe_divide
from ..utils.logging import log_info


def ratio_features(df, columns=None, max_pairs=50):
    """
    Create pairwise ratio features between numeric columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to use. Defaults to all numeric columns.
    max_pairs : int
        Maximum number of pairs to create.
    """
    validate_dataframe(df)
    df = df.copy()
    if columns is None:
        columns = get_numeric_columns(df)

    count = 0
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if count >= max_pairs:
                break
            c1, c2 = columns[i], columns[j]
            df[f"{c1}_ratio_{c2}"] = safe_divide(df[c1].values, df[c2].values)
            count += 1

    log_info(f"ratio_features: created {count} ratio feature(s).")
    return df
