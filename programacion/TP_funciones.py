
#Ejercicio 1.
print ("convertir una cadena de caracteres separada por comas a una lista eliminando los que no son enteros"
"Ejemplo: cadena=12,13,122,S,SA,$,% Debe devolver una lista con los siguientes valores"
"[12,13,122]")
def cadena_a_lista_enteros(cadena):
    elementos = cadena.split(',')  
    lista_enteros = []
    for elemento in elementos:
        if elemento.isdigit():
            lista_enteros.append(elemento)

    return lista_enteros


cadena = input("ingrese cualquier caractere separado por comas: \n")
resultado = cadena_a_lista_enteros(cadena)
print(resultado)



#Ejercicio 2.
print ("El CUIT/CUIL es el código único de de identificación tributaria/laboral, que se le asigna a cada persona"
"física o jurídica (sociedades) alcanzadas por el sistema impositivo argentino."
"Generar una función llamada validarCuit que devuelva True o False siguiendo estas condiciones: \n"
"1.- La longitud debe ser de 13\n"
"2.- Solo se permiten numeros excepto los guiones – \n"
"3.- Los guiones deben estar en las posiciones correctas\n")

def validarCuit(cuit):
    # 1. La longitud debe ser de 13
    if len(cuit) != 13:
        return False
    
    # 2. Solo se permiten números excepto los guiones -
    permitidas = set("0123456789-")
    if not all(char in permitidas for char in cuit):
        return False
    
    # 3. Los guiones deben estar en las posiciones correctas
    if cuit[2] != '-' or cuit[11] != '-':
        return False

    return True

#cuit = input("Ingrese su numero de cuit con el siguiente formato (xx-xxxxxxxx-x):\n")
cuit = "20-12345678-9"
resultado = validarCuit(cuit)
print(resultado)





#Ejercicio 3.
print ("Desarollar una funcion que retorne cuantas vocales hay en una determinada cadena"
"Ejemplo: cadena=Programación           debe devolver 5")
def contar_vocales(cadena):
    # Inicializamos un contador para las vocales
    contador = 0

    # Convertimos la cadena a minúsculas para que coincida con vocales en mayúsculas y minúsculas
    cadena = cadena.lower()

    # Definimos una lista de vocales
    vocales = "aeiouáéíóú"

    # Recorremos la cadena y contamos las vocales
    for letra in cadena:
        if letra in vocales:
            contador += 1

    return contador


#cadena = input ("Ingrese cualquier cadena de texto: \n")
cadena = "Programación"
resultado = contar_vocales(cadena)
print("Número de vocales en la cadena:", resultado)



#Ejercicio 4.
print ("Desarollar una función que reciba como argumento una lista de enteros y que retorne la suma de los numeros pares de la lista"
"Ejemplo: [1,4,26,11]      Debe devolver 30")

def suma_numeros_pares(lista):
    suma = 0

    for numero in lista:
        if numero % 2 == 0:  # Verificar si el número es par
            suma += numero

    return suma


# lista_enteros = []  # Inicializamos una lista vacía para almacenar los números

# while True:
#     entrada = input("Ingresa un número (o presiona Enter para finalizar): ")
    
#     if entrada == "":
#         break  # Si se presiona Enter, salimos del bucle
#     try:
#         numero = int(entrada)  # Intentamos convertir la entrada en un número
#         lista_enteros.append(numero)  # Agregamos el número a la lista
#     except ValueError:
#         print("Entrada no válida. Introduce un número válido.")

# Ejemplo de uso:
lista_enteros = [1,4,26,11]
resultado = suma_numeros_pares(lista_enteros)
print("La suma de los números pares en la lista es:", resultado)
