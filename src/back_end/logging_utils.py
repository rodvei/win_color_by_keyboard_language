import os
import sys
import logging
from back_end.settings import get_settings

def setup_logging():
    # Check if running inside a PyInstaller executable
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        log_level = logging.ERROR  # Production level when bundled
    else:
        log_level = logging.DEBUG  # Development level

    # Configure logging
    log_settings = get_settings()['logging']
    logging.basicConfig(level=log_level, **log_settings)
    logging.info(f"Log level set to: {logging.getLevelName(log_level)}")
