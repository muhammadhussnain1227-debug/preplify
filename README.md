<div align="center">

# 🚀 Preplify

### The Last Preprocessing Library You'll Ever Need

**Preprocess any tabular dataset in one line — clean, encode, scale, engineer, and ML-ready.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.2-orange?style=for-the-badge)](https://github.com/yourusername/preplify)
[![sklearn](https://img.shields.io/badge/sklearn-compatible-red?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)

```python
# From messy raw data to ML-ready in ONE line
df_clean = auto_prep(df)
```

![Before vs After](Before%20vs%20After.png)

---

## 📌 What is Preplify?

**Preplify** is a modular, professional Python library for **tabular data preprocessing**. Whether you're a beginner who wants everything handled automatically, or an advanced user who wants full control over every step — Preplify has you covered.

> No more writing 100 lines of boilerplate preprocessing code. Preplify does it all.

---

## ✨ Features at a Glance

| Module | What it does |
|---|---|
| 🧹 **Cleaning** | Remove duplicates, empty rows, fix column names |
| ❓ **Missing Values** | Mean / Median / Mode / Drop / Constant strategies |
| 📊 **Outlier Removal** | IQR and Z-score based detection |
| 🔠 **Encoding** | One-Hot and Label encoding |
| 📏 **Scaling** | Standard, Min-Max, Robust scaling |
| 🔄 **Transformation** | Log and Power transforms |
| ⚙️ **Feature Engineering** | Interaction, Ratio, and DateTime features |
| 🎯 **Feature Selection** | Correlation filter, Variance filter, Importance selector |
| 📉 **Dimensionality Reduction** | PCA |
| 🔍 **Profiling** | Full data report + summary stats |
| 💡 **Recommender** | Auto-suggests best preprocessing steps |
| 🤖 **AutoML** | Preprocess + train baseline model in one call |
| 🔧 **Pipeline** | Custom modular pipeline with full control |

---

## ⚡ Installation

```bash
pip install -e .
```

**Requirements:**
```bash
pip install pandas numpy scikit-learn
```

> Python 3.8+ required

---

## 🚀 Quick Start

### One-Line Preprocessing
```python
import pandas as pd
from preplify import auto_prep

df = pd.read_csv("your_dataset.csv")
df_clean = auto_prep(df)
print(df_clean.shape)
```

### See What Your Data Needs First
```python
from preplify import recommend_preprocessing, data_report

_ = recommend_preprocessing(df)   # get smart suggestions
_ = data_report(df)                # full data overview
```

<div align="center">
  <img src="Data%20Report.png" width="700"/>
  <img src="Processing%20Recommendations.png" width="700"/>
</div>

### Train a Baseline Model Instantly
```python
from preplify import automl_prep

X, model, score = automl_prep(df, target="Survived", task="classification")
print(f"Accuracy: {score:.4f}")
```

---

## 🔧 Full API Reference

### 📦 Load Demo Data
```python
from preplify.datasets.demo_datasets import (
    load_sample_classification,   # fake classification dataset
    load_sample_regression,       # fake regression dataset
    load_titanic                  # real Titanic CSV (needs internet)
)

df = load_sample_classification()
df = load_sample_regression()
df = load_titanic()
```

---

### 🔍 Profiling
```python
from preplify import data_report, recommend_preprocessing

_ = data_report(df)             # shape, missing, dtypes, duplicates
_ = recommend_preprocessing(df) # smart preprocessing suggestions
```

---

### 🧹 Cleaning
```python
from preplify import remove_duplicates, remove_empty_rows, standardize_columns

df = standardize_columns(df)   # "First Name" → "first_name"
df = remove_duplicates(df)     # drop repeated rows
df = remove_empty_rows(df)     # drop fully empty rows
```

---

### ❓ Missing Values
```python
from preplify import handle_missing

df = handle_missing(df, strategy="mean")              # fill with average
df = handle_missing(df, strategy="median")            # fill with middle value
df = handle_missing(df, strategy="mode")              # fill with most frequent
df = handle_missing(df, strategy="drop")              # drop rows with missing
df = handle_missing(df, strategy="constant", fill_value=0)  # fill with 0
```

---

### 📊 Outlier Removal
```python
from preplify import remove_outliers, remove_outliers_iqr, remove_outliers_zscore

df = remove_outliers(df, method="iqr")          # IQR method (recommended)
df = remove_outliers(df, method="zscore")       # Z-score method
df = remove_outliers_iqr(df)                    # direct IQR
df = remove_outliers_zscore(df, threshold=3)    # direct Z-score
```

---

### 🔠 Encoding
```python
from preplify import encode_features, onehot_encode, label_encode

df = encode_features(df, method="onehot")   # "Male/Female" → 2 columns
df = encode_features(df, method="label")    # "Male/Female" → 0/1
df = onehot_encode(df)                      # direct one-hot
df = label_encode(df)                       # direct label encoding
```

---

### 📏 Scaling
```python
from preplify import scale_features, minmax_scale, robust_scale

df = scale_features(df, method="standard")  # mean=0, std=1
df = scale_features(df, method="minmax")    # values between 0 and 1
df = scale_features(df, method="robust")    # outlier-resistant scaling
df = minmax_scale(df)                       # shortcut minmax
df = robust_scale(df)                       # shortcut robust
```

---

### 🔄 Transformation
```python
from preplify import log_transform, power_transform

df = log_transform(df)                           # log1p — fix skewed data
df = power_transform(df, method="yeo-johnson")   # works with negatives too
df = power_transform(df, method="box-cox")       # positive values only
```

---

### ⚙️ Feature Engineering
```python
from preplify import (
    auto_feature_engineering,
    interaction_features,
    ratio_features,
    extract_date_features
)

df = auto_feature_engineering(df)                      # auto interaction + ratio
df = interaction_features(df)                          # age * income → age_x_income
df = ratio_features(df)                                # income / age → income_ratio_age
df = extract_date_features(df, date_columns=["date"])  # year, month, day, weekday, is_weekend
```

---

### 🎯 Feature Selection
```python
from preplify import correlation_filter, variance_filter, importance_selector

df = correlation_filter(df, threshold=0.9)   # drop columns that are 90%+ similar
df = variance_filter(df, threshold=0.01)     # drop near-constant columns
X  = importance_selector(X, y, top_n=10)    # keep top 10 by Random Forest importance
```

---

### 📉 Dimensionality Reduction
```python
from preplify import apply_pca

df = apply_pca(df, n_components=0.95)   # keep 95% of variance
df = apply_pca(df, n_components=3)      # reduce to exactly 3 components
```

---

### ✂️ Train-Test Split
```python
from preplify import split_dataset

X_train, X_test, y_train, y_test = split_dataset(X, y, test_size=0.2)
```

---

### 🔧 Custom Pipeline
Full control over every single step:
```python
from preplify import PreplifyPipeline

pipe = PreplifyPipeline(
    missing_strategy="median",     # mean / median / mode / drop / constant
    encoding="onehot",             # onehot / label
    scaling="robust",              # standard / minmax / robust
    outlier_method="iqr",          # iqr / zscore / None
    feature_engineering=True       # True / False
)

df_clean = pipe.fit_transform(df)
```

---

### 🤖 AutoML — Preprocess + Train in One Call
```python
from preplify import automl_prep

# Classification
X, model, score = automl_prep(df, target="Survived", task="classification")
print(f"Accuracy: {score:.4f}")

# Regression
X, model, score = automl_prep(df, target="Price", task="regression")
print(f"R² Score: {score:.4f}")
```

| Task | Model Used | Score Metric |
|---|---|---|
| classification | Logistic Regression | Accuracy |
| regression | Ridge Regression | R² Score |

---

## 🌍 Real Dataset Example (Titanic)

```python
import pandas as pd
from preplify import auto_prep, recommend_preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load
df = pd.read_csv("titanic.csv")

# Explore
_ = recommend_preprocessing(df)

# Preprocess
target = df["Survived"]
df_clean = auto_prep(df.drop(columns=["Survived"]))

# Train Random Forest
X_train, X_test, y_train, y_test = train_test_split(df_clean, target, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(f"Accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")
```

---

## 🗂️ Project Structure

```
preplify/
│
├── preplify/
│   ├── core/              # Pipeline, auto_prep, automl_prep
│   ├── cleaning/          # Duplicates, empty rows, column names
│   ├── missing/           # Missing value strategies
│   ├── outliers/          # IQR and Z-score detection
│   ├── encoding/          # One-hot and label encoding
│   ├── scaling/           # Standard, MinMax, Robust
│   ├── transformation/    # Log and Power transforms
│   ├── feature_engineering/  # Interaction, ratio, date features
│   ├── feature_selection/ # Correlation, variance, importance
│   ├── reduction/         # PCA
│   ├── split/             # Train-test split
│   ├── profiling/         # Data report, summary stats
│   ├── recommender/       # Preprocessing recommendations
│   ├── datasets/          # Demo datasets
│   └── utils/             # Validators, logging, helpers
│
├── examples/              # Ready-to-run example scripts
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── setup.py
└── README.md
```

---

## 🔕 Disable Logs

By default Preplify logs every step. To turn off:

```python
import logging
logging.getLogger("preplify").setLevel(logging.WARNING)
```

---

## 🧪 Run Tests

```bash
pip install pytest
pytest tests/
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

**Muhammad Hussnain**
- 📧 muhammadhussnain1227@gmail.com
- ⭐ [GitHub Repo](https://github.com/muhammadhussnain1227-debug/preplify?tab=readme-ov-file)
- 🐙 [GitHub Profile](https://github.com/muhammadhussnain1227-debug)
- 💼 [Linkedin Profile](https://www.linkedin.com/in/muhammad-hussnain-28861537a/)

---

<div align="center">

**If Preplify saved you time, give it a ⭐ on GitHub!**

</div>
