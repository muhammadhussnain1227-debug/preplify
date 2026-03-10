# preplify/split/train_test_split.py
from sklearn.model_selection import train_test_split


def split_dataset(X, y, test_size=0.2, random_state=42, stratify=None):
    """
    Split features and target into train/test sets.

    Parameters
    ----------
    X : pd.DataFrame
    y : pd.Series or array-like
    test_size : float (default 0.2)
    random_state : int (default 42)
    stratify : array-like, optional
        Used for stratified splitting (e.g. pass y for classification).

    Returns
    -------
    X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify)
