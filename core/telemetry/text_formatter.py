import logging
import os

COLORS = {
    "DEBUG": "\033[94m",     # Blue
    "INFO": "\033[92m",      # Green
    "WARNING": "\033[93m",   # Yellow
    "ERROR": "\033[91m",     # Red
    "CRITICAL": "\033[95m",  # Magenta
    "ENDC": "\033[0m",       # Reset
}

class TextLogFormatter(logging.Formatter):
    def format(self, record):
        color = COLORS.get(record.levelname, "")
        endc = COLORS["ENDC"]
        record.env = os.getenv("ENV", "DEV").upper()

        log_line = f"{color}[{record.levelname}] [{record.env}] {record.name} - {record.funcName}: {record.getMessage()}{endc}"
        return log_line
