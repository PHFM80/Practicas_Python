import ingresos_alumnos as i_a
import modificar_alumnos as m_a
import abrir_listas_e_imprimir as v_a
import eliminar_alumno as e_a
import modificar_notas as m_n
import agregar_notas as a_n


print ("Menu para ingresar, modificar, eliminar, alumnos y sus notas.")

while True:
    try:
        opc = int(input ("Ingrese la opcion que desea realizar: \n"
                     "\t1. Ingresar un alumno.\n"
                     "\t2. Modificar un alumno.\n"
                     "\t3. Eliminar un alumno.\n"
                     "\t4. Modificar notas.\n"
                     "\t5. Agreagr notas.\n"
                     "\t6. Ver Todos los Alumnos.\n"
                     "\t10. Salir.\n"))
    
        if opc == 1:
            i_a.ingresar_alumno()
        
        elif opc == 2:
            m_a.modificar_alumno()
            
        elif opc == 3:
            e_a.eliminar_alumno() 
                
        elif opc == 4:
            m_n.modificar_nota()
        
        elif opc == 5:
            a_n.agregar_nota()
        
        elif opc == 6:
            v_a.imprmir_alumnos()

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
       









