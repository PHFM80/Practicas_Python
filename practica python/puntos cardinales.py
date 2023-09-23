def ingresarDatos():
    ejeX = int(input("Ingrese la coordenada del eje 'X'\n"))
    print("")
    ejeY = int(input("Ingrese la coordenada del eje 'Y'\n"))
    print("")
    return ejeX, ejeY
    
def imprimirDatos():
    ejeX, ejeY = ingresarDatos()

    cuad1 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra en el cuadrante N° 1"
    cuad2 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra en el cuadrante N° 2"
    cuad3 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra en el cuadrante N° 3"
    cuad4 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra en el cuadrante N° 4"
    cuad1_2 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra entre los cuadrantes 1 y 2"
    cuad2_3 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra entre los cuadrantes 2 y 3"
    cuad3_4 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra entre los cuadrantes 3 y 4"
    cuad4_1 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra entre los cuadrantes 4 y 1"
    cuad0_0 = f"  Para los valor de X = {ejeX} e Y = {ejeY}.\n  Ustede se encuentra en el centro de los cuadrantes"

    if ejeX == 0 and ejeY == 0:
        print(cuad0_0)

    elif ejeX == 0 and ejeY > 0:
        print(cuad4_1)

    elif ejeX == 0 and ejeY < 0:
        print(cuad2_3)

    elif ejeX > 0 and ejeY == 0:
        print(cuad1_2)

    elif ejeX < 0 and ejeY == 0:
        print(cuad3_4)

    elif ejeX > 0 and ejeY > 0:
        print(cuad1)

    elif ejeX > 0 and ejeY < 0:
        print(cuad2)

    elif ejeX < 0 and ejeY > 0:
        print(cuad4)

    elif ejeX < 0 and ejeY < 0:
        print(cuad3)


print("")
print("Ingrese las coordenadas para determinar en que cuadrante se encuentra")
print("")


while True:
    print("")
    opc = int(input("Ingrese una opcion.\n1.  Ingresar unas cordenadas.\n2.  Salir\n"))
    print("")
    if opc == 1:
        imprimirDatos()
       
    elif opc == 2:
        print("Terminando de ejecutar el programa")
        break




