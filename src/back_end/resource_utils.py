import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    #base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    file_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    main_path = os.path.join(''.join(file_path.split('src')[:-1]), 'src')
    full_path = os.path.normpath(os.path.join(main_path, relative_path))
    return full_path