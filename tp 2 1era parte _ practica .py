import math

def ejercicio_1 ():
    print ("1. Ejercicio 1\n")
    print ("Tienes 150 lápices de colores y quieres distribuirlos por igual entre 7 personas.\n"
       "¿Cuantos lápices utilizara cada persona? ¿Cuántos sobrarán? \n")
    cant_lapices = int(input ("Ingrese la cantidad de lapices: \n"))
    cant_personas = int(input ("\nIngrese la cantidad de personas: \n"))

    div_exacta = cant_lapices // cant_personas
    resto = cant_lapices % cant_personas
    print (f"La cantidad de personas es: {cant_personas}\n"
        f"La cantidad de lapices es: {cant_lapices}\n"
        f"A cada persona le corresponden '{div_exacta}' lapices,\n"
        f"sobraron '{resto}' lapices.")

    print ("\nFin del 1er ejercicio.\n")


def ejercicio_2 ():
    print ("2. Ejercicio 2")

    print ("Una caja de lápices contiene 12 lápices de colores individuales.\n"
        "¿Cuántas cajas necesitarías comprar para dar 15 lápices a cada una de las siete personas? \n")

    lapices_X_caja = int ( input ("Ingrese la cantidad de lapices que vienen en la caja: \n"))
    cant_personas2 = int ( input ("Ingrese la cantidad de personas: \n"))
    cant_lapices2 = int ( input ("Ingrese la cantidad de lapices que le quiere dar a cada persona: \n"))
    cant_cajas = round ((cant_personas2 * cant_lapices2)/lapices_X_caja, 0)

    print (f"\nA cada persona quiere dar {cant_lapices2} lapices, \n"
        f"si cada caja contiene {lapices_X_caja} lapices, \n"
        f"necesitara comprar {cant_cajas} cajas de lapices.")


    print ("\nFin del 2do ejercicio.\n")

def ejercicio_3 ():
    
    print (" Ejercicio 3 \n")
    print ("Tiene dos esferas, la esfera 1 presenta un radio de 5 cm y la esfera 2 presenta un radio de 12.5 cm. \n"
        "¿Cuál es la diferencia de volumen entre las dos esferas? V = 4/3 πr³. \n")

    radio1 = float ( input ("Ingrese el radio de la esfera 1: \n"))

    radio2 = float ( input ("Ingrese el radio de la esfera 2: \n"))

    volumen1 = round ((4/3) * math.pi * (radio1**3), 2) 
    volumen2 = round ((4/3) * math.pi * (radio2**3), 2)

    if volumen1 > volumen2:
        diferencia = round (volumen1 - volumen2, 2)
    else:
        diferencia = round (volumen2 - volumen1, 2)

    print (f"El volumen de la esfera 1 es: {volumen1}\n"
        f"El volumen de la esfera 2 es: {volumen2}\n"
        f"La diferencia de volumen entre las dos esferas es: {diferencia}")

    print ("\nFin del 3er ejercicio.\n")

def ejercicio_4():
        
    print ("Ejercicio 4 \n")
    print ("Realiza un programa que reciba una cantidad de días y devuelva, la cantidad de años, meses y días\n" 
            "en que pueden agruparse esos días")
    dias = int (input("Ingrese la cantidad de dias: \n"))

    dias_a_anios = dias // 365
    resto_dias_anios = dias % 365
    resto_anios_a_meses = resto_dias_anios // 30
    dias_a_meses = dias // 30
    resto_dias_meses = dias % 30

    print(f"\nUsted ingreso {dias} dias, que equiavalen a :\n"
        f"{dias_a_anios} años \n"
        f"{dias_a_meses} meses \n"
        f"y por ultimo equivale a: \n"
        f"{dias_a_anios} años, {resto_anios_a_meses} meses y {resto_dias_meses} dias.")


    print ("\nFin del 4to ejercicio.\n")


def ejercicio_5():
        
    print ("Ejercicio 5 \n")
    print ("Aplicar el Teorema de Pitágoras.\n" 
            "Solicite los datos correspondientes, para su ingreso por teclado. \n")
    opc = int(input("Ingrese una opcion:\n"
                    "1. Para calcular el cateto A.\n"
                    "2. Para calcular el cateto B.\n"
                    "3. Para calcular la hipotenusa.\n"))

    if opc == 1:
        catetoB = float(input("Ingrese el valor del cateto B: \n"))
        hipotenusa = float(input("Ingrese el valor de la hipotenusa: \n"))
        if hipotenusa > catetoB:
            catetoA = round(math.sqrt(hipotenusa**2 - catetoB**2), 2)
            print(f"El cateto A es: {catetoA}")
        else: 
            print (f"El cateto B ({catetoB}), no puede ser mayor que la hipotenusa  ({hipotenusa})")

    elif opc == 2:
        catetoA = float(input("Ingrese el valor del cateto A: \n"))
        hipotenusa = float(input("Ingrese el valor de la hipotenusa: \n"))
        if hipotenusa > catetoA:
            catetoB = round (math.sqrt(hipotenusa**2 - catetoA**2), 2)
            print(f"El cateto B es: {catetoB}")
        else:
            print (f"El cateto A ({catetoA}), no puede ser mayor que la hipotenusa  ({hipotenusa})")
        

    elif opc == 3:
        catetoA = float(input("Ingrese el valor del cateto A: \n"))
        catetoB = float(input("Igrese el valor del cateto B: \n"))
        hipotenusa = round (math.sqrt(catetoA**2 + catetoB**2), 2)
        print (f"La hipotenusa es: {hipotenusa}")                    

    print ("\nFin del 5to ejercicio.\n")

def ejercicio_6():
        
    print ("Ejercicio 6 \n")
    print ("calcule el seno, coseno, tangente de un angulo ingresado por teclado.\n")

    angulo = float(input("Ingrese el valor del angulo: \n"))

    seno = round(math.sin(math.radians(angulo)), 2)

    coseno = round(math.cos(math.radians(angulo)), 2)

    tangente = round(math.tan(math.radians(angulo)), 2)

    print (f"El seno de {angulo} es: {seno}")
    print (f"El coseno de {angulo} es: {coseno}")
    print (f"El tangente de {angulo} es: {tangente}")

    print ("\nFin del 6to ejercicio.\n")
