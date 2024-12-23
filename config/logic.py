import os
import sys
import json
from PIL import Image

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_settings():
    settings_path = resource_path("settings.json")
    with open(settings_path, 'r') as f:
        settings = json.load(f)
    return settings

def get_icon():
    icon_path = resource_path("system_tray_icon.png")
    icon = Image.open(icon_path)
    return icon