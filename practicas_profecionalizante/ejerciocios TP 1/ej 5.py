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