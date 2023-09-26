puntos = int( input("Ingrese la cantidad de puntos: "))
salarioMinimo = int(input("Ingrese el valor del salario mínimo: "))

if puntos > 151:
    premio = salarioMinimo * 3
elif puntos <= 100:
    premio = salarioMinimo
else:
    premio = salarioMinimo * 2

print("El valor del premio es: $", premio)