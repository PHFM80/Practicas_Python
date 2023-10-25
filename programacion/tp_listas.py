import random

#Ejercicio 1.
print ("Escriba un programa que pida dos números enteros y muestre la lista de números pares que hay entre ellos (incluidos"
"ellos mismos si son pares) y mostrando la cantidad total de números pares")

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

numeros_pares = []

inicio = min(numero1, numero2)
fin = max(numero1, numero2)

for palabra in range(inicio, fin + 1):
    if palabra % 2 == 0:
        numeros_pares.append(palabra)

print(f"Números pares entre {inicio} y {fin}: {numeros_pares}")

cantidad_pares = len(numeros_pares)
print(f"Cantidad total de números pares: {cantidad_pares}\n")


#Ejercicio 2.
print ("Escriba un programa genere 100 números aleatorios enteros positivos y luego muestre los no repetidos ordenados en"
"forma descendente.\nNota: es posible utilizar una lista secundaria")

numeros_aleatorios = [random.randint(1, 1000) for _ in range(100)]

numeros_unicos = []

for palabra in numeros_aleatorios:
    if palabra not in numeros_unicos:
        numeros_unicos.append(palabra)

numeros_unicos.sort(reverse=True)

print (f"Lista de números aleatorios: {numeros_aleatorios}")
print (f"lista de números unicos: {numeros_unicos}")
print("Números únicos ordenados en forma descendente:")
for palabra in numeros_unicos:
    print(palabra)


#Ejercicio 3.
print ("Defina una lista vacía. Luego ingrese 5 sueldos y almacenelos en la lista definida. Luego muestre por pantalla el"
"promedio de los sueldos ingresados, también muestre los sueldos que están por encima del promedio calculado")

sueldos = []

for i in range(5):
    sueldo = float(input(f"Ingrese el sueldo {i+1}: "))
    sueldos.append(sueldo)

promedio = sum(sueldos) / len(sueldos)

print(f"El promedio de los sueldos ingresados es: {promedio}")

print("Sueldos por encima del promedio:")
for sueldo in sueldos:
    if sueldo > promedio:
        print(sueldo)


#Ejercicio 4.
print ("Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas"
"veces aparece esa palabra en la lista.  Posibles salidas por pantalla:\n"
"1.- La palabra ??? no aparece en la lista\n"
"2.- La palabra ??? aparece una vez en la lista\n"
"3.- La palabra ??? aparece XX veces en la lista\n")

# Crear una lista de palabras
lista_de_palabras = []

while True:
    palabra = input("Ingrese una palabra (o deje en blanco para detenerse): ")
    if palabra == "":
        break
    lista_de_palabras.append(palabra)

palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

cantidad = lista_de_palabras.count(palabra_a_buscar)

if cantidad == 0:
    print(f"La palabra '{palabra_a_buscar}' no aparece en la lista")
elif cantidad == 1:
    print(f"La palabra '{palabra_a_buscar}' aparece una vez en la lista")
else:
    print(f"La palabra '{palabra_a_buscar}' aparece {cantidad} veces en la lista")


Ejercicio 5.
print ("Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos"
"(dejando únicamente el primero de los elementos repetidos).")

lista_de_palabras2 = []

while True:
    palabra2 = input("Ingrese una palabra (o deje en blanco para detenerse): ")
    if palabra2 == "":
        break
    lista_de_palabras2.append(palabra2)

palabras_unicas = []

for palabra in lista_de_palabras2:
    if palabra not in palabras_unicas:
        palabras_unicas.append(palabra)

print (f"La lista de palabras es: {lista_de_palabras2}")
print (f"La lista de palabras unicas es: {palabras_unicas}")

Ejercicio 6.
print ("Codificar en Python un programa que permita cargar una lista que contenga las notas de un curso de 20 alumnos"
"indicando:\nA. La nota más alta y la nota más baja"
"B. El promedio de notas\n"
"C. El número de notas superiores al promedio\n"
"D. La cantidad de alumnos aprobados (notas >= a 4)\n"
"E. La cantidad de alumnos reprobados.\n")
notas = []

for i in range(20):
    nota = random.randint(1,10)
    print (f"La nota del alumno {i+1} es: {nota}\n")
    notas.append(nota)

print (f"La lista de notas es: \n{notas}\n")
print (f"La nota mas alta es: {max(notas)}")
print (f"La nota mas baja es: {min(notas)}")
promedio = sum(notas)/len(notas)
print (f"El promedio de las notas es: {promedio}")
SupPromedio = 0
for i in notas: 
    if i >= promedio:
        SupPromedio += 1
print (f"La cantidad de notas superiores al promedio es: {SupPromedio}")
alumn_aprob = 0
for i in notas:
    if i >= 4:
        alumn_aprob += 1
print (f"La cantidad de alumnos aprobados es:{alumn_aprob}")
print (f"El cantidad de alumnos desaprobados: {len(notas) - alumn_aprob}")




