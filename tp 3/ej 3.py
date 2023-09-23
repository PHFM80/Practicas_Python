print ("Para saber la cantidad de dolares que le corresponden segun la cantidad de pesos que usted posee, debera:")
print ("1) Ingresar primero el valor actual del dolar.")
valorDolar = int(input("Ingrese el valor del dolar: "))
print ("2) Ahora debe ingresar la cantidad de pesos que posee: ")
cantPesos = int(input("Ingrese la cantidad de pesos que quire cambiar: "))
cantDolar = cantPesos/valorDolar
print ("- - - - - - - - - - - - -")
print (f"A usted le corresponden U$ {round(cantDolar, 2)}")