import os
import json
import ctypes
from PIL import Image
import matplotlib.colors as mcolors

# def hash_to_idx(string, idx_len):
# 	hash_idx = hash(string)%idx_len
# 	return(hash_idx)


class ColorMaper(object):
	mapping_path = 'img'
	hex_colors = ['#141414'] + list(mcolors.TABLEAU_COLORS.values())[1:]
	def __init__(self) -> None:
		self.screen_size = self._get_screen_size()
		self.get_file_path(self._clean_filename('English - United States'))

	def get_file_path(self, text):
		text = self._clean_filename(text)
		file_path = os.path.join(self.mapping_path, f'{text}.png')
		if not os.path.exists(file_path):
			col_numb = len(os.listdir(self.mapping_path))
			self._create_img(file_path, col_numb)
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


class BackgroundHandler(object):
	SPI_SETDESKWALLPAPER = 20
	def __init__(self) -> None:
		self.color_maper = ColorMaper()
	
	def action(self, text):
		rel_img_path = self.color_maper.get_file_path(text)
		full_img_path = os.path.abspath(rel_img_path)
		ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER,0, full_img_path, 3)
