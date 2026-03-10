# preplify/feature_engineering/interaction_features.py
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def interaction_features(df, columns=None, max_pairs=50):
    """
    Create pairwise multiplication interaction features between numeric columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to use. Defaults to all numeric columns.
    max_pairs : int
        Maximum number of pairs to create (prevents explosion with many columns).
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
            df[f"{c1}_x_{c2}"] = df[c1] * df[c2]
            count += 1

    log_info(f"interaction_features: created {count} interaction feature(s).")
    return df
