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


print ("Ingrese una contraseña y el programa le indicara si es segura o no.")

seguro = False
while seguro ==False:
    contrasenia = input("Ingrese una contraseña: \n")

    largo_contr = False
    if len(contrasenia) >= 10:
        largo_contr = True
    else:
        print ("La contraseña es demasiado corta. \n"
            "Contraseña Insegura.")
        
        

    tiene_numero = False
    if any([dig.isdigit() for dig in contrasenia]):
        tiene_numero = True
    else:
        print ("La contraseña no tiene números. \n"
            "Contraseña insegura.")
        
        
    tiene_espacio = False
    if contrasenia.count(" ") > 0:
        print ("La contraseña no debe tener espacios. \n"
            "Contraseña Insegura.")
        
    else:
        tiene_espacio = True

    tiene_mayuscula = False
    for i in contrasenia:
        if i.isupper():
            print (i)
            tiene_mayuscula = True
            break
        else:
            print ("La contraseña no contiene mayusculas. \n"
                "Contraseña Insegura")
           

    tiene_minuscula = False
    for i in contrasenia:
        if i.islower():
            print (i)
            tiene_minuscula = True
            break
        else:
            print ("La contraseña no contiene minusculas. \n"
            "Contraseña Insegura")
            

    if tiene_minuscula==True and tiene_mayuscula==True and tiene_espacio==False and tiene_numero==True and largo_contr == True:
        print ("CONTRASEÑA SEGURA")
        seguro = True