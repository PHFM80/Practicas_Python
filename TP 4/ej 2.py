nro1 = int (input("Ingrese un número: "))

nro2 = int (input("Ingrese otro número: "))

if nro1 == 0:
    print(f"El número {nro2} no se puede dividir por {nro1}")
else: 
    res = nro1 / nro2
    print(f"El resultado es {res}")
    