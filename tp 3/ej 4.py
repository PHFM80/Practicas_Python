import math
print ("Calculador de edad, segun años.")
anioActual = int(input("Ingrese el año en el que se encuentra: "))
anioNac = int(input("Ingrese su año de nacimiento: "))
edad = anioActual-anioNac
print ("- -  - - - - -  - -")
print (f"Su edad es: {math.trunc(edad)}")
