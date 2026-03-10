# preplify/missing/validators.py

VALID_STRATEGIES = {"mean", "median", "mode", "drop", "constant"}


def validate_strategy(strategy):
    """Raise ValueError for unsupported missing-value strategies."""
    if strategy not in VALID_STRATEGIES and not (
        isinstance(strategy, dict)
    ):
        raise ValueError(
            f"Invalid strategy '{strategy}'. "
            f"Choose from: {sorted(VALID_STRATEGIES)} or pass a dict mapping columns to strategies."
        )
