import json
from back_end.resource_utils import resource_path

def get_settings():
    settings_path = resource_path(r"../assets/default_settings.json")
    with open(settings_path, 'r') as f:
        settings = json.load(f)
    return settings