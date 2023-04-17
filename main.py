# TODO: Create master template for track order
# TODO: Load files into Luna (is this even possible?)
# TODO: figure out how to read text from Luna GUI
# TODO: color code files by track type, select first item in tracks list color palate, click, move mouse to correct color, /n
#  change color, move on with arrow key
# TODO: Import Session Template
# TODO: Route
# TODO: Notify via email or text of complete session
# TODO: Close Luna
# TODO: Update color dict to populate positions based on screen size
### 1-import 2-arrange in order 3-color code 4-import template 5- route
## can you check if a program has loaded before a script starts running?
from subprocess import Popen
import pyautogui
import os
from time import sleep

TEMPLATE_NAME = "FankTemplate1.1"
PATH = '/Users/calebfankhauser/Desktop/MixAssist Test'

x,y = pyautogui.size()
screen_size = int(str(x)),int(str(y))


track_list_start = (21,191)
color_pos_dict = {
    "ocean_blue": (137, 358),
    "light_blue": (119, 348),
    "drums": (102, 348),
    "dark_blue": (91, 332),
    "bass": (80, 314),
    "pink": (86, 294),
    "bg_vox": (80, 276),
    "hot_pink": (104, 260),
    "lead_vox": (119, 253),
    "orange": (138, 252),
    "keys": (158, 259),
    "gold": (172, 275),
    "yellow": (184, 295),
    "key_lime": (182, 313),
    "guitars": (170, 330),
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
template_search_dict = {
    "drums": ["Kick Aux", "Snare Aux", "Toms Aux", "Overheads Aux", "Rooms Aux", "Fatso", "K/S Crush", "Devil-loc",
              "False Room", "Drum Plate", "Drum Slap", "Drums Aux"],
    "bass": ["Bass Aux"],
    "guitars": ["GTR Plate", "GTR Slap"],
    "keyboards": ["Keys Aux"],
    "lead_vox": ["Lead Combiner", "FoxySlap", "Vox Paralell", "Vox Plate", "Vox Chamber", "16th Delay", "8th Delay",
                 "Lead Vocal Aux"],
    "bg_vox": ["BG Combiner", "BG FoxySlap", "BG Vox Paralell", "BG Vox Plate", "BG Vox Chamber", "BG 16th Delay",
                 "BG 8th Delay", "BG Vocal Aux"],
    "full_mix": ["Rear Bus", "Mix Bus"]

}
setup_options_dict = {
    "file": (125, 11),
    "import add": (422, 453),
    "clear import search": (490, 395),
}

class Sorter:
    '''sorts instruments into dict with number of occurances as values'''
    ### longterm figure out a better way to classify tracks than these key lists
    def __init__(self, track_directory: str):
        #TODO: Read file names in folder to add to tracks list
        self.tracks = os.listdir(track_directory)
        self.formated_tracks = [item.replace('.wav', '') for item in self.tracks]
        self.instrument_groups = []
        self.group_order = ["drums", "bass", "guitars", "keyboards", "lead_vox", "bg_vox"]
        self.keyword_dict = {
            'drums': ["kick", "snare", "toms", "overheads", "oh", "rooms"],
            'bass': ["bass", "di_bass", "bass_amp", "808"],
            'guitars': ["guitar", "gtr", "electric", "acoustic"],
            'keyboards': ["keys", "piano", "wurli", "synth"],
            'lead_vox': ["lead_vox", "vocals", "vox"],
            'bg_vox': ["bg_vox", "backgrounds", "harmonies", "harmony", "adlib", "adlibs"]
        }
        for item in self.formated_tracks:
            for key in self.keyword_dict:
                if item in self.keyword_dict.get(key):
                    if key not in self.instrument_groups:
                        self.instrument_groups.append(key)

    def sort_to_group(self):
        master_dict = {}
        for group in self.group_order:
            if group in self.instrument_groups:
                print(group)
                master_dict[group] =  {"number": 0, "color": color_pos_dict.get(group)}
        for item in self.formated_tracks:
            for key in self.keyword_dict:
                if item in self.keyword_dict.get(key):
                    master_dict[key]["number"] += 1
        return master_dict




def color_coder(master_dict: dict):
    # pyautogui.moveTo(track_list_start)
    pyautogui.click(track_list_start)
    pyautogui.click(track_list_start)
    for n in master_dict:
        number = master_dict[n]["number"]
        color = master_dict[n]["color"]
        pyautogui.moveTo(color)
        while number > 0:
            print(color)
            pyautogui.click()
            number -= 1
            pyautogui.press('down')


def import_template(search_dict: dict):
    # I can select the tracks I want the import to go under as they are imported but the timing needs to be right
    pyautogui.hotkey('option', 'i', interval=0.1)
    pyautogui.write(TEMPLATE_NAME)
    pyautogui.press('enter')
    sleep(5)
    for key in search_dict:
        for item in search_dict[key]:
            pyautogui.write(item)
            pyautogui.click(setup_options_dict["import add"])
            pyautogui.click(setup_options_dict['clear import search'])
            pyautogui.click(setup_options_dict['clear import search'])


print(pyautogui.position())
sorter = Sorter(PATH)
color_coder(sorter.sort_to_group())
import_template(template_search_dict)












