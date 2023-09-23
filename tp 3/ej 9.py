print (f'''Realiza un DF para ingresar por teclado los mmetros cuadrado totales de un predio y 
los metros cuadrados cubiertos, luego calcular y mostrar por pantalla el porcentaje de metros
cuadrados cubiertos y el porcentaje de metros cuadrados escubiertos.''')
print("")
m2Tot = int(input("Ingrese la cantidad de metros cuadrados totales: "))
m2Cub = int(input("Ingrese la cantidad de metros cuadrados cubiertos: "))
print("- -  - - -  - -")
m2Desc = m2Tot - m2Cub
porcM2Cub = (m2Cub * 100) / m2Tot
porcM2Desc = (m2Desc * 100) / m2Tot

print(f'''El porcentaje de metros cuadrados cubiertos es de: {round(porcM2Cub, 1)}%
El porcentaje de metros cuadrados descubiertos es de: {round(porcM2Desc, 1)}%)''')

