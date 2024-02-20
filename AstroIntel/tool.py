from rich.console import Console
from modules.option import *
from modules.menu import *
from modules.table import *
from modules.api import *
from modules.terminal_tools import *
import json
console = Console()



API_URL = "https://services.isrostats.in/api/spacecraft"


def main():
    print_menu()
    
    
    spacecraft_name = console.input(
        "[bold blue]Enter Spacecraft Name: [/bold blue]")
    print("\n")

    data = get_api_data(API_URL)
    found = False
    table_title = f"Information for {spacecraft_name}🚀"

    if data:
        for entry in data:
            if entry["name"] == spacecraft_name:
                print_data(table_title, entry)
                found = True

    if found == False:
        print_error("Spacecraft Not Found!")

    generate_options()


def generate_options():
    options = [
        "Run Again",
        "Exit Tool"
    ]

    option = generate_option(options)

    if option == 1:
        main()  # run the tool again
    else:
        return  # exit the tool


# Main Execution Point of the Script
if __name__ == "__main__":
    main()