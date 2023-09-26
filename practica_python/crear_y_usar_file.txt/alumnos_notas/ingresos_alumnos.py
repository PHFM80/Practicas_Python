

# Menu opcion nro 1
# Cargar datos de un alumno y las primeras notas 

def ingresar_alumno():
    alumno = []
    notas = []

    ver_id = open ("archivos_txt/id.txt", "r")
    lista_id = ver_id.readlines()
    ver_id.close()
    for i in (lista_id):
        id_final = lista_id[len(lista_id)-1]
    print (f"El ultimo id ingresado es: {id_final}")
 
    id = int (input ("Ingrese el ID del alumno: "))
    alumno.append(id)

    nombre1 = str (input ("Ingrese el 1er nombre del alumno: "))
    alumno.append(nombre1)

    nombre2 = str (input ("Ingrese el 2do nombre del alumno: "))
    alumno.append(nombre2)

    apellido1 = str (input ("Ingrese el 1er apellido del alumno: "))
    alumno.append(apellido1)

    apellido2 = str (input ("Ingrese el 2do apellido del alumno: "))
    alumno.append(apellido2)

    edad = int (input ("Ingrese la edad del alumno: "))
    alumno.append(edad)

    dni = int (input( "ingrese el DNI del alumno: "))
    alumno.append(dni)

    materia = str (input ("Ingrese la materia del alumno: "))
    alumno.append(materia)

    opc = int( input("Cuantas notas va a ingresar: "))
    for i in range(opc):
        nota = int( input(f"Ingrese la nota nro {i+1} del alumno: "))
        notas.append(nota)

# Guardar los datos cargados del alumno y borrar la lista alumno y notas
    print ("- - - - - - - - - - - - - - - - -")
    print ("Estos son los datos ingresados: ")
    for i in alumno:
        a=alumno[0]
        b=alumno[1]
        c=alumno[2]
        d=alumno[3]
        e=alumno[4]
        f=alumno[5]
        g=alumno[6]
        h=alumno[7]
    print (f"{a}) Nombre 1: {b} \tNombre 2: {c}\n"
            f"Apellido 1: {d} \tapellido 2: {e}\n"
            f"Edad: {f} \tDNI: {g} \tMateria: {h}")
    for i in range(len(notas)):
        print (f"{i+1}) nota: {notas[i]}")
    
    print ("- - - - - - - - - - - - - - - - -")
    op = input ("¿Desea guardar los datos ingresados? \n "
                "si_ Para guardar los datos. \n" 
                " no_ Para volver a cargar los datos.\n").lower()
    if op == "si":
        
        file_id = open ("archivos_txt/id.txt", "a+")
        file_id.write(str(id))
        file_id.write(" \n")
        file_id.close()

        file_nombre1 = open ("archivos_txt/nombre1.txt", "a+")
        file_nombre1.write(nombre1)
        file_nombre1.write(" \n")
        file_nombre1.close()

        file_nombre2 = open ("archivos_txt/nombre2.txt", "a+")
        file_nombre2.write(nombre2)
        file_nombre2.write(" \n")
        file_nombre2.close()

        file_apellido1 = open ("archivos_txt/apellido1.txt", "a+")
        file_apellido1.write(apellido1)
        file_apellido1.write(" \n")
        file_apellido1.close()

        file_apellido2 = open ("archivos_txt/apellido2.txt", "a+")
        file_apellido2.write(apellido2)
        file_apellido2.write(" \n")
        file_apellido2.close()

        file_edad = open ("archivos_txt/edad.txt", "a+")
        file_edad.write(str(edad))
        file_edad.write(" \n")
        file_edad.close()

        file_dni = open ("archivos_txt/dni.txt", "a+")
        file_dni.write(str(dni))
        file_dni.write(" \n")
        file_dni.close()
        
        file_materia = open ("archivos_txt/materia.txt", "a+")
        file_materia.write(materia)
        file_materia.write(" \n")
        file_materia.close()

        file_notas = open ("archivos_txt/notas.txt", "a+")
        for i in notas:
            nota1 = i
            file_notas.write(str(nota1))
            file_notas.write(" \t")    
        file_notas.write("\n")
        file_notas.close()

        alumno =[]
        notas = []

    elif op == "no":
        print ("Volviendo al menu de carga")
        

    else:
        print ("Ingrese una opcion correcta")    
    

    
    
    
    
    
    
    








