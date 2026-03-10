"""Custom pipeline example for Preplify."""
from preplify import PreplifyPipeline
from preplify.datasets.demo_datasets import load_sample_regression

df = load_sample_regression(n=200)
print("Original shape:", df.shape)

pipe = PreplifyPipeline(
    missing_strategy="median",
    encoding="label",
    scaling="minmax",
    outlier_method="zscore",
    feature_engineering=True,
)
df_clean = pipe.fit_transform(df)
print("Processed shape:", df_clean.shape)
