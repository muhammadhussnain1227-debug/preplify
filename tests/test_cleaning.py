import pandas as pd
import pytest
from preplify import remove_duplicates, remove_empty_rows, standardize_columns


def test_remove_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    result = remove_duplicates(df)
    assert len(result) == 2


def test_remove_empty_rows():
    df = pd.DataFrame({"a": [1, None, 3], "b": [None, None, 4]})
    result = remove_empty_rows(df)
    assert len(result) == 2  # row [None, None] removed


def test_standardize_columns():
    df = pd.DataFrame({"First Name": [1], "  Age ": [2], "ZIP Code!": [3]})
    result = standardize_columns(df)
    assert list(result.columns) == ["first_name", "age", "zip_code"]
