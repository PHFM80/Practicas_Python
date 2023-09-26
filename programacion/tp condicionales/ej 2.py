cantLapices = int(input("Ingrese la cantidad de lapices: "))

if cantLapices > 1000:
    valor = cantLapices * 85
else: valor = cantLapices * 90

print(f"El valor de la compra es: {valor}")