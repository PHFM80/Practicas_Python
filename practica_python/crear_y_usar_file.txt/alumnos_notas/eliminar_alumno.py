import abrir_listas_e_imprimir as a_l_i


def eliminar_alumno():
    
    print ("\nVea primero la lista de alumnos.")
    while True:
        opc = input("\nSi ya vio la lista de alumnos presione:\n"
                    "C continuar.\n"
                    "De lo contrario presione:\n"
                    "V volver.\n")
        opc = opc.upper()
        if opc == "C":
            select_id = int (input("Seleccione la ID del alumno a eliminar: \n"))
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

            #Ingresando los datos nuevos del alumno selecccionado
            nombre1 = ""
            nombre2 = ""
            apellido1 = ""
            apellido2 = ""
            edad = ""
            dni = ""
            materia = ""
            notas2 = ""

            # Agregando los datos nuevos a las listas
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

            lista_notas.pop(pos)
            lista_notas.insert(pos, notas2)

            #pasando los datos de las listas a los txt
            opc = input ("¿Esta seguro de eliminar al alumno?\n"
                         "Luego no se podran revertir los cambios.\n"
                         "Si esta seguro presione\n"
                         " si\n"
                         "de los contrario presione:\n no\n").upper()
            
            if opc == "SI":
                arch_nombre1 = open("archivos_txt/nombre1.txt", "w+", encoding="utf-8")
                arch_nombre1.seek(0)
                for i in range(len(lista_nombre1)):
                    arch_nombre1.write(lista_nombre1[i])
                    arch_nombre1.write("\n")
                arch_nombre1.close()

                arch_nombre2 = open("archivos_txt/nombre2.txt", "w+", encoding="utf-8")
                arch_nombre2.seek(0)
                for i in range (len(lista_nombre2)):
                    arch_nombre2.write(lista_nombre2[i])
                    arch_nombre2.write("\n")
                arch_nombre2.close()

                arch_apellido1 = open ("archivos_txt/apellido1.txt", "w+", encoding="utf-8")
                arch_apellido1.seek(0)
                for i in range(len(lista_apellido1)):
                    arch_apellido1.write(lista_apellido1[i])
                    arch_apellido1.write("\n")
                arch_apellido1.close()

                arch_apellido2 = open("archivos_txt/apellido2.txt", "w+", encoding="utf-8")
                arch_apellido2.seek(0)
                for i in range(len(lista_apellido2)):
                    arch_apellido2.write(lista_apellido2[i])
                    arch_apellido2.write("\n")
                arch_apellido2.close()

                arch_edad = open ("archivos_txt/edad.txt", "w+", encoding="utf-8")
                arch_edad.seek(0)
                for i in range(len(lista_edad)):
                    arch_edad.write(lista_edad[i])
                    arch_edad.write("\n")
                arch_edad.close()

                arch_dni = open ("archivos_txt/dni.txt", "w+", encoding="utf-8")
                arch_dni.seek(0)
                for i in range(len(lista_dni)):
                    arch_dni.write(lista_dni[i])
                    arch_dni.write("\n")
                arch_dni.close()

                arch_materia = open ("archivos_txt\materia.txt", "w+", encoding="utf-8")
                arch_materia.seek(0)
                for i in range (len(lista_materia)):
                    arch_materia.write(lista_materia[i])
                    arch_materia.write("\n")
                arch_materia.close()

                arch_notas = open ("archivos_txt/notas.txt", "w+", encoding="utf-8")
                arch_notas.seek(0)
                for i in range (len(lista_notas)):
                    arch_notas.write(lista_notas[i])
                    arch_notas.write("\n")
                arch_notas.close()
            break

        elif opc == "V":
            print ("Volviendo al menu principal")
            break
        
        else:
            print ("Ingrese una opcion correcta")