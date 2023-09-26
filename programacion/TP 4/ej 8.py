nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))

if nota1 > 8 and nota2 > 8:
    cartel = "Aprobacion Directa"
elif nota1 >= 6 and nota2 >= 6:
    cartel = "Rinde Examen Final"
else: cartel = "Debe Recuperar"

print(cartel)