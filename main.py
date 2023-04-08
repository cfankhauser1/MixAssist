# TODO: Create master template for track order
# TODO: Load files into Luna (is this even possible?)
# TODO: keep list of number of each track type (drums, bass, keys etc)
# TODO: figure out how to read text from Luna GUI
# TODO: color code files by track type, select first item in tracks list color palate, click, move mouse to correct color, /n
#  change color, move on with arrow key
# TODO: Import Session Template
# TODO: Route
# TODO: Notify via email or text of complete session
# TODO: Close Luna


from subprocess import Popen
import pyautogui

track_list_start = (21,191)
color_pos_dict = {
    "ocean_blue": (137, 358),
    "light_blue": (119, 348),
    "blue": (102, 348),
    "dark_blue": (91, 332),
    "purple": (80, 314),
    "pink": (86, 294),
    "flamingo": (80, 276),
    "hot_pink": (104, 260),
    "red": (119, 253),
    "orange": (138, 252),
    "tangerine": (158, 259),
    "gold": (172, 275),
    "yellow": (184, 295),
    "key_lime": (182, 313),
    "green": (170, 330),
    "sea_foam": (156, 348),
    "sat_ocean_blue": (146, 386),
    "sat_light_blue": (114, 392),
    "sat_blue": (73, 377),
    "sat_dark_blue": (56, 352),
    "sat_purple": (46, 323),
    "sat_pink": (50, 281),
    "sat_flamingo": (58, 262),
    "sat_hot_pink": (77, 231),
    "sat_red": (116, 218),
    "sat_orange": (153, 220),
    "sat_tangerine": (178, 228),
    "sat_gold": (199, 247),
    "sat_yellow": (211, 285),
    "sat_key_lime": (218, 314),
    "sat_green": (198, 350),
    "sat_sea_foam": (179, 373)
}

nav_bar_dict = {
    "file": (125, 11)
}

class Sorter:
    '''sorts instruments into dict with number of occurances as values'''
    def __init__(self):
        self.tracks = []
        self.instruments_involved = []
        self.drum_keys = ["kick", "snare", "toms", "overheads", "oh", "rooms"]
        self.bass_keys = ["bass", "di_bass", "bass_amp"]
        self.guitar_keys = ["guitar", "gtr", "electric", "acoustic"]
        self.keyboard_keys = ["keys", "piano", "wurli", "synth"]
        self.lead_vox_keys = ["lead_vox", "vocals", "vox"]
        self.bg_vox_keys = ["bg_vox", "backgrounds", "harmonies", "harmony"]

    def sort(self):
        master_dict = {instrument: 0 for instrument in self.instruments_involved}





def import_template():
    pyautogui.hotkey('option', 'i', interval=0.1)
    pyautogui.write("FankTemplate1.1")
    pyautogui.press('enter')

print(pyautogui.position())
import_template()



