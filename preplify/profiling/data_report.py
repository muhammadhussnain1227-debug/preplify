# preplify/profiling/data_report.py
import pandas as pd
from .summary_stats import summary_stats
from ..utils.dataframe_validator import validate_dataframe, get_numeric_columns, get_categorical_columns
from ..utils.logging import log_info


def data_report(df, print_report=True):
    """
    Generate and optionally print a comprehensive data report.

    Parameters
    ----------
    df : pd.DataFrame
    print_report : bool
        If True, pretty-print the report to stdout.

    Returns
    -------
    dict with full report.
    """
    validate_dataframe(df)
    stats = summary_stats(df)

    report = {
        **stats,
        "numeric_columns": get_numeric_columns(df),
        "categorical_columns": get_categorical_columns(df),
        "duplicate_rows": int(df.duplicated().sum()),
        "constant_columns": [col for col in df.columns if df[col].nunique() <= 1],
    }

    if print_report:
        print("=" * 60)
        print("               PREPLIFY — DATA REPORT")
        print("=" * 60)
        print(f"  Shape            : {report['shape'][0]} rows × {report['shape'][1]} columns")
        print(f"  Numeric cols     : {len(report['numeric_columns'])}")
        print(f"  Categorical cols : {len(report['categorical_columns'])}")
        print(f"  Duplicate rows   : {report['duplicate_rows']}")
        print(f"  Constant cols    : {report['constant_columns']}")
        print("\n  Missing Values:")
        for col, cnt in report["missing_counts"].items():
            if cnt > 0:
                pct = report["missing_pct"][col]
                print(f"    {col}: {cnt} ({pct}%)")
        print("=" * 60)

    log_info("data_report: report generated.")
    return report
