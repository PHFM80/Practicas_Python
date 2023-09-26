print(f'''Realizar un DF que permita ingresar el número de partidos ganados, perdidos y 
empatados.  Se debe mostrar su púntaje total, teniendo en cuenta que por cada partido  ganado
obtendra 3 puntos, empatado 1 punto y perdido 0 puntos.''')
print("")
cantPartGan = int(input("Ingrese la cantidad de partidos ganados: "))
cantPartEmpa = int(input("Ingrese la cantidad de partidos empatados: "))
cantPartPerd = int(input("Ingrese la cantidad de partidos perdidos: "))

puntosGan = cantPartGan * 3

puntosTot = puntosGan + cantPartEmpa
partJugados = cantPartEmpa + cantPartGan + cantPartPerd

print(f"La cantidad de puntos obtenidos es: {puntosTot}")
print(f"La cantidad de partidos jugados es: {partJugados}")

