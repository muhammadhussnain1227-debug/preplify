# preplify/utils/logging.py
import logging

_logger = logging.getLogger("preplify")
if not _logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s [Preplify] %(levelname)s: %(message)s"))
    _logger.addHandler(_handler)
    _logger.setLevel(logging.INFO)


def log_info(msg: str):
    """Log an informational message."""
    _logger.info(msg)


def log_warning(msg: str):
    """Log a warning message."""
    _logger.warning(msg)


def log_error(msg: str):
    """Log an error message."""
    _logger.error(msg)
