from os import system
from time import sleep


def crear_user_cont():
    system ("cls")
    print ("Bienvenido al servicio de Cajeros Automaticos del Banco IES 9023.\n"
        "--  --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n"
            "Crear usuario y contraseña.\n"
        "--  --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n"
        "\n")

    while True:
        opc = int(input ("Seleccione una opción:\n"
        "\t1_ Para crear usuario y contraseña.\n"
            "\t2_ Para volver al menu anterior.\n"
            "\t3_ Para salir del sistema.\n"))
        try:
            if opc == 1:
                user = input ("Por favor ingrese su usuario.\n")
                contrasena = input ("Por favor ingrese su contraseña.\n"
                                    "La misma debera contar con:\n"
                                    "\t1) Minimo 12 caracteres.\n"
                                    "\t2) Al menos una mayuscula, una miniscula y un caracter especial.\n"
                                    "\t3) No puede contener espacios en blanco.\n")

                if len(contrasena) < 10:
                    print ("La contraseña debe tener 13 caracteres o mas. \nContraseña Insegura.\n")
                elif not any ([c.isdigit() for c in contrasena]):
                    print ("La contraseña debe tener al menos un número.\n Contraseña Insegura")
                elif not any ([c.islower() for c in contrasena]):
                    print ("La contraseña debe tener letras minusculas.\n Contraseña Insegura")
                elif not any ([c.isupper() for c in contrasena]):
                    print ("La contraseña debe tener letras mayusculas.\n Contraseña Insegura")
                elif (contrasena.count(" ")>0):
                    print ("La contraseña no debe tener espacios.\n Contraseña Insegura")
                else:
                    system ("cls")
                    print ( "\n::::::::::::::::::::::"
                            f"\nUsuario: {user} y\n"
                            f"Contraseña: {contrasena}.\n"
                            "Creados exiosamente.\n"
                            ":::::::::::::::::::::::\n")
                    sleep(6)
                    system ("cls")
                    break
            elif opc == 2:
                system ("cls")
                print ("\nVolviendo al menu anterior...\n")
                sleep(5)
                system ("cls")
                break
                
            elif opc == 3:
                system ("cls")
                print ("\nSaliendo del programa...\n"
                                "\t\t\t\tD & T\n"
                                "\t\t\tPropuestas Digitales\n"
                                "\t\t\t\t\t\tBY Pablo Flores\n")
                sleep(5)
                system ("cls")
                exit (0)
            else:
                print ("Ingrese una opcion correcta.")
                system ("cls")
        except ValueError:
            print ("\nUsted ingreso una letra.\n"
                    "Debe ingresar un número.\n")
