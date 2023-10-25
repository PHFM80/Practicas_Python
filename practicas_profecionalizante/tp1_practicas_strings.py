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




"""Ejercicio 3
Ahora deberá crear estas 5 variables: materiapreferida, pasatiempo, deporte, familia, nrodemascotas
Inicializarlas por teclado
Luego Imprima por pantalla la siguiente frase:
Mi materia preferida en el colegio es Programación. Mi pasatiempo preferido es dormir. Practico correr como
deporte. En mi familia somos 4 personas y 2 mascotas
Tenga en cuenta cómo hacer para mostrar texto con variables, todo en un mismo texto."""

materiapreferida = input("Ingrese materia preferida: ")
pasatiempo = input("Ingrese pasatiempo preferido: ")
deporte = input("Ingrese deporte preferido: ")
familia = int(input("Ingrese cuantos miembros son en su familia: "))
nrodemascotas = int(input("Ingrese numero de mascotas: "))

print (f"Mi materia preferida en el colegio es {materiapreferida}. Mi pasatiempo preferido es {pasatiempo}."
       f" Practico {deporte} como deporte. "
       f"\nEn mi familia somos {familia} personas y {nrodemascotas} mascotas")



"""Ejercicio 4
Defina una variable que almacene su nickname
Imprima su nickname con minúscula, excepto la letra inicial 
y su apellido todo con mayúscula"""

# nickname = input("Ingrese su nickname: ")
# apellido = input("Ingrese su apellido: ")
# print (nickname.capitalize() + " " + apellido.upper())
nombreCompleto = "Pablo Flores"
print (nombreCompleto)
print(nombreCompleto[0:5].capitalize()+" "+nombreCompleto[6:12].upper())



'''1) DESAFÍO
CADENAS
Dada la variable python, nombredelestudiante = “Este es el trabajo de: apellido, nombre”
Tenga en cuenta cuales son los datos a la entrada que necesita
Ahora define los comandos necesarios para llevar a cabo el remplazo
Finalmente redefina la variable para que tome los comandos aplicados
Ejemplo: “Este es el trabajo de: Juan Perez” '''

# print ("Forma 1")
# nombredelestudiante = "Este es el trabajo de: Perez, Juan"
# print(nombredelestudiante)

# nombredelestudiante = nombredelestudiante.replace("Perez, Juan", "Juan Perez")
# print(nombredelestudiante)

print ("Forma 2")

nombredelestudiante = "Este es el trabajo de: apellido, nombre"
print(nombredelestudiante)
apellido = input("Ingrese un apellido: ").capitalize()
nombre = input ("Ingrese un nombre: ").capitalize()

nombredelestudiante = nombredelestudiante.replace("apellido, nombre", f"{apellido}, {nombre}")
print (nombredelestudiante)