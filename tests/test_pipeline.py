import pandas as pd
import numpy as np
from preplify import PreplifyPipeline
from preplify.datasets.demo_datasets import load_sample_classification


def test_pipeline_runs():
    df = load_sample_classification(n=100)
    df = df.drop(columns=["target"])
    pipe = PreplifyPipeline(feature_engineering=False)
    result = pipe.fit_transform(df)
    assert result.shape[0] > 0
    assert result.isnull().sum().sum() == 0


def test_pipeline_label_encoding():
    df = load_sample_classification(n=100)
    df = df.drop(columns=["target"])
    pipe = PreplifyPipeline(encoding="label")
    result = pipe.fit_transform(df)
    assert result.select_dtypes(include=["object"]).shape[1] == 0
