class alumno:
    def __init__(self, nombre, apellido, dni, edad, curso, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.curso = curso
        self.notas = notas

alumnos = []
notas = []

# Sub Programa para mostrar alumnos
def mostrarAlumnos():
    for i in range(len(alumnos)):
        print(f"N° {i+1}) Nombre: {alumnos[i].nombre}, Apellido: {alumnos[i].apellido}\n"
        f"DNI: {alumnos[i].dni}, Edad: {alumnos[i].edad}\n"
        f"Curso: {alumnos[i].curso}, Notas: {alumnos[i].notas}\n")

#ESTE ES EL MENU PRINCIPAL
while True:
    print("")
    print("Bienvenido al sistema de gestión de alumnos")
    try:
        opc = int(input("Elija una opción.\n1. Menu Ingresos.\n2. Menu Modificaciones.\n"
                        "3. Mostrar Alumnos.\n4. Salir.\n"))
    
    except TypeError as e:
        print(f"no es una opcion valida.  {e}" )

    
    print("")
    # MENU INGRESOS 
    if opc == 1:
        while True:
            print("")
            opcIngreso = int(input("¿Qué desea ingresar?\n1. Ingresar Alumno\n"
                                 "2. Volver a la pantalla anterior.\n"))
            print("")
            if opcIngreso == 1:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = int(input("DNI: "))
                edad = int(input("Edad: "))
                curso = input("Curso: ")
                notas = []
                cantNotas = int(input("¿Cuántas notas va a ingresar: "))
                for i in range(cantNotas):
                    nota = int(input("Nota: "))
                    notas.append(nota)
                alum = alumno(nombre, apellido, dni, edad, curso, notas)
                alumnos.append(alum)
                
            elif opcIngreso == 2:
                input("Volviendo a la pantalla anterior.\n"
                      "Presione enter.\n")
                break

            else:
                print("\nLa opción ingresada no es correta\n"
                      "Ingrese una opcion correcta\n")
   
    # MENU MODIFICACIONES
    elif opc ==2:
        while True:
            opcMod = int(input("\n¿Qué desea modificar?\n1. Opción Modificar Datos Personales\n"
                               "2. Opción Notas\n3. Volver a la pantalla anterior.\n" "\n"))
            
            # MENU MODIFICAR DATOS PERSONALES
            if opcMod == 1:
                mostrarAlumnos()
                selecAlum = int(input("\nSeleccione el n° de alumno al cual modificara los datos.\n"))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = int(input("DNI: "))
                edad = int(input("Edad: "))
                curso = input("Curso: ")
                selecAlum -=1
                alumnos[selecAlum].nombre = nombre
                alumnos[selecAlum].apellido = apellido
                alumnos[selecAlum].dni = dni
                alumnos[selecAlum].edad = edad
                alumnos[selecAlum].curso = curso
                
            # MENU NOTAS
            elif opcMod == 2:
                while True:
                    opc = int(input("\n¿Que acción desea realizar?\n"
                                    "1. Modificar una nota.\n"
                                    "2. Agregar una nota.\n"
                                    "3. Volver al menu anterior.\n"))
                    
                    # MODIFICAR NOTAS
                    if opc == 1:
                        mostrarAlumnos()
                        selecAlum = int(input("\nSeleccione el n° de alumno al cual modificar las notas.\n"))
                        selecAlum -= 1
                        #en esta linea quiero mostrar solamente el alumno que voy a modificar pero me muestra 
                        #el alumno q quiero ver, pero el largo de la lista 
                        
                        #for i in range(len(alumnos)):
                        print(f"\nN° {selecAlum+1}: {alumnos[selecAlum].nombre}, {alumnos[selecAlum].apellido}. DNI: {alumnos[selecAlum].dni} "
                            f"Edad: {alumnos[selecAlum].edad}. Curso: {alumnos[selecAlum].curso}. Notas: {alumnos[selecAlum].notas}")
                        for i in range(len(notas)):
                            print(f"Nota {i+1}: {notas[selecAlum]}")
                            nota = int(input("Nota: "))
                            notas[i] = nota
                    
                    #AGREGAR NOTAS
                    elif opc == 2:
                        mostrarAlumnos()
                        selecAlum = int(input("\nSeleccione el n° de alumno al cual agregara las notas.\n"))
                        selecAlum -= 1
                        
                        #for i in range(len(alumnos)):
                        print(f"\nN° {selecAlum+1}: {alumnos[selecAlum].nombre}, {alumnos[selecAlum].apellido}. DNI: {alumnos[selecAlum].dni} "
                                f"Edad: {alumnos[selecAlum].edad}. Curso: {alumnos[selecAlum].curso}. Notas: {alumnos[selecAlum].notas}")
                       
                        cantNotas = int(input("¿Cuántas notas va a ingresar: "))
                        for i in range(cantNotas):
                            nota = int(input("Nota: "))
                            #notas.append(nota)
                            alumnos[selecAlum].notas = notas.append(nota)
                            
                    #VOLVER AL MENU MODIFICAR DATOS PERSONALES
                    elif opc == 3:
                        input("\nVolviendo a la pantalla anterior.\n"
                            "Presione enter.\n")
                        break
                    
                    else:
                        print("\nLa opción ingresada no es correta\n"
                      "Ingrese una opcion correcta\n")
                        
            #VOLVIENDO
            elif opcMod == 3:
                input("\nVolviendo a la pantalla anterior.\n"
                      "Presione enter.\n")
                break
            
            else:
                print("\nLa opción ingresada no es correta\n"
                      "Ingrese una opcion correcta\n")
   
    # MENU MOSTRANDO ALUMNOS
    elif opc == 3:
        mostrarAlumnos()
        input("\n  Volviendo a la pantalla pincipal\n  Presione enter\n")
    
    #SALIR
    elif opc == 4:
        input("Usted esta saliendo del programa\n"
              "Presione enter")
        print("")
        break
        
    else:
        print("\nLa opción ingresada no es correta\n"
                "Ingrese una opcion correcta\n")

    

