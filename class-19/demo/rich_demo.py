from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Instantiate a console object
# The "console" refers to a text-based user interface (TUI) for displaying richly formatted and styled text in the terminal.
console = Console()

# Let's print something out in green.
# Note the open / closing (almost like HTML)
console.print("Hello, [bold green]User[/bold green]!")

# Ask for a Users name
# We could do a simple input statement here and it will work.
# But watch what happens when I press Enter. No user input.
# name = input('What is your name? ')
name = Prompt.ask("What is your name?", default='Roger')

# Display a message to the user
console.print(f"Nice to meet you, [bold blue]{name}[/bold blue]!")

# Create a table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name", style="dim", width=20)
table.add_column("Age")
table.add_column("Country")

# Add rows to the table
table.add_row("John Doe", "30", "USA")
table.add_row("Jane Doe", "25", "Canada")
table.add_row(name, Prompt.ask("What is your age?"), Prompt.ask("What is your country?"))

# Display the table
console.print(table)

# Let's make a link clickable by our mouse.
# console.print("CodeFellows", style="link https://codefellows.com")
