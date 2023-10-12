from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf
import mod_cajero_crear_usuario_y_contrasena as c_u_c
from os import system
from time import sleep


def ingreso():
    sleep(3)
    system("cls")
    
    try:
        
        while True:
            print ("Para Ingresar al sistema debera contar con un usuario y contraseña.\n"
                    "\n"
                    "--  --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")
            opc = int (input("Si ya posee un usuario y contraseña.\n"
                        "Digite \t1\n"
                        "Si no posee un usuario y contraseña y quiere crearlo.\n"
                        "Digite \t2\n"
                        "Para salir del cajero.\n"
                        "Digite \t3\n"
                        "\n"))
            print ("")
            if opc == 1:
                #crear_usuario_y_contrasenia()
                pass
            elif opc == 2:
                c_u_c.crear_user_cont()
                
            elif opc == 3:
                salir_dyt_by_pf()
                
            else:
                print ("Ingrese una opcion valida.\n")
                sleep(3)
                system ("cls")
    except ValueError:
        print ("\nUsted ingreso una letra.\n"
            "Debe ingresar un número.\n")
        sleep(3)
        system ("cls")

        
