from PIL import Image
from back_end.resource_utils import resource_path

def get_icon():
    icon_path = resource_path(r"../assets/system_tray_icon.png")
    icon = Image.open(icon_path)
    return icon