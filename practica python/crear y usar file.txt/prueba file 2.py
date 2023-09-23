from io import open
# creacion de objeto persona
class personas:
    def __init__(self, codUnico, nombre, apellido, dni, edad):
        self.codUnico = codUnico
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
persona = []

# creacion de objeto persona

# persona1 = personas(codUnico=123456789, nombre="Juan", apellido="Pérez", dni=123456789, edad=25)
# persona2 = personas(codUnico=987654321, nombre="Pedro", apellido="Pérez", dni=987654321, edad=25)
# persona3 = personas(codUnico=987654321, nombre="Pedro", apellido="Pérez", dni=987654321, edad=25)

#Menu principal
while True:
    opc1 = int(input("Elija la accion que desearealzar\n"
                 "1. Ingresar Una persona.\n"
                 "2. Ver las personas ingresadas.\n"
                 "3. Modificar las personas ingresadas.\n"
                 "4. Eliminar una persona.\n"
                 "5. Salir\n"))
#1 crear el file.txt
    if opc1 == 1:
        archivoDePersonas = open("personas.txt", "w")
        while True:
            opc = input("Desea ingresar una person\n"
                "S si desea ingresar una person\n"
                "N si desea salir\n")
            if opc == "s" or opc == "S":
                persona.append(personas(codUnico=int(input("Ingrese el código de la persona: ")),
                                        nombre=input("Ingrese el nombre de la persona: "),
                                        apellido=input("Ingrese el apellido de la persona: "),
                                        dni=int(input("Ingrese el DNI de la persona: ")),
                                        edad=int(input("Ingrese la edad de la persona: "))))
            elif opc == "n" or opc == "N":
                print ("Saliendo")
                break
            else:
                print ("Opción incorrecta")
        archivoDePersonas.write(str(persona))
        archivoDePersonas.write("\n")
        archivoDePersonas.close()

#Ver las personas ingresadas
    elif opc1 == 2:
        archivoDePersonas = open("personas.txt", "r")
        for linea in archivoDePersonas:
            print(linea)
            persona.append(linea)
            print(persona)
            archivoDePersonas.close()

#modificar personas ingresadas
    elif opc1 == 3:
        pass

#eliminar personas ingresadas
    elif opc1 == 4:
        pass

    elif opc1 == 5:
        print("Saliendo del programma...")

    else:
        print("Opción incorrecta\n"
              "Ingrese otra opcion")

