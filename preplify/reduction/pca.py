# preplify/reduction/pca.py
from sklearn.decomposition import PCA
import pandas as pd
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns
from ..utils.logging import log_info


def apply_pca(df, n_components=0.95, columns=None):
    """
    Apply PCA dimensionality reduction on numeric columns.

    Parameters
    ----------
    df : pd.DataFrame
    n_components : int or float
        Number of components (int) or explained variance ratio to retain (float, default 0.95).
    columns : list, optional
        Columns to apply PCA on. Defaults to all numeric columns.
        Non-numeric columns are preserved alongside PCA output.

    Returns
    -------
    pd.DataFrame with PCA components and any non-numeric columns.
    """
    validate_dataframe(df)
    if columns is None:
        columns = get_numeric_columns(df)

    pca = PCA(n_components=n_components)
    pca_array = pca.fit_transform(df[columns])
    n_kept = pca_array.shape[1]

    pca_df = pd.DataFrame(
        pca_array,
        columns=[f"PC{i + 1}" for i in range(n_kept)],
        index=df.index
    )

    non_numeric = [c for c in df.columns if c not in columns]
    result = pd.concat([df[non_numeric].reset_index(drop=True), pca_df.reset_index(drop=True)], axis=1)
    log_info(f"apply_pca: reduced {len(columns)} columns → {n_kept} principal component(s).")
    return result
