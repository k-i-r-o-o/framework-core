import logging
import os
from core.telemetry.json_formatter import JSONLogFormatter
from core.telemetry.text_formatter import TextLogFormatter

def get_logger(name: str = None) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # prevent duplicate handlers

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_format = os.getenv("LOG_FORMAT", "plain").lower()

    logger.setLevel(log_level)

    handler = logging.StreamHandler()
    if log_format == "json":
        handler.setFormatter(JSONLogFormatter())
    else:
        handler.setFormatter(TextLogFormatter())

    logger.addHandler(handler)
    return logger
