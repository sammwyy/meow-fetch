from pathlib import Path
from config import Config
from utils import Utils
from fetcher import Fetcher
from colors import Colors
import os

class MeowFetch:
    def __init__(self):
        config_dir = os.path.join(Path.home(), ".config")
        working_dir = os.path.join(config_dir, "meow-fetch")

        # Config
        config = Config(os.path.join(working_dir, "config.meow"))
        config.load()

        # Colors
        colors = Colors()

        # Utilities
        utils = Utils()

        # Fetcher
        fetcher = Fetcher(config.get("color-char", "*"))
        
        # Ascii
        ascii_path = config.get("ascii-path", "ascii/cat.txt")
        ascii = open(os.path.join(working_dir, ascii_path)).read()

        # Info
        info_path = os.path.join(working_dir, "info.meow")
        info = open(info_path).read()

        self.config = config
        self.colors = colors
        self.fetcher = fetcher
        self.utils = utils
        self.ascii = ascii
        self.info = info

    def fetch(self):
        padding_x = self.config.get("padding-x", 3)
        padding_y = self.config.get("padding-y", 2)
        space_between = self.config.get("space-between", 3)

        ascii = self.utils.normalize(self.ascii)
        info = self.utils.add_padding_to_text(self.info, space_between, 0)

        raw_text = self.utils.add_info_to_ascii(ascii, info)
        text = self.utils.add_padding_to_text(raw_text, padding_x, padding_y)

        print(self.colors.format(self.fetcher.format(text)))

if __name__ == "__main__":
    MeowFetch().fetch()
