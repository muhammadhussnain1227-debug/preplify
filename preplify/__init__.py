# preplify/__init__.py

# Core pipeline
from .core.pipeline import PreplifyPipeline
from .core.auto import auto_prep
from .core.automl_prep import automl_prep

# Cleaning
from .cleaning.remove_duplicates import remove_duplicates
from .cleaning.remove_empty_rows import remove_empty_rows
from .cleaning.standardize_columns import standardize_columns

# Missing values
from .missing.handle_missing import handle_missing

# Outliers
from .outliers.iqr_detector import remove_outliers_iqr
from .outliers.zscore_detector import remove_outliers_zscore
from .outliers.outlier_removal import remove_outliers

# Encoding
from .encoding.auto_encoder import encode_features
from .encoding.onehot_encoder import onehot_encode
from .encoding.label_encoder import label_encode

# Scaling
from .scaling.standard_scaler import scale_features
from .scaling.minmax_scaler import minmax_scale
from .scaling.robust_scaler import robust_scale

# Transformation
from .transformation.log_transform import log_transform
from .transformation.power_transform import power_transform

# Feature engineering
from .feature_engineering.auto_feature_engineering import auto_feature_engineering
from .feature_engineering.interaction_features import interaction_features
from .feature_engineering.ratio_features import ratio_features
from .feature_engineering.date_features import extract_date_features

# Feature selection
from .feature_selection.correlation_filter import correlation_filter
from .feature_selection.variance_filter import variance_filter
from .feature_selection.importance_selector import importance_selector

# Reduction
from .reduction.pca import apply_pca

# Split
from .split.train_test_split import split_dataset

# Profiling
from .profiling.data_report import data_report
from .profiling.summary_stats import summary_stats

# Recommender
from .recommender.preprocessing_recommender import recommend_preprocessing

# Utils
from .utils.dataframe_validator import validate_dataframe, get_numeric_columns, get_categorical_columns
from .utils.column_detector import detect_numeric_columns, detect_categorical_columns
from .utils.logging import log_info, log_error
from .utils.helpers import safe_divide

# Datasets
from .datasets.demo_datasets import load_titanic, load_sample_regression, load_sample_classification

__version__ = "1.0.0"
__author__ = "Muhammad Hussnain"
