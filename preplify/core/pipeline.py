# preplify/core/pipeline.py
from ..cleaning.remove_duplicates import remove_duplicates
from ..cleaning.remove_empty_rows import remove_empty_rows
from ..cleaning.standardize_columns import standardize_columns
from ..missing.handle_missing import handle_missing
from ..outliers.outlier_removal import remove_outliers
from ..encoding.auto_encoder import encode_features
from ..scaling.standard_scaler import scale_features
from ..feature_engineering.auto_feature_engineering import auto_feature_engineering
from ..utils.dataframe_validator import validate_dataframe
from ..utils.logging import log_info


class PreplifyPipeline:
    """
    A modular preprocessing pipeline for tabular data.

    Parameters
    ----------
    missing_strategy : str
        Strategy for handling missing values: 'mean', 'median', 'mode', 'drop', 'constant'.
    encoding : str
        Encoding method for categorical columns: 'onehot' or 'label'.
    scaling : str
        Scaling method: 'standard', 'minmax', or 'robust'.
    outlier_method : str or None
        Outlier removal method: 'iqr', 'zscore', or None to skip.
    feature_engineering : bool
        Whether to apply automatic feature engineering.

    Example
    -------
    >>> from preplify import PreplifyPipeline
    >>> pipe = PreplifyPipeline(scaling='minmax', encoding='label')
    >>> df_clean = pipe.fit_transform(df)
    """

    def __init__(
        self,
        missing_strategy="mean",
        encoding="onehot",
        scaling="standard",
        outlier_method="iqr",
        feature_engineering=False,
    ):
        self.missing_strategy = missing_strategy
        self.encoding = encoding
        self.scaling = scaling
        self.outlier_method = outlier_method
        self.feature_engineering = feature_engineering

    def fit_transform(self, df):
        """Run all preprocessing steps and return the cleaned DataFrame."""
        validate_dataframe(df)
        log_info("PreplifyPipeline: starting fit_transform.")

        df = standardize_columns(df)
        df = remove_duplicates(df)
        df = remove_empty_rows(df)
        df = handle_missing(df, strategy=self.missing_strategy)

        if self.outlier_method:
            df = remove_outliers(df, method=self.outlier_method)

        df = encode_features(df, method=self.encoding)
        df = scale_features(df, method=self.scaling)

        if self.feature_engineering:
            df = auto_feature_engineering(df)

        log_info(f"PreplifyPipeline: done. Final shape: {df.shape}.")
        return df
