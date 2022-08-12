import sys
import time
import keyboard
import datetime
from windows_interfaces.detect_language import KeyboardLanguageDetector
from windows_interfaces.sys_windows_api import BackgroundHandler


class EventHandler:
    def __init__(self, trigger_info, actor, name=None) -> None:
        ''' trigger_info is responsible to figure out what info should be acted
        on actor is responsible for the action.
        '''
        self.name = name
        self.trigger_info = trigger_info
        self.actor = actor
    
    def run(self):
        time.sleep(0.5)
        info = self.trigger_info.get()
        self.actor.action(info)
        print(f'{datetime.datetime.now()}|{self.name}: Keyboard language set to "{info}"')


def main():
    keyboard_detector = KeyboardLanguageDetector()
    backgrund_handler = BackgroundHandler()
    event_handller = EventHandler(keyboard_detector, backgrund_handler, 'Handler#1')
    print(f'{datetime.datetime.now()}: Keyboard language taskbar color program started')
    event_handller.run()
    keyboard.add_hotkey('alt+shift', event_handller.run)
    keyboard.add_hotkey('windows+space', event_handller.run)
    keyboard.wait('ctrl+q')
    print(f'{datetime.datetime.now()}: Quiting keyboard language taskbar color program')
    keyboard.unhook_all()


if __name__=="__main__":
    main()