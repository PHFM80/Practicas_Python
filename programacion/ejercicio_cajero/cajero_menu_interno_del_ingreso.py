

def menu_interno():
    while True:
        try:
            opc = int(input("seleccione la opcion que deea consultar\n"
                            "\t1. Deposito.\n"
                            "\t2. Extraccion.\n"
                            "\t3. Trasnferencia.\n"
                            "\t4. Concusltar saldo.\n"
                            "\t5. Consultar Movimientos.\n"
                            "\t6. Salir del programa.\n"))
            if opc == 1:
                pass
            elif opc == 2:
                pass
            elif opc == 3:
                pass
            elif opc == 4:
                pass
            elif opc == 5:
                pass
            elif opc == 6:
                print ("\nSaliendo del programa...\n"
                    "\t\t\t\tD & T\n"
                    "\t\t\tPropuestas Digitales\n"
                    "\t\t\t\t\t\tBY Pablo Flores\n")
                break
            else:
                print ("ingrese una opcion correcta")
        except ValueError:
            print ("Ingreso una letra, debe ingresar solo numeros.")
   