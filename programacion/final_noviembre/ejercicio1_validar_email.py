
# a) Caracteres permitidos [aA…….zZ] y [0…9] y además   ('.','_','-')    
# b) No se permiten espacios en blanco
# c) El e-mail debe debe iniciar con una letra
# d) Longitud mínima antes del arroba, debe ser de 5 carácteres
# e) Debe contener un solo arroba
# f) Después del arroba, debe estar el dominio: 
#   i. El dominio debe contener por lo menos un punto (.)
#   ii. El punto (.) no debe estar a continuación del arroba ni tampoco debe terminar con un punto.
# g) Luego del punto del dominio se requieren al menos tres caracteres.  

# Funcion validar correo
def validar_correo(correo):
    # CARACTERES PERMITIDOS Y DE PRIMERAS LETRAS PERMITIDAS
    caracterPermitidos = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM1234567890-_."
    letrasIniciales = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM"
        # Verificador de 1 solo arroba
   
    cont_arroba = 0
    for i in (correo):
        if i =="@":
            cont_arroba += 1
    #print (f"El correo: {correo} tiene {cont_arroba} @.")
            #Verificar arroba true o false
    verifArroba = False
    if cont_arroba == 1:
        verifArroba = True

        # Verificador del largo del correo y de los caracteres permitidos
    contLargoDireccion = 0
    for i in (correo):
        if i != "@":
            contLargoDireccion += 1
        elif i == "@":
            break
    #print (f"El largo de la direccion {correo} es: {contLargoDireccion}")
            #Verificar largo de direccion true o false
    verifLargoDireccion = False
    if contLargoDireccion >=5:
        verifLargoDireccion = True 

    cadenaDireccion = correo [0 : contLargoDireccion]
            #Verificar caracteres permitidos dentro de la cadena por true o false
    verifCaracterPermitido = True
    for i in (cadenaDireccion):
        if i in caracterPermitidos:
            #print (f"El caracter {i}, es valido")
            pass
        else:
            #print ("Hay un caracter invalido")
            verifCaracterPermitido = False         

        # Verificacion de letra inicial
            #Verificador true o false del primer caracter letra
    verifPrimerCaracter = True
    for i in (cadenaDireccion[0]):
        if i not in letrasIniciales:
            #print ("El primer caracter no es una letra.")
            verifPrimerCaracter = False

        # Verificar espacios en balnco
            #Verificar espacio en blanco por true o false
    verifEspacioBlanco = True
    for i in (cadenaDireccion):
        if i == " ":
            #print ("Hay un espacion en blanco.")
            verifEspacioBlanco = False

        # Verificacion del dominio
    cadenaDominio = correo [contLargoDireccion+1 : len(correo)]
    #print (cadenaDominio)

        # Verificar un solo punto y en la posiscion correcta
    contPunto = 0
    for i in (cadenaDominio):
        if i == ".":
            contPunto += 1
    #print (f"El contador de puntos es: {contPunto}")
            #Verificador de un solo punto por tru o false
    verfiUnPunto = False
    if contPunto == 1:
        verfiUnPunto = True
            #Verificador de la posiscion correcta del punto y
            # por defecto la cantidad de caracteres posterior a el por true o false
    verifPosicionPunto = False
    for i in (cadenaDominio[-4]):
        if i == ".":
            verifPosicionPunto = True
            #print (f"En la posicion -4 se encuentra el: {i}")

    if  verifArroba == True and verifLargoDireccion == True and verifCaracterPermitido == True and verifPrimerCaracter == True and     verifEspacioBlanco == True and verifPosicionPunto == True and verifPosicionPunto == True:
        return True


# Funcion validar correo en lista
def validar_lista_correos(lista):
    for i in (lista):
        email = validar_correo(i)
        if email == True :
            print (f"El correo {i} es correcto.")
        else:
            print (f"\t\t\tEl correo {i} no es correcto.")


listaCorreos =[" pablito@gmail.com", "p@blito@gmail.com", "pablito@gmail", "pablito@gmail.cm"
               , "1pablito@gmail.com.", "p4blito@gmail.com.", "p@blito@gmail.com", "pablito@gmail.com", 
               "pab_li-to@gmail.com", "pa.blito@gmail.com", "pab lito@gmail.com", "pablito@gmail.net", 
               "pablito@gmail.lol"]

lista_correos_validos = validar_lista_correos(listaCorreos)


# Ingresar correo
#correo = "pablito@gmail.com"
correo = input ("Ingrese su correo electronico:\n")
correoValido = validar_correo(correo)

#print (f"El correo: {correo} es: {correoValido}")

if correoValido == True:
    print ("El correo ingresado es correcto")
else:
    print ("El correo ingresado no es correcto")