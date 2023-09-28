import abrir_listas_e_imprimir as a_l_i

def modificar_alumno():
    
    print ("Vea primero la lista de alumnos.")
    while True:
        opc = input("Si ya vio la lista de alumnos presione:\n"
                    "C continuar.\n"
                    "De lo contrario presione:\n"
                    "V volver.\n")
        opc = opc.upper()
        if opc == "C":
            select_id = int (input("Seleccione la ID del alumno a modificar: \n"))
            pos = select_id - 1
            a_l_i.imprimir_un_alumno(pos)
            lista_id = a_l_i.abrir_id()
            lista_nombre1 = a_l_i.abrir_nombre1()
            lista_nombre2 = a_l_i.abrir_nombre2()
            lista_apellido1 = a_l_i.abrir_apellido1()
            lista_apellido2 = a_l_i.abrir_apellido2()
            lista_edad = a_l_i.abrir_edad()
            lista_dni = a_l_i.abrir_dni()
            lista_materia = a_l_i.abrir_materia()
            lista_notas = a_l_i.abrir_notas()
            print ("control de listas originales.  se borra este print cuando el programa funcione\n"
                   f"lista id: {lista_id}\nLista nombre 1: {lista_nombre1}\nLista nombre 2: {lista_nombre2}\n"
                   f"lista apellido 1: {lista_apellido1}\nLista apellido2: {lista_apellido2}\nlista edad: {lista_edad}\n"
                   f"lista DNI: {lista_dni}\n lista materias: {lista_materia}\n lista notas: {lista_notas}\n")
            
            #Ingresando los datos nuevos del alumno selecccionado
            nombre1 = input ("Ingrese el 1er nombre nuevamente: ")

            nombre2 = input ("Ingrese el 2do nombre nuevamente: ")

            apellido1 = input ("Ingrese el 1er apellido nuevamente: ")
 
            apellido2 = input("Ingrese el 2do apellido nuevamente: ")
 
            edad = input("Ingrese la edad nuevamente: ")

            dni = input("Ingrese la dni nuevamente: ")

            materia = input("Ingrese la materia nuevamente: ")

            notas = []
            opc = int( input("Cuantas notas va a ingresar nuevamente: "))
            for i in range(opc):
                nota = int( input(f"Ingrese la nota nro {i+1} del alumno: "))
                notas.append(nota)

            print (f"\nPara la id: {lista_id[pos]}\n"
                    "\t\tDatos anteriores \tDatos Actuales\n"
                    f"Nombre 1:\t {lista_nombre1[pos]} \t\t\t {nombre1}\n"
                    f"Nombre 2:\t {lista_nombre2[pos]} \t\t\t {nombre2}\n"
                    f"Apellido 1:\t {lista_apellido1[pos]} \t\t {apellido1}\n"
                    f"Apellido 2:\t {lista_apellido2[pos]} \t\t {apellido2}\n"
                    f"edad:\t\t {lista_edad[pos]} \t\t\t {edad}\n"
                    f"DNI:\t\t {lista_dni[pos]} \t\t {dni}\n"
                    f"MAteria:\t {lista_materia[pos]} \t\t {materia}\n"
                    f"Notas:\t\t {lista_notas[pos]} \t\t\t {notas}\n")
            
            lista_nombre1.pop(pos)
            lista_nombre1.insert(pos, nombre1)

            lista_nombre2.pop(pos)
            lista_nombre2.insert(pos, nombre2)
            
            lista_apellido1.pop(pos)
            lista_apellido1.insert(pos,apellido1)

            lista_apellido2.pop(pos)
            lista_apellido2.insert(pos,apellido2)

            lista_edad.pop(pos)
            lista_edad.insert(pos,edad)
            
            lista_dni.pop(pos)
            lista_dni.insert(pos,dni)

            lista_materia.pop(pos)
            lista_materia.insert(pos, materia)

            print ("control de listas modificadas.  se borra este print cuando el programa funcione\n"
                f"lista id: {lista_id}\nLista nombre 1: {lista_nombre1}\nLista nombre 2: {lista_nombre2}\n"
                f"lista apellido 1: {lista_apellido1}\nLista apellido2: {lista_apellido2}\nlista edad: {lista_edad}\n"
                f"lista DNI: {lista_dni}\n lista materias: {lista_materia}\n lista notas: {lista_notas}\n")



            #seguramente aca hay que hacer un break
        elif opc == "V":
            print ("Volviendo al menu principal")
            break
        
        else:
            print ("Ingrese una opcion correcta")
        
    





