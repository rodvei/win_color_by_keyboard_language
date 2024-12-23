from pystray import Icon, Menu, MenuItem
from config.logic import get_icon


# Handle quitting the application
def on_quit(icon):
    print("Exiting...")
    icon.stop()
    # Add any additional cleanup logic here, if necessary

def front_end_main():
    # Define the menu
    menu = Menu(MenuItem('Quit', lambda icon: on_quit(icon)))
    icon = Icon(
        "KeyboardLang",
        get_icon(),
        "Keyboard Language",
        menu
    )
    icon.run()