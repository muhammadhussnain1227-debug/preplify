# preplify/recommender/preprocessing_recommender.py
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns, get_categorical_columns
from ..utils.logging import log_info


def recommend_preprocessing(df, print_recommendations=True):
    """
    Analyze a DataFrame and recommend preprocessing steps.

    Parameters
    ----------
    df : pd.DataFrame
    print_recommendations : bool
        If True, print recommendations to stdout.

    Returns
    -------
    list of recommendation strings.
    """
    validate_dataframe(df)
    recommendations = []

    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)
    total_missing = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    if duplicate_rows > 0:
        recommendations.append(f"✔ Remove duplicates — {duplicate_rows} duplicate row(s) found.")

    if total_missing > 0:
        recommendations.append(
            f"✔ Handle missing values — {total_missing} missing cell(s) detected "
            f"({(total_missing / df.size * 100):.1f}% of data)."
        )

    if cat_cols:
        recommendations.append(
            f"✔ Encode categorical columns — {len(cat_cols)} column(s): {cat_cols}."
        )

    if num_cols:
        recommendations.append(
            f"✔ Scale numeric features — {len(num_cols)} numeric column(s) found."
        )

    # Outlier detection hint
    import numpy as np
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)).sum()
        if outliers > 0:
            recommendations.append(f"✔ Handle outliers — '{col}' has {outliers} potential outlier(s) (IQR method).")

    if df.shape[1] > 15:
        recommendations.append(
            f"✔ Consider dimensionality reduction (PCA) — {df.shape[1]} features detected."
        )

    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    if constant_cols:
        recommendations.append(f"✔ Drop constant/low-variance columns: {constant_cols}.")

    if not recommendations:
        recommendations.append("✔ Dataset looks clean! No immediate preprocessing required.")

    if print_recommendations:
        print("=" * 60)
        print("         PREPLIFY — PREPROCESSING RECOMMENDATIONS")
        print("=" * 60)
        for rec in recommendations:
            print(f"  {rec}")
        print("=" * 60)

    log_info(f"recommend_preprocessing: {len(recommendations)} recommendation(s) generated.")
    return recommendations
