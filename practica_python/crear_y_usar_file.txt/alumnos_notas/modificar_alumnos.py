import abrir_listas_e_imprimir as a_l_i

import abrir_listas_e_imprimir_prueba as v_a_2

def modificar_alumno():
    
    print ("Vea primero la lista de alumnos.")
    select_id = int (input("Seleccione la ID del alumno a modificar: \n"))
    pos = select_id - 1
    a_l_i.imprimir_un_alumno(pos)

    v_a_2.imprimir_un_alumno()
    





