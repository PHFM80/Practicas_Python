from random import randint
from os import system
from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf



while True:

    print ("Ingresar numeros en una matriz cuadrada n x n, en donde n es un numero positivo menor que 10 que se ingresara por teclado.\n  El programa debera mostrar:\n"
"A) El promedio de los elementos de la diagonal principal.\n"
"B) El promedio de cada una de las filas almacenando los resultados en un nuevo vector unidimencional\n"
"C) Mostrar la matriz.\n")
    try:
        largo_n = int (input("Ingrese el largo de de la matriz cuadrada.\n"
                     "el cual debe ser un numero positivo menor a 10\n")) 
        if largo_n > 0 and largo_n <= 10:
            matriz = []
            for i in range (largo_n):
                matriz.append([0]*largo_n)
            
            #llenado de matriz aleatoriamente
            for i in range (largo_n):
                for j in range (largo_n):
                    matriz[i][j] = randint(0, 100)
            
            # impresion de matriz
            for i in matriz:
                print ("\n")
                for j in i:
                    print (j, end="\t")
            
            #promedio diagonal principal
            diagPrincipal = []
            for i in range (largo_n):
                for j in range (largo_n):
                    if i == j:
                        num = matriz[i][j]
                        diagPrincipal.append(num)
            print (f"\nLa diagonal principal es: {diagPrincipal}\n"
                   f"La suma de la diagonal principal es: {sum (diagPrincipal)}\n"
                   f"El promedio de la diagonal principal es: {(sum (diagPrincipal))/(len(diagPrincipal))}\n")

            #promedio y listas nuevas de las filas
            for i in range (len(matriz)) :
                print (f"\nLa fila nro {i} de la matriz es: {matriz[i]}\n"
                       f"Y su promedio es: {(sum(matriz[i])/len(matriz[i]))}\n")




            opc = input ("\nDesea repetir el proceso.\n"
                         "SI_ para repetir.\n"
                         "NO_ para salir.\n").upper()
            if opc == "SI":
                system("cls")
                pass
                

            elif opc == "NO":
                salir_dyt_by_pf()
                
        else:
            print ("Ingrese un valor adecuado")
    except ValueError:
        print ("\nwarnign  --  warning  -- warning  --  warning  -- warning\n"
            "\t\tIngreso una letra.\n"
               "\tDebe ingresar un valor numerico.\n")