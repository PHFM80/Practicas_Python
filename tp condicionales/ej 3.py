valorTraje = int(input("Ingrese el valor del traje: $"))

if valorTraje <= 2500:
    totalPagar = valorTraje * 0.92
else: totalPagar = valorTraje * 0.85

print(f"El valor del traje es de $ {valorTraje} y el total a pagar es de $ {totalPagar}")