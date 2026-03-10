# preplify/core/automl_prep.py
from .pipeline import PreplifyPipeline
from ..split.train_test_split import split_dataset
from ..utils.logging import log_info
import pandas as pd


def automl_prep(
    df,
    target,
    missing_strategy="mean",
    encoding="onehot",
    scaling="standard",
    outlier_method="iqr",
    task="classification",
    test_size=0.2,
    random_state=42,
):
    """
    Automatic preprocessing + baseline model training.

    Parameters
    ----------
    df : pd.DataFrame
        Full dataset including target column.
    target : str
        Name of the target column.
    missing_strategy : str
    encoding : str
    scaling : str
    outlier_method : str or None
    task : str
        'classification' or 'regression'
    test_size : float
    random_state : int

    Returns
    -------
    X_processed : pd.DataFrame
        The preprocessed feature matrix.
    model : fitted sklearn model
    score : float
        Test set accuracy (classification) or R² (regression).
    """
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in DataFrame.")

    X = df.drop(columns=[target]).copy()
    y = df[target].copy()

    pipe = PreplifyPipeline(
        missing_strategy=missing_strategy,
        encoding=encoding,
        scaling=scaling,
        outlier_method=outlier_method,
        feature_engineering=False,
    )
    X_processed = pipe.fit_transform(X)

    # Align y after row drops in pipeline
    y = y.loc[X_processed.index] if hasattr(y, "loc") else y

    stratify = y if task == "classification" else None
    X_train, X_test, y_train, y_test = split_dataset(
        X_processed, y, test_size=test_size, random_state=random_state, stratify=stratify
    )

    if task == "classification":
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        model = LogisticRegression(max_iter=1000, random_state=random_state)
        model.fit(X_train, y_train)
        score = accuracy_score(y_test, model.predict(X_test))
        log_info(f"automl_prep: classification accuracy = {score:.4f}.")
    elif task == "regression":
        from sklearn.linear_model import Ridge
        from sklearn.metrics import r2_score
        model = Ridge(random_state=random_state)
        model.fit(X_train, y_train)
        score = r2_score(y_test, model.predict(X_test))
        log_info(f"automl_prep: regression R² = {score:.4f}.")
    else:
        raise ValueError("task must be 'classification' or 'regression'.")

    return X_processed, model, score
