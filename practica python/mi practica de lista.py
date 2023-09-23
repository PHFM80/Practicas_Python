listaNombre = ["pepe", "meme"]
listaApellido = ["pepe", "meme"]
listaDNI = [1234, 4567]

def ingresarDatos():
    global listaNombre
    global listaApellido
    global listaDNI
    nombre = input("Ingrese un nombre: ")
    apellido = input("Ingrese un apellido: ")
    dni = input("Ingrese un DNI: ")
    listaNombre.append(nombre)
    listaApellido.append(apellido)
    listaDNI.append(dni)


while True:
    opcion = int(input("Ingrese una opcion: \n1. Ingresar datos \n2. Mostrar datos \n3. Modificar datos \n4. Salir \n"))
    if opcion == 1:
        ingresarDatos()
    elif opcion == 2:
        for i in range(len(listaNombre)):
            print(f"{i+1})Nombre: {listaNombre[i]} \n  Apellido: {listaApellido[i]} \n  |DNI: {listaDNI[i]}")
            print("")
    elif opcion == 3:
        for i in range(len(listaNombre)):
            print(f"{i+1}) Nombre: {listaNombre[i]} Apellido: {listaApellido[i]} DNI: {listaDNI[i]}")
            print("")
        opModif = int(input("Que dato desea modificar: "))
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese un apellido: ")
        dni = input("Ingrese un DNI: ")
        opModif -= 1
        listaNombre[opModif] =nombre
        listaApellido[opModif] = apellido
        listaDNI[opModif] = dni
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
        