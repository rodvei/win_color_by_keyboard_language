import ctypes
import json


class KeyboardLanguageDetector(object):
    settings_path = 'settings.json'
    
    def __init__(self) -> None:
         with open(self.settings_path, 'r') as f:
            self.hex_to_language = json.load(f)['hex_to_language']

    def get(self):
        return(self.get_keyboard_language())
    
    def get_keyboard_language(self):
        layout_id = self._get_keyboard_layout_id()
        hex = self._layout_id_to_hex(layout_id)
        language = self._hex_to_language(hex)
        return(language)

    def _get_keyboard_layout_id(self):
        """
        Gets the keyboard language in use by the current
        active window process.
        """
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        # Get the current active window handle
        handle = user32.GetForegroundWindow()
        # Get the thread id from that window handle
        thread_id = user32.GetWindowThreadProcessId(handle, 0)
        # Get the keyboard layout id from the threadid
        layout_id = user32.GetKeyboardLayout(thread_id)
        return(layout_id)
    
    def _layout_id_to_hex(self, layout_id):
        # Extract the keyboard language id from the keyboard layout id
        language_id = layout_id & (2 ** 16 - 1)
        # Convert the keyboard language id from decimal to hexadecimal
        language_id_hex = hex(language_id)
        return(language_id_hex)
    
    def _hex_to_language(self, language_id_hex):
        # Check if the hex value is in the dictionary.
        language = self.hex_to_language.get(language_id_hex, str(language_id_hex))
        return(language)



