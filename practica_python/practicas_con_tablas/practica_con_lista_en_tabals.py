from rich.table import Table
import random
import time
from rich.live import Live


id = [1, 2, 3, 4, 5]
nombre = ["A", "B", "C", "D", "E"]
apellido = ["a", "b", "c", "d", "e"]


table = Table()
table.add_column("Id")
table.add_column("Nombre")
table.add_column("Apellido")

with Live (table, refresh_per_second=4):
    for i in range(len(id)):
        id1 = str(id[i])
        nomb = nombre[i]
        ape =apellido[i]
        time.sleep(0.4)
        table.add_row(id1, nomb, ape)

matriz = [["1", "pablo", "Flores"], ["2", "Matias","majul"], ["3", "Marcela", "Morelo"], ["4", "Juan", "Gomez"], ["5", "micaela", "Majul"]]


