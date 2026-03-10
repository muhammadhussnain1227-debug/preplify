import pandas as pd
import numpy as np
import pytest
from preplify import handle_missing


def test_handle_missing_mean():
    df = pd.DataFrame({"a": [1.0, None, 3.0], "b": ["x", None, "z"]})
    result = handle_missing(df, strategy="mean")
    assert result["a"].isnull().sum() == 0
    assert result["b"].isnull().sum() == 0


def test_handle_missing_drop():
    df = pd.DataFrame({"a": [1.0, None, 3.0]})
    result = handle_missing(df, strategy="drop")
    assert len(result) == 2


def test_invalid_strategy():
    df = pd.DataFrame({"a": [1.0]})
    with pytest.raises(ValueError):
        handle_missing(df, strategy="unknown")
