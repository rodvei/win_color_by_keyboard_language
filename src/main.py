import os
import logging
from back_end.logging_utils import setup_logging
from back_end.logic import back_end_main
from ui.system_tray import front_end_main

# fix Windows + L lock
# https://pypi.org/project/global-hotkeys/
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

setup_logging()
logger = logging.getLogger(__name__)

def main():
    """
    Main application entry point.

    Handles the initialization of the back end and front end for the keyboard language detection app.
    - Back End: Monitors keyboard input and performs background logic.
    - Front End: Provides a system tray interface for user interaction.
    """
    back_end_main()
    front_end_main()

if __name__=="__main__":
    main()
