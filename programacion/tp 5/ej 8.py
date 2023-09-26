#Ciclo while
print("ciclo 'while'")

totVentas = 0
contA = 0
contB = 0
contC = 0
acumA = 0
acumB = 0
acumC = 0
montoFinal = 0


while True:
    resp = input('''Si desea ingresar el monto de una venta,
digite "S", de lo contrario digite "N".
Muchas Gracias.   
''').upper()
    print ("...............")
    if resp == "S":
        print ("...............")
        monto = float(input("Ingrese el monto de la venta: "))
        print ("...............")
        if monto > 1 and monto <= 500 :
            contA += 1
            acumA += monto
        elif monto > 500 and monto <= 1000:
            contB += 1
            acumB += monto
        elif monto > 1000:
            contC += 1
            acumC += monto

        montoFinal = acumA + acumB + acumC
        totVentas = contA + contB + contC
    if resp == "N":
        print ("...............")
        print (f'''La cantidad de ventas con montos entre $1 y $500 son: {contA} y
suman un total de: ${acumA}''')
        print (f'''La cantidad de ventas con montos entre $501 y $1000 son: {contB} y
suman un total de: ${acumB}''')
        print (f'''La cantidad de ventas con montos superior a $1001 son: {contC} y
suman un total de: ${acumC}''')
        print (f"La cantidad total de ventas es: {totVentas}")
        print (f"El monto total de ventas es: ${montoFinal}")
        print ("...............")
        print("Gracias por usar el programa")
        print ("...............")
        break
    elif resp != "S" and resp != "N":
        print ("...............")
        print("Por favor ingrese una respuesta valida")
        print ("...............")



