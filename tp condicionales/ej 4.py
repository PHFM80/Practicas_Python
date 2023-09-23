valorHora = int(input("Ingrese el valor en pesos de la hora: $"))
cantHoras = int(input("Ingrese la cantidad de horas trabajadas: "))

if cantHoras < 40:
    sueldo = cantHoras * valorHora
else: 
    horasExtra = cantHoras - 40
    sueldo = cantHoras * valorHora + horasExtra * (2 * valorHora)

print("El sueldo neto es: $", sueldo)