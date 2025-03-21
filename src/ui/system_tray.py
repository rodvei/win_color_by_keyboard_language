import logging
from pystray import Icon, Menu, MenuItem
from ui.img_handeling import get_icon

logger = logging.getLogger(__name__)

# Handle quitting the application
def on_quit(icon):
    print("Exiting...")
    icon.stop()
    # Add any additional cleanup logic here, if necessary

def front_end_main():
    # Define the menu
    logging.info("Starting front-end processes...")
    menu = Menu(MenuItem('Quit', lambda icon: on_quit(icon)))
    icon = Icon(
        "KeyboardLang",
        get_icon(),
        "Keyboard Language",
        menu
    )
    icon.run()
    logging.info("Front-end processes are running!")