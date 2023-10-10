import cajero_ingreso_esp as cie
from os import system
from time import sleep



while True:
    system("cls")
    try:
        
        print ("Bienvenido al servicio de Cajeros Automaticos del Banco IES 9023.\n"
                "Welcome to the IES 9023 ATM.\n")
        opc = int (input( "Por Favor.\n  Seleccione el lenguaje.\n"
                    "  Please, select your lenguage.\n"
                    "1_ Para español.\n"
                    "2_ For english.\n"
                    "3_ Salir del sistema.  Get out of the system.\n"))
        if opc == 1:
            cie.ingreso()
        elif opc == 2:
            pass
        elif opc == 3:
            system ("cls")
            print ("\nSaliendo del programa...\n"
                            "\t\t\t\tD & T\n"
                            "\t\t\tPropuestas Digitales\n"
                            "\t\t\t\t\t\tBY Pablo Flores\n")
            sleep(5)
            system ("cls")
            break
        else:
            print ("Seleccione una opcion valida.\n")
            sleep(3)
            system ("cls")
    
    except ValueError:
        print ("Ingreso una letra.\nYou entered a letter.\n"
            "Debe ingresar un número.\nYou must enter a number\n")
    
