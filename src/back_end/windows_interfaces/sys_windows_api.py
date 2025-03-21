import os
import ctypes
import win32con
import logging
from PIL import Image
import matplotlib.colors as mcolors
from back_end.resource_utils import resource_path

logger = logging.getLogger(__name__)

# def hash_to_idx(string, idx_len):
# 	hash_idx = hash(string)%idx_len
# 	return(hash_idx)


class ColorMaper(object):
	hex_colors = ['#141414'] + list(mcolors.TABLEAU_COLORS.values())[1:]

	def __init__(self) -> None:
		self.background_img_path = self._get_img_folder_path()
		self.screen_size = self._get_screen_size()
		self.get_file_path(self._clean_filename('English - United States'))

	def get_file_path(self, text):
		text = self._clean_filename(text)
		file_path = os.path.join(self.background_img_path, f'{text}.png')
		if not os.path.exists(file_path):
			logging.info(f'No color for {text} exists, creating new background...')
			col_numb = len(os.listdir(self.background_img_path))
			self._create_img(file_path, col_numb)
			logging.info(f'Background for {text} created')
		return(file_path)

	def _clean_filename(self, text):
		# regex:
		# value = re.sub(r'[^\w\s-]', '', value.lower())
    	# re.sub(r'[-\s]+', '-', value).strip('-_')
		clean_text = text.lower().replace(' ', '')
		clean_text = clean_text.replace('.', '')
		clean_text = clean_text.replace('(', '')
		clean_text = clean_text.replace(')', '')
		clean_text = clean_text.replace('æ', 'ae')
		clean_text = clean_text.replace('ø', 'oe')
		clean_text = clean_text.replace('å', 'aa')
		return(clean_text)
	
	def _create_img(self, file_path, numb):
		im = Image.new("RGB", self.screen_size, self.hex_colors[numb])
		im.save(file_path)
	
	def _get_screen_size(self):
		user32 = ctypes.windll.user32
		screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
		return(screen_size)
	
	def _get_img_folder_path(self):
		# background_img_path = os.path.join(os.getcwd(), "background_img")
		background_img_path = resource_path(r'../assets/background_img')

		# Check if the folder exists, create it if not
		if not os.path.exists(background_img_path):
			os.makedirs(background_img_path)
		return background_img_path



class BackgroundHandler(object):
	def __init__(self) -> None:
		self.color_maper = ColorMaper()
	
	def action(self, text):
		rel_img_path = self.color_maper.get_file_path(text)
		full_img_path = os.path.abspath(rel_img_path)
		logger.debug(f'win32con.SPIF_UPDATEINIFILE "{win32con.SPIF_UPDATEINIFILE}"')
		logger.debug(f'win32con.SPIF_SENDCHANGE "{win32con.SPIF_SENDCHANGE}"')
		changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
		logger.debug(f'Changed option: "{changed}"')
		ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, full_img_path, changed)
