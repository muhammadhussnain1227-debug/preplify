"""AutoML preprocessing demo for Preplify."""
from preplify import automl_prep
from preplify.datasets.demo_datasets import load_sample_classification

df = load_sample_classification(n=300)
X, model, score = automl_prep(df, target="target", task="classification")
print(f"Preprocessed shape: {X.shape}")
print(f"Baseline model accuracy: {score:.4f}")
