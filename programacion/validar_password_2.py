# Ejercicio: 
#    Crear un programa de validación de contraseñas, este debe cumplir con los siguientes requisitos:
#  La contraseña debe contener mínimo 10 caracteres
#  Debe contener al menos; minúscula, mayúscula y números
#  No puede haber espacios en blancos en la contraseña
#  Si cumple con todos estos requisitos debe retornar el mensaje, 
# “La Contraseña es segura”
#    Datos de entrada
#  Contraseña
#    Proceso
#  Validación de la longitud 
#  Comprobación de mayúsculas y minúsculas
#  Comprobación de números y espacios
#    Datos de salida
#  Si no cumple requisitos imprimir errores y el mensaje
# “La contraseña no es segura”
#  Si cumple requisitos imprimir mensaje de “La contraseña es segura”


while True:
    opc = int (input("Ingrese una opcion:\n1. Para contnuar.\n Cualquier otro numero para salir."))
    if opc == 1:
        print ("Ingrese una contraseña y el programa le indicara si es segura o no.")

        contr = input ("Ingrese una contraseña segura: \n")

        if len(contr) < 10:
            print ("La contraseña debe tener 10 caracterres o mas. \nContraseña Insegura.\n")
        elif not any ([c.isdigit() for c in contr]):
            print ("La contraseña debe tener al menos un número.\n Contraseña Insegura")
        elif not any ([c.islower() for c in contr]):
            print ("La contraseña debe tener letras minusculas.\n Contraseña Insegura")
        elif not any ([c.isupper() for c in contr]):
            print ("La contraseña debe tener letras mayusculas.\n Contraseña Insegura")
        elif (contr.count(" ")>0):
            print ("La contraseña no debe tener espacios.\n Contraseña Insegura")
        else:
            print ("La contraseña es Segura")
    else:
        print ("Saliendo del programa")
        break


















