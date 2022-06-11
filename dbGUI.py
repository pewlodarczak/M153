from rich.console import Console
from rich.table import Table
from os import system

def printMenu(input):
    system('cls')
    table = Table(title="DB Commands")

    table.add_column("Num Cmd", style="cyan", no_wrap=True)
    table.add_column("Command", style="magenta")
    table.add_column("Status", justify="center", style="green")
    if input == 1:
        table.add_row("1", "Insert image", "✅")
    else:
        table.add_row("1", "Insert image", "❌")
    if input == 2:
        table.add_row("2", "Read image", "✅")
    else:
        table.add_row("2", "Read image", "❌")
    table.add_row("3", "Update image", "❌")
    table.add_row("4", "Quit", "")

    console = Console()
    console.print(table)

