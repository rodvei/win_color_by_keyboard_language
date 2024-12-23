import time
import logging
import threading
import datetime
from pynput  import keyboard
from windows_interfaces.detect_language import KeyboardLanguageDetector
from windows_interfaces.sys_windows_api import BackgroundHandler

logger = logging.getLogger(__name__)

class EventHandler(object):
    def __init__(self, trigger_info, actor):
        self.trigger_info = trigger_info
        self.actor = actor


class KeyboardLanguageHandler(EventHandler):
    def __init__(self, detect_language, change_background, name=None) -> None:
        ''' trigger_info is responsible to figure out what info should be acted
        on actor is responsible for the action.
        '''
        super().__init__(detect_language, change_background)
        self.name = name
        self.last_language = None
    
    def run(self):
        time.sleep(0.5)
        current_language = self.trigger_info.get()
        if current_language != self.last_language:
            self.actor.action(current_language)
        logger.info(f'{self.name}: Keyboard language set to "{current_language}"')

def periodic_check(interval=5, name='Periodic_trigger'):
    """Periodically checks the keyboard language."""
    keyboard_detector = KeyboardLanguageDetector()
    backgrund_handler = BackgroundHandler()
    event_handler = KeyboardLanguageHandler(keyboard_detector, backgrund_handler, name)
    while True:
        event_handler.run()
        time.sleep(interval)

def start_language_background_handler(name='Keyboard_trigger'):
    keyboard_detector = KeyboardLanguageDetector()
    backgrund_handler = BackgroundHandler()
    event_handler = KeyboardLanguageHandler(keyboard_detector, backgrund_handler, name)
    logger.info(f'Keyboard language background handler started')
    # Check current state and change
    # event_handler.run()
    # keyboard.add_hotkey('alt+shift', event_handler.run)
    # keyboard.add_hotkey('windows+space', event_handller.run)
    # Event listener
    def on_press(key):
        if key in [keyboard.Key.alt, keyboard.Key.shift, keyboard.Key.cmd]:
            event_handler.run()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def back_end_main():
    # Start periodic check thread
    threading.Thread(target=periodic_check, args=(3, ), daemon=True).start()
    threading.Thread(target=start_language_background_handler, daemon=True).start()
    # keyboard.wait('ctrl+q')
    # print(f'{datetime.datetime.now()}: Quiting keyboard language taskbar color program')
    # keyboard.unhook_all()