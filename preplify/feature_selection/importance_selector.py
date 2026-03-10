# preplify/feature_selection/importance_selector.py
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pandas as pd
from ..utils.logging import log_info


def importance_selector(X, y, top_n=10, task="classification"):
    """
    Select top N features by Random Forest feature importance.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix (must be fully numeric).
    y : pd.Series or array-like
        Target variable.
    top_n : int
        Number of top features to keep.
    task : str
        'classification' or 'regression'.

    Returns
    -------
    pd.DataFrame with selected columns.
    """
    if task == "classification":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif task == "regression":
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError("task must be 'classification' or 'regression'.")

    model.fit(X, y)
    importances = pd.Series(model.feature_importances_, index=X.columns)
    selected = importances.sort_values(ascending=False).head(top_n).index.tolist()
    log_info(f"importance_selector: selected top {len(selected)} features.")
    return X[selected]
