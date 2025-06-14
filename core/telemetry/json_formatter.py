import logging
import json
import os

class JSONLogFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "file": record.pathname,
            "line": record.lineno,
            "function": record.funcName,
            "env": os.getenv("ENV", "DEV"),
            "message": record.getMessage(),
        }
        return json.dumps(log_record)
