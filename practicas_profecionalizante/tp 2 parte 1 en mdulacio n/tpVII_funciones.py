from random import randint


# # Ejercicio 1
# # Desarrollar una función que calcule el promedio de una serie de números ingresados por teclado
# # Dejará de pedir valores hasta que la variable de corte alcance un determinado valor
# #  Los valores solo pueden ser positivos
# #  Los valores deberán ser parte de una lista
# #  Validar que la entrada de datos solo sean nros enteros

# def promedio(lista):
#     promedio = (sum(lista))/len(lista)
#     return promedio

# cantNros = int (input("Indique la cantidad maxima de numeros a ingresar: \n"))
# listaNumeros = []
# cont = 0
# while cont != cantNros:
    
#     try:
#         nro = int (input("Ingrese un numero positivo mayor a 0 sin decimales: \n"))
#     except ValueError:
#         print ("Ingrese un numero entero.  sin decimales")
    
#     if nro > 0 and nro != float:
#         listaNumeros.append(nro)
#         cont += 1
#     else:
#         print ("Ingrese una opcion correcta.")
# print (listaNumeros)
# print (f"El promedio de los numeros ingresados es: {promedio(listaNumeros)}")


# # Ejercicio 2
# # Desarrollar una función que cuente el número de palabras que hay en una expresión o cadena ingresada por teclado

# def contar_palabras(cadena):
#     palabras = cadena.split()
#     numero_palabras = len(palabras)
#     return numero_palabras
    

# cadena = input("Ingresa una expresión o cadena: \n")

# print(f"El número de palabras en la cadena es: {contar_palabras(cadena)}")


# # Ejercicio 3
# # Desarrollar una función que cuente el número de mayúsculas que hay en una expresión o cadena ingresada
# # por teclado
# # También deberá mostrar el carácter en el que se encuentra cada mayúscula.

# def contar_mayusculas(cadena):
#     contador_mayusculas = 0

#     for indice, caracter in enumerate(cadena):
#         if caracter.isupper():
#             contador_mayusculas += 1
#             print(f"Mayúscula encontrada en la posición {indice + 1}: '{caracter}'")

    
#     print(f"El número total de mayúsculas en la cadena es: {contador_mayusculas}")


# frase = input("Ingresa una expresión o cadena: ")
# contar_mayusculas(frase)


# # Ejercicio 4
# # Desarrollar un programa que nos permita elegir a partir de una expresión o cadena ingresada por teclado, 
# # lo que deseamos calcular en esa expresión (llamando a las diferentes funciones que realicen lo solicitado)
# # 1: Contar cantidad total de palabras
# # 2: Contar y ubicar vocales 
# # 3: Contar cantidad total de letras
# # 4: Contar y ubicar mayúsculas
# # El programa deberá seguir pidiendo que ingresemos frases hasta que ingresemos un valor de corte

# def contar_palabras(cadena):
#     palabras = cadena.split()
#     return len(palabras)

# def contar_y_ubicar_vocales(cadena):
#     contador_vocales = 0

#     for indice, caracter in enumerate(cadena):
#         if caracter.lower() in "aeiou":
#             contador_vocales += 1
#             print(f"Vocal encontrada en la posición {indice + 1}: '{caracter}'")

#     return contador_vocales


# def contar_letras(cadena):
#     contador_letras = 0
#     for caracter in cadena:
#         if caracter.isalpha():
#             contador_letras += 1
#     return contador_letras

# def contar_y_ubicar_mayusculas(cadena):
#     contador_mayusculas = 0
    
#     for indice, caracter in enumerate(cadena):
#         if caracter.isupper():
#             contador_mayusculas += 1
#             print(f"Mayuscula encontrada en la posición {indice + 1}: '{caracter}'")

#     return contador_mayusculas

# while True:
#     cadena_ingresada = input("Ingresa una expresión o cadena (presiona Enter para salir): ")

#     if cadena_ingresada == "":
#         break

#     print("Opciones del mnenu:\n"
#         "\t1: Contar cantidad total de palabras\n"
#         "\t2: Contar y ubicar vocales\n"
#         "\t3: Contar cantidad total de letras\n"
#         "\t4: Contar y ubicar mayúsculas\n")

#     opcion = input("Elija una opción: \n")

#     if opcion == '1':
#         resultado = contar_palabras(cadena_ingresada)
#         print(f"Total de palabras: {resultado}")
    
#     elif opcion == '2':
#         contador = contar_y_ubicar_vocales(cadena_ingresada)
#         print(f"Total de vocales: {contador}")

#     elif opcion == '3':
#         resultado = contar_letras(cadena_ingresada)
#         print(f"Total de letras: {resultado}")
    
#     elif opcion == '4':
#         contador = contar_y_ubicar_mayusculas(cadena_ingresada)
#         print(f"Total de mayúsculas: {contador}")
    
#     else:
#         print("Opción no válida. Inténtalo de nuevo.")



# # Ejercicio 5
# # Desarrollar una función que ordene una lista cuyos valores serán ingresados por teclado.
# # Luego el usuario podrá elegir si desea ordenar la lista en forma creciente o decreciente
# # Una vez obtenido el resultado el programa pedirá nuevamente ingresar valores para ordenar
# # Dejará de pedir valores hasta que la variable de corte alcance un determinado valor

#     # funcion para ordenar la lista
# def ordenar(opc, lista):
#     lista_ordenada = sorted(lista)
#     if opc == 2 :
#         lista_ordenada = list(reversed(lista_ordenada))
#     return lista_ordenada

#     #Funcion del programa principal
# def ejecutar ():
#     print ("Debera ingresar numeros que seran guardados, luego deteminara si los desea ordenar en forma ascendente o descendente.\nCuando ingrese el 0 dejara de ingresar numeros.")
#     numeros =[]
#     num1 = 1
#     while num1 !=0 :
#         num = int(input("Ingrese un numero: \n"))
#         num1 = num
#         if num !=0 :
#             numeros.append(num)
#     print ("Para ordenar la lista en forma ascendente presiones 1.\nPara hacerlo en forma descendente presione2.\n")
#     try:
#         opc = int(input("ingrese una opcion:\n"))
#     except ValueError:
#         print("Ingrese una opcion correcta.")

#     orden = "ascendente"
#     if opc == 2:
#         orden = "descendente"
#     print (f"La lista de numeros es: {numeros}.\n"
#             f"La lista ordenada en forma {orden} es:"
#             f"{ordenar (opc, numeros)}")

#     #Programa principal
# while True:
#     ejecut = input ("Si desea ejecutar elprograma presione SI, de lo contrario presion NO.\n").lower()
#     if ejecut == "si":
#         ejecutar()
#     elif ejecut == "no":
#         print ("Saliendo del programa.")
#         break
#     else:
#         print ("Ingrese una opcion correcta")


# print ("Debera ingresar numeros que seran guardados, luego deteminara si los desea ordenar en forma ascendente o descendente.\nCuando ingrese el 0 dejara de ingresar numeros.")
# numeros =[]
# num1 = 1
# while num1 !=0 :
#     num = int(input("Ingrese un numero: \n"))
#     num1 = num
#     if num !=0 :
#         numeros.append(num)
# print ("Para ordenar la lista en forma ascendente presiones 1.\nPara hacerlo en forma descendente presione2.\n")
# try:
#     opc = int(input("ingrese una opcion:\n"))
# except ValueError:
#     print("Ingrese una opcion correcta.")

# orden = "ascendente"
# if opc == 2:
#     orden = "descendente"
# print (f"La lista de numeros es: {numeros}.\n"
#         f"La lista ordenada en forma {orden} es:"
#         f"{ordenar (opc, numeros)}")



# Desafío
# Se ha colocado una nueva cámara de velocidad en una ruta, donde el límite de velocidad es de 110 km/h. La 
# cámara detecta la velocidad de cada automóvil que pasa e indica el número de puntos que se deducirán de la 
# licencia de conducir si van demasiado rápido. Escriba una función para verificar la velocidad de cada 
# automóvil y determine las deducciones de puntos, si las hubiera.  Su función debe incluir el argumento correspondiente.
# Utilize un generador de números aleatorios (enteros positivos con un rango coherente de velocidades para vehículos).
# Los puntos se deducen siguiendo estas condiciones:
# 1.- Si el auto está yendo al límite de velocidad (110 km/h) o más lento, debe imprimir “Ok”
# 2.- Después de eso, por cada 5 km/h por encima del límite de velocidad (110 km/h), debe indicar que un 
# punto debe deducirse de la licencia de conducir. Por ejemplo, si la velocidad está entre 110 - 115 km/h 
# (mayor a 110 y menor igual a 115), su función debe imprimir: “Puntos a deducir: 1”. El siguiente rango 
# seria mayor a 115km/h y menor igual a 120 km/h y asi sucesivamente hasta llegar a 6 puntos
# 3.- Si se deben deducir 6 o más puntos, la función debe imprimir:”¡Suspender la licencia!”.


    # Funcion de calculo de velocidad
def camara_velocidad(vel):
    #cartel = ""
    if vel <= 110:
        cartel = "OK"
    elif vel >110 and vel <= 115:
        cartel = "Puntos a deducir: 1"
    elif vel >115 and vel <= 120:
        cartel = "Puntos a deducir: 2"
    elif vel >120 and vel <= 125:
        cartel = "Puntos a deducir: 3"
    elif vel >125 and vel <= 130:
        cartel = "Puntos a deducir: 4"
    elif vel >130 and vel <= 135:
        cartel = "Puntos a deducir:5"
    elif vel >130 :
        cartel = "¡Suspender la Licencia!"
    return cartel

    #Main
print ("Se ingresara aleatoriamente una velocidad.  que sera medida")
vel = randint(60, 180)
print (f"La velociodad es: {vel} km/h")
print(camara_velocidad(vel))


