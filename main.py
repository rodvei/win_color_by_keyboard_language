import sys
import time
import keyboard
import datetime
from windows_interfaces.detect_language import get_keyboard_layout_id, layout_id_to_hex, hex_to_language
from windows_interfaces.sys_windows_api import set_background

def handle_taskbar_color()->None:
    time.sleep(0.5)
    layout_id = get_keyboard_layout_id()
    hex = layout_id_to_hex(layout_id)
    language = hex_to_language(hex)
    print(f'{datetime.datetime.now()}: Keyboard language set to "{language}"')
    set_background(hex)

def detect_language_change():
    # https://pypi.org/project/keyboard/
    keyboard.wait('alt+shift') # also 'windows+space'

class EventHandler:
    def __init__(self, trigger, action) -> None:
        self.trigger = trigger
        self.action = action
    
    def run():
        pass


# def main():
#     while True:
#         detect_language_change()
#         time.sleep(1)
#         handle_taskbar_color()

def main():
    print(f'{datetime.datetime.now()}: Keyboard language taskbar color program started')
    handle_taskbar_color()
    keyboard.add_hotkey('alt+shift', handle_taskbar_color)
    keyboard.add_hotkey('windows+space', handle_taskbar_color)
    keyboard.wait('ctrl+q')
    print(f'{datetime.datetime.now()}: Quiting keyboard language taskbar color program')

if __name__=="__main__":
    main()