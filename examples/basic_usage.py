"""Basic usage example for Preplify."""
from preplify import auto_prep, data_report, recommend_preprocessing
from preplify.datasets.demo_datasets import load_sample_classification

df = load_sample_classification(n=300)
print("Original shape:", df.shape)

recommend_preprocessing(df)
data_report(df)

df_clean = auto_prep(df)
print("Cleaned shape:", df_clean.shape)
