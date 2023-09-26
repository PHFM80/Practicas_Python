#Ciclo while
cont = 0 
acum = int (0)
cantAlum = int(input("Ingrese un número de alumnos: "))

while cont < cantAlum:
    edad = int(input(f"Ingrese la edad del alumno n° {cont+1}: "))
    acum = acum + edad
    cont = cont + 1

media = acum / cantAlum

print(f"La media de las edades es: {media}")

#ciclo for
acum2 = int(0)
for i in range(0, cantAlum):
    edad = int(input(f"Ingrese la edad del alumno n° {i+1}: "))
    acum2 = acum2 + edad

media2 = acum2 / cantAlum

print(f"La media de las edades es: {media2}")
