import metodos_alumnos as m_a

print ("Menu para ingresar, modificar, eliminar, alumnos y sus notas.")

while True:
    try:
        opc = int(input ("Ingrese la opcion que desea realizar: \n"
                     "\t1. Ingresar un alumno.\n"
                     "\t2. Modificar un alumno.\n"
                     "\t3. Eliminar un alumno.\n"
                     "\t4. Modificar notas.\n"
                     "\t5. Agreagr notas.\n"
                     "\t6. Ver Alumno.\n"
                     "\t10. Salir.\n"))
        if opc == 1:
            m_a.ingresar_alumno()
            print (m_a.alumno)
            print (m_a.notas)
            m_a.cargar_alumno_a_txt()
        
        elif opc == 2:
            #m_a.modificar_alumno()
            pass

        elif opc == 3:
            #m_a.eliminar_alumno()
            pass

        elif opc == 4:
            #m_a.modificar_nota()
            pass

        elif opc == 5:
            #m_a.agregar_nota()
            pass

        elif opc == 6:
            #m_a.ver_alumno()
            pass

        elif opc == 10:
            print ("\nSaliendo del programa\n")
            break
        else:
            print ("\nOpcion incorrecta. \n" 
                "Ingrese una opcion correcta\n")

    except ValueError:
        print ("\nOpcion incorrecta. \n" 
               "Ustede ingreso una letra, debe ingresar un número.\n"
                "Ingrese una opcion correcta\n")      









