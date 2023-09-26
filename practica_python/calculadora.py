
def ingresarNrs():
    nro1 = int(input("Ingrese el primer numero: "))
    nro2 = int(input("Ingrese el segundo numero: "))
    return nro1, nro2

def suma():
    print ("+ + + + + + + + + + + +")
    nro1, nro2 = ingresarNrs()
    suma = nro1 + nro2
    print (f"La suma de: {nro1} + {nro2} = {suma}")
    print ("+ + + + + + + + + + + +")
    print("")

def resta():
    print ("- - - - - - - - - - - - - -")
    nro1, nro2 = ingresarNrs()
    resta = nro1 - nro2
    print (f"La resta de: {nro1} - {nro2} = {resta}")
    print ("- - - - - - - - - - - - - -")
    print("")

def multiplicacion():
    print ("* * * * * * * * * * * * *")
    nro1, nro2 = ingresarNrs()
    multiplicacion = nro1 * nro2
    print (f"La multiplicacion de: {nro1} * {nro2} = {multiplicacion}")
    print ("* * * * * * * * * * * * * *")
    print("")

def division():
    print ("/ / / / / / / / / / / / / /")
    nro1, nro2 = ingresarNrs()
    if nro2 == 0:
        print (f"No se puede dividir por '0'")
    else:
        decimales = int(input("Ingrese la cantidad de decimales a ver: "))
        division = nro1 / nro2
        print (f"La division de: {nro1} / {nro2} = {round(division, decimales)}")
    print ("/ / / / / / / / / / / / / /")
    print("")

def potenciacion():
    print ("** ** ** ** ** ** ** ** ** ** ** **")
    print ("El 1er número que se ingresa es la base de la potencia.   \n"
           "El 2do número que se ingresa es el exponente.")
    nro1, nro2 = ingresarNrs()
    potenciacion = nro1 ** nro2
    print (f"La potenciacion de: {nro1} elevado al/a {nro2} = {potenciacion}")
    print ("** ** ** ** ** ** ** ** ** ** ** **")
    print("")


def radicacion():
    print ("v* v* v* v* v* v* v* v* v* v* v* v* v*")
    print ("El 1er número que se ingresa es el indice de la raiz.   \n"
           "El 2do número que se ingresa es el radicando.")
    nro1, nro2 = ingresarNrs()
    decimales = int(input("Ingrese la cantidad de decimales a ver: "))
    radicacion = nro2 ** (1/nro1)
    print (f"La raiz {nro1} de {nro2} = {round(radicacion, decimales)}")
    print ("v* v* v* v* v* v* v* v* v* v* v* v* v*")
    print("")

    

print("")
print ("Bienvenido a la calculadora de Pablo")


while True:
    print("")
    print ("Ingrese el tipo de operacion a relizar")
    print("")
    opcion = int(input("1. Suma\n2. Resta\n3. Multiplicación\n"
                       "4. División\n5. Potenciacion\n6. Radicacion\n7. Salir\n   \n"))
    print("")
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        potenciacion()
    elif opcion == 6:
        radicacion()
    elif opcion == 7:
        print ("Gracias por usar calculadora Pablo\n "
               "Vuelva a utilizarla cuando necesite")
        print("")
        break
    else:
        print ("Opción no valida\n  "
               "Ingrese una opcion correcta")
    


