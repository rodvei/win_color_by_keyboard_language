import logging
from config.set_logging import setup_logging
from back_end.logic import back_end_main
from front_end.system_tray import front_end_main

# fix Windows + L lock
# https://pypi.org/project/global-hotkeys/

setup_logging()
logger = logging.getLogger(__name__)

def main():
    back_end_main()
    front_end_main()

if __name__=="__main__":
    main()
