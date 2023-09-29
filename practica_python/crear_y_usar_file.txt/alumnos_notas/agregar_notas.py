import abrir_listas_e_imprimir as a_l_i
import re

def agregar_nota():
    
    print ("\nVea primero la lista de alumnos.")
    while True:
        opc = input("\nSi ya vio la lista de alumnos presione:\n"
                    "C continuar.\n"
                    "De lo contrario presione:\n"
                    "V volver.\n")
        opc = opc.upper()
        if opc == "C":
            select_id = int (input("Seleccione la ID del alumno al cual modificara las notas: \n"))
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

            #Ingresando los notas nuevas del alumno selecccionado
            
            lista_notas2 = []

            numeros = re.split ("\D+", lista_notas[pos])

            for i in range (len(numeros)):
                num = numeros[i]
                lista_notas2.append(num)
                
            opc = int( input("Cuantas notas va a agreagr: "))
            for i in range(opc):
                nota = int( input(f"Ingrese la nota a agregar nro {i+1} del alumno: "))
                lista_notas2.append(str(nota))
            notas2 = " -- ".join(lista_notas2)

            print (f"\nPara la id: {lista_id[pos]}\n"
                    "\t\tDatos anteriores \tDatos Actuales\n"
                    f"Nombre 1:\t {lista_nombre1[pos]}\t "
                    f"Nombre 2:\t {lista_nombre2[pos]} \n  "
                    f"Apellido 1:\t {lista_apellido1[pos]}\t "
                    f"Apellido 2:\t {lista_apellido2[pos]}\n "
                    f"edad:\t\t {lista_edad[pos]} \t"
                    f"DNI:\t\t {lista_dni[pos]} \t"
                    f"Materia:\t {lista_materia[pos]}\n "
                    f"Notas ya ingresadas:\t {lista_notas[pos]}\n Notas ingresadas mas agregadas: {notas2}\n")
            # Agregando los datos nuevos a las listas
            
            lista_notas.pop(pos)
            lista_notas.insert(pos, notas2)

            #pasando los datos de las listas a los txt
            opc = input ("¿Esta seguro de los cambios a realizar?\n"
                         "Luego no se podran revertir los cambios.\n"
                         "Si esta seguro presione\n"
                         " si\n"
                         "de los contrario presione:\n no\n").upper()
            
            if opc == "SI":
                
                arch_notas = open ("archivos_txt/notas.txt", "w+", encoding="utf-8")
                arch_notas.seek(0)
                for i in range (len(lista_notas)):
                    arch_notas.write(lista_notas[i])
                    arch_notas.write("\n")
                arch_notas.close()
                break


            elif opc == "NO":
                print ("Volviendo al menu anterior.\n")
                break
            else:
                print ("Ingrese una opcion correcta.")


        elif opc == "V":
            print ("Volviendo al menu principal")
            break
        
        else:
            print ("Ingrese una opcion correcta")
