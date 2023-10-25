import datetime
#Ejercicio 1_  Escriba la siguiente frase
print ("Ejercicio 1")
print ('“El verdadero desafío es imaginarte el algoritmo y no programarlo”')

print ("")
"""Ejercicio 2_ Defina 5 variables: nickname, cumple, edad, factura, compra
Inicialice nickname con su nombre en redes sociales
¿Qué tipo de variable es?
Inicialice su edad
¿Qué tipo de variable es?
Inicialice cumple con su fecha de cumpleaños
¿Qué tipo de variable es?
Inicialice factura con lo último que gastó
¿Qué tipo de variable es?
Inicialice compra con lo último que compró
¿Qué tipo de variable es? """

print ("Ejercicio 2")

nickname = input("Ingrese su nombre de usuario: ")  
print (nickname)
print ("Es un 'String'")
print ("- -  - - -  - -")

cumple = datetime.date(1980,12,1)
cumple = datetime.date.strftime(cumple, "%d/%m/%Y")
print (cumple)
print ("Es un dato tipo fecha")
print ("- -  - - -  - -")

edad = 42
print (edad)
print ("Es un dato tipo 'interger'")
print ("- -  - - -  - -")

factura = 15000.00
print (factura)
print ("Es un dato tipo 'float'")
print ("- -  - - -  - -")

compra = "Cocina Industrial"
print (compra)
print ("Es un dato tipo 'String'")
print ("- -  - - -  - -")
