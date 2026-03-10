# preplify/core/auto.py
from .pipeline import PreplifyPipeline
from ..utils.logging import log_info


def auto_prep(df, feature_engineering=False):
    """
    One-line automatic preprocessing using sensible defaults.

    Steps: standardize columns → remove duplicates/empty rows →
           handle missing (mean) → remove IQR outliers →
           one-hot encode → standard scale.

    Parameters
    ----------
    df : pd.DataFrame
    feature_engineering : bool
        Whether to add interaction/ratio features (default False).

    Returns
    -------
    pd.DataFrame
    """
    log_info("auto_prep: running automatic preprocessing.")
    pipe = PreplifyPipeline(feature_engineering=feature_engineering)
    return pipe.fit_transform(df)
