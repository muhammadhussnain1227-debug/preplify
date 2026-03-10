# preplify/datasets/demo_datasets.py
import pandas as pd
import numpy as np


def load_titanic():
    """Load the Titanic dataset from a public source."""
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    try:
        df = pd.read_csv(url)
        return df
    except Exception:
        # Fallback: tiny synthetic version
        return _synthetic_titanic()


def load_sample_regression(n=200, random_state=42):
    """
    Generate a simple synthetic regression dataset.

    Returns
    -------
    pd.DataFrame with numeric features and a continuous target.
    """
    rng = np.random.RandomState(random_state)
    df = pd.DataFrame({
        "feature_1": rng.randn(n),
        "feature_2": rng.rand(n) * 10,
        "feature_3": rng.randint(1, 5, size=n).astype(float),
        "category": rng.choice(["A", "B", "C"], size=n),
        "target": rng.randn(n) * 5 + 10,
    })
    # Introduce some missing values
    df.loc[rng.choice(n, 10, replace=False), "feature_1"] = np.nan
    df.loc[rng.choice(n, 5, replace=False), "category"] = np.nan
    return df


def load_sample_classification(n=200, random_state=42):
    """
    Generate a simple synthetic binary classification dataset.

    Returns
    -------
    pd.DataFrame with features and a binary target column.
    """
    rng = np.random.RandomState(random_state)
    df = pd.DataFrame({
        "age": rng.randint(18, 70, size=n).astype(float),
        "income": rng.rand(n) * 100000,
        "score": rng.randn(n),
        "gender": rng.choice(["M", "F"], size=n),
        "target": rng.randint(0, 2, size=n),
    })
    df.loc[rng.choice(n, 8, replace=False), "age"] = np.nan
    return df


def _synthetic_titanic():
    """Tiny synthetic Titanic-like fallback."""
    rng = np.random.RandomState(0)
    n = 100
    return pd.DataFrame({
        "PassengerId": range(1, n + 1),
        "Survived": rng.randint(0, 2, n),
        "Pclass": rng.choice([1, 2, 3], n),
        "Name": [f"Passenger_{i}" for i in range(n)],
        "Sex": rng.choice(["male", "female"], n),
        "Age": np.where(rng.rand(n) < 0.2, np.nan, rng.randint(1, 80, n).astype(float)),
        "SibSp": rng.randint(0, 5, n),
        "Parch": rng.randint(0, 3, n),
        "Fare": rng.rand(n) * 200,
        "Embarked": rng.choice(["S", "C", "Q", None], n),
    })
