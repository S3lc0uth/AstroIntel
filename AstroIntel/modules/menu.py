from rich.console import Console
from modules.terminal_tools import *

console = Console()


def print_menu():
   
    f = open('./assets/details.txt', 'r', encoding="utf8")
    details = f.read()
    print_log(details, "blue")
    f.close()
