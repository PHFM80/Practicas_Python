from rich.table import Table
#from rich.console import Console
#import random
import time
from rich.live import Live


table = Table()
table.add_column("Id")
table.add_column("Descripcion")

with Live (table, refresh_per_second=4):
    for i in range(12):
        time.sleep(0.4)
        table.add_row(f"{i+1}", "[green]LISTo")

# console = Console()
# console.print(table)


