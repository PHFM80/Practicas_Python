nro1 = int (input ("Ingrese el primer número: "))
nro2 = int (input ("Ingrese el segundo número: "))
nro3 = int (input ("Ingrese el tercer número: "))
nro4 = int (input ("Ingrese el cuarto número: "))

mayor = nro1

if nro2 > mayor:
    mayor = nro2
elif nro3 > mayor:
    mayor = nro3
elif nro4 > mayor:
    mayor = nro4

print ("El mayor número es: ", mayor)

       