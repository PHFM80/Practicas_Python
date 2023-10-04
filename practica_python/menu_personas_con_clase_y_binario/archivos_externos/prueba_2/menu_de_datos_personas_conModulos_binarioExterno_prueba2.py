import modulos_del_menu_prueba2 as mm



while True:
    print ("Seleccione una opcion del menu:\n"
       "\t1. Ingresar una persona.\n"
       "\t2. Ver las personas ingresadas.\n"
       "\t3. Modificar los datos de una persona.\n"
       "\t4. Eliminar una persona.\n"
        "\t5. Salir del programa.\n")
    opc = int (input("Seleccione una opcion:\n"))

    try:
        if opc == 1:
            mm.ingresar_persona()
            pass
        
        elif opc == 2:
            mm.listaPrincipalDePersonas.mostrar_fichero_externo()
        
        elif opc == 3:
            pass
        
        elif opc == 4:
            pass
        
        elif opc == 5:
            print ("\nSaliendo del programa...\n"
                "\t\t\t\tD & T\n"
                "\t\t\tPropuestas Digitales\n")
            break
        
        else:
            print ("Ingrese una oncion correcta")
    except ValueError:
        print("Ingreso una letra.\n"
              "Debe ingresar un número")
    