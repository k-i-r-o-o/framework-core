from functools import wraps
from core.telemetry.logger import get_logger

def auto_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger(func.__module__)
        logger.debug(f"➡️ Entering {func.__qualname__}")
        result = func(*args, **kwargs)
        logger.debug(f"⬅️ Exiting {func.__qualname__}")
        return result
    return wrapper

def auto_log_class(cls):
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith("__"):
            setattr(cls, attr_name, auto_log(attr))
    return cls
