import os
import json
import ctypes as ctypes

with open('settings.json', 'r') as f:
  settings = json.load(f)['background_img']

def set_background(hex: str)->None:
    SPI_SETDESKWALLPAPER=20
    img_path = settings[hex]
    full_img_path = os.path.abspath(img_path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, full_img_path, 3)