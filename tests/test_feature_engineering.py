import pandas as pd
from preplify import auto_feature_engineering, interaction_features, ratio_features


def test_interaction_features():
    df = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    result = interaction_features(df)
    assert "a_x_b" in result.columns


def test_ratio_features():
    df = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    result = ratio_features(df)
    assert "a_ratio_b" in result.columns


def test_auto_feature_engineering():
    df = pd.DataFrame({"x": [1.0, 2.0, 3.0], "y": [4.0, 5.0, 6.0]})
    result = auto_feature_engineering(df)
    assert result.shape[1] > df.shape[1]
