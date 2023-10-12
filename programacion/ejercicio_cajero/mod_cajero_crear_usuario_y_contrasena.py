from os import system
from time import sleep
from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf
import pickle

usuariosConContrasenias = []
usuarios = []
contrasenias = []
def crear_user_cont(self):
    
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
                #verificacion de usuario inexistente
                user = input ("Por favor ingrese un nombre de usuario.\n")
                listaDeUsuarios = open ("archivos_cajero\datos_de_usuarios_con_contrasenias", "ab+")
                listaDeUsuarios.seek(0)
                try:
                    self.usuariosConContrasenias = pickle.load(listaDeUsuarios)
                    print (f"se cargaron {len(self.usuariosConContrasenias)} desde el fichero externo")
                except:
                    print ("El fichero esta vacio")
                finally:
                    listaDeUsuarios.close()



                #creacion de contraseña
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
                salir_dyt_by_pf()
            else:
                print ("Ingrese una opcion correcta.")
                system ("cls")
        except ValueError:
            print ("\nUsted ingreso una letra.\n"
                    "Debe ingresar un número.\n")
