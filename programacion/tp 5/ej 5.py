#ciclo while
cont = 0
acum = int(0)
estat = 0
print ("Ciclo while")
while True:
    estat = int(input(f"Ingrese la estatura de la persona n° {cont + 1}:  "))
    acum = acum + estat
    cont = cont + 1
    if estat == 0:
        break
print ("- -   - - -  - -")
print (f"La cantidad de personas ingresadas es de: {cont-1}")
print(f"La media de las estaturas es: {acum / (cont-1)}")

#Ciclo for
print ("Ciclo for")
acum2 = int(0)
estat2 = 0
for i in estat2:
    estat = int(input(f"Ingrese la estatura de la persona n° {i}: "))
    acum2 = acum2 + estat2
    if estat == 0:
        break

print ("- -   - - -  - -")
print (f"La cantidad de personas es: {i} ")

print(f"La media de las estaturas es: {acum2 / (i)}")



