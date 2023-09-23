import modulo_tp2_1 as mod

print ("Trabajo practico N° 2 de 'Practica profecionalizante I'")

while True:
    opc = int (input ("Seleccione una opcion: \n"
                      "1. Ejercicio nro 1\n"
                      "2. Ejercicio nro 2\n"
                      "3. Ejercicio nro 3\n"
                      "4. Ejercicio nro 4\n"
                      "5. Ejercicio nro 5\n"
                      "6. Ejercicio nro 6\n"
                      "7. Salir. \n"))
    
    if opc == 1:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_1()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")
    elif opc == 2:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_2()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")

    elif opc == 3:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_3()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")                

    elif opc == 4:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_4()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")
    
    elif opc == 5:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_5()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")
    
    elif opc == 6:
        while True:
            opc2 = input ("C. Si desea continuar.\n"
                          "V. Si desea volver.\n")
            if opc2 == "C" or opc2 == "c":
                mod.ejercicio_6()
            elif opc2 == "V" or opc2 == "v":
                print ("Volviendo a la pantalla principal.\n"
                       "..\n"
                       "...\n")
                break
            else:
                print ("Ingrese una opcion correcta")
    
    elif opc == 7:
        print ("Saliendo del Programa.\n"
               "Gracias por utilizar los servicios de D & T")
        break
    
    else:
        print ("Ingrese una opcion correcta")
