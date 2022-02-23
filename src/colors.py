from colorama import init
from colorama import Fore, Back, Style

class Colors:
    def __init__(self):
        init()

    def format(self, text):
        return (
            text
                .replace("{black}", Fore.BLACK)
                .replace("{blue}", Fore.BLUE)
                .replace("{cyan}", Fore.CYAN)
                .replace("{green}", Fore.GREEN)
                .replace("{magenta}", Fore.MAGENTA)
                .replace("{red}", Fore.RED)
                .replace("{reset}", Fore.RESET)
                .replace("{white}", Fore.WHITE)
                .replace("{yellow}", Fore.YELLOW)

                .replace("{light_black}", Fore.LIGHTBLACK_EX)
                .replace("{light_blue}", Fore.LIGHTBLUE_EX)
                .replace("{light_cyan}", Fore.LIGHTCYAN_EX)
                .replace("{light_green}", Fore.LIGHTGREEN_EX)
                .replace("{light_magenta}", Fore.LIGHTMAGENTA_EX)
                .replace("{light_red}", Fore.LIGHTRED_EX)
                .replace("{light_white}", Fore.LIGHTWHITE_EX)
                .replace("{light_yellow}", Fore.LIGHTYELLOW_EX)
        )
