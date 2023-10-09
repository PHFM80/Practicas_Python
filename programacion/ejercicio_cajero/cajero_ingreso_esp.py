from os import system
from time import sleep


def ingreso():
    sleep(3)
    system("cls")
    print ("Para Ingresar al sistema debera contar con un usuario y contraseña.\n"
       "\n"
       "--  --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")
    try:
        while True:
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
                #ingresar_al_sistema()
                pass
            elif opc == 3:
                system ("cls")
                print ("\nSaliendo del programa...\n"
                            "\t\t\t\tD & T\n"
                            "\t\t\tPropuestas Digitales\n"
                            "\t\t\t\t\t\tBY Pablo Flores\n")
                break
                
            else:
                print ("\Ingrese una opcion valida.\n")
                system ("cls")
    except ValueError:
        print ("\nUsted ingreso una letra.\n"
            "Debe ingresar un número.\n")

        
