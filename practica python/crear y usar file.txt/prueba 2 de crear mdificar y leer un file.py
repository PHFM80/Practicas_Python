import os

while True:
    opc1 = int(input("\nIngrese la opcion de la accion que desea realizazar○\n"
                     "1. Ingresar un nombre\n"
                     "2. Ver los nombres ingresados.\n"
                     "3. Modificar un nombre.\n"
                     "4. Eliminar un nombre.\n"
                     "5. Salir del programa.\n"))

#Ingresar un nombre y guardarlo en el archivo txt
    if opc1 == 1:
        while True:
            opc2 = input("desea ingresar un nombre.\n"
                         "S para ingresar uno nombre.\n"
                         "N para salir del programa.\n")
            
              
            if opc2 == "S" or opc2 == "s":
                archivo_nombres = open("nombres.txt", "a")
                nombre = input("Ingrese un nombre: ")
                archivo_nombres.write(nombre)
                archivo_nombres.write(" ")
                archivo_nombres.write("\n")
                archivo_nombres.close()
            
            elif opc2 == "n" or opc2 == "N" :
                print("Volviendo al menu anterior")
                break

            else:
                print ("Ingrese una opcion correcta")

#Mostrar los nombres que estan guardados en el archivo txt
    elif opc1 == 2:
        print ("\nSe mostraran los registros de nombres.\n")
        archivo_nombres = open("nombres.txt", "r")
        lista_nombres = archivo_nombres.readlines()
        archivo_nombres.close()
        for i in range (0, len(lista_nombres)):
            print (f"posicion: {i+1}, {lista_nombres[i]}")

#Modificar un nombre que esta guardado en el archivo txt
    elif opc1 == 3:
        #Esto es para visualizar los nombnres contenidos en el archivo txt, para saber cual modificar
        archivo_nombres = open("nombres.txt", "r")
        lista_nombres = archivo_nombres.readlines()
        archivo_nombres.close()
        for i in range (0, len(lista_nombres)):
            print (f"posicion: {i+1}, {lista_nombres[i]}")
        
        posicion = int(input("Ingrese la posicion del nombre que desea modificar: "))
        posicion -= 1
        archivo_nombres = open("nombres.txt", "r+")
        lista_nombres = archivo_nombres.readlines()
        
        # Es para mi control se puede borrar, es para ver como queda conformada la lista
        #print (lista_nombres)
        
        nombre = input ("Ingrese el nuevo nombre: ")
        lista_nombres.pop(posicion)
        lista_nombres.insert(posicion, nombre + " \n")
        print (lista_nombres)

        #Esto es para guardar cada campo de la lista en una linea del archivo Txt
        archivo_nombres.seek(0)
        for i in range(len(lista_nombres)):
            archivo_nombres.write(lista_nombres[i])            

        archivo_nombres.close()

        # Esto es para corroborar que la lista quedo modificada
        # archivo_nombres = open("nombres.txt", "r")
        # lista_nombres = archivo_nombres.readlines()
        # archivo_nombres.close()
        # for i in range (0, len(lista_nombres)):
        #     print (f"posicion: {i+1}, {lista_nombres[i]}")


# Eliminar un nombre que este guardado en el archivo txt
    elif opc1 == 4:
        
        archivo_nombres = open("nombres.txt", "r+")
        lista_nombres = archivo_nombres.readlines()
        archivo_nombres.close()
        for i in range (0, len(lista_nombres)):
            print (f"posicion: {i+1}, {lista_nombres[i]}")
        
        archivo_nombres.close()

        
        posicion = int(input("Ingrese la posicion del nombre que desea eliminar: "))
        posicion -= 1
                
        os.remove("nombres.txt")
        
        # Es para mi control se puede borrar, es para ver como queda conformada la lista
        print ("Lista inicial ")
        print (f"largo de la lista {len(lista_nombres)}")
        print (lista_nombres)
        
        
        lista_nombres.pop(posicion)
        #lista_nombres.append(" ")
        
        print ("lista con el nombre borrado")
        print (f"largo de la lista {len(lista_nombres)}")
        print (lista_nombres)

        #Esto es para guardar cada campo de la lista en una linea del archivo Txt
        archivo_nombres = open("nombres.txt", "w")
        #archivo_nombres.seek(0)
        for i in range(len(lista_nombres)):
            archivo_nombres.write(lista_nombres[i])            

        archivo_nombres.close()

    elif opc1 == 5:
        print ("Saliendo del prgrama...")
        break

    else:
        print ("Ingrese una opcion correcta")
