nro1 = int (input("Ingrese un número: "))
nro2 = int (input("Ingrese un número: "))
nro3 = int (input("Ingrese un número: "))

res = nro3 + nro2 + nro1

if res > 10:
    res = res//2
else: 
    res = pow(res, 3)

print (f"el resultado es: {res}")

