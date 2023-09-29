import re

lista_notas = ["1  --  2  -- 3", "1 -- 4", "1 -- 5", "5  -- 6", "1 -- 7", "1 -- 8"]
pos = int(input("ingrese la posiscion de la nota que va a modificar: "))
lista_notas2 = []

numeros = re.split ("\D+", lista_notas[pos])

for i in range (len(numeros)):
    num = numeros[i]
    lista_notas2.append(num)

opc = int( input("Cuantas notas va a agreagr: "))
for i in range(opc):
    nota = int( input(f"Ingrese la nota a agregar nro {i+1} del alumno: "))
    lista_notas2.append(str(nota))

notas2 = " -- ".join(lista_notas2)

print (notas2)