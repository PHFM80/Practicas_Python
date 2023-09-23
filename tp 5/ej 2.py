print ("Ciclo 'while'")
finCont = 10
cont = 0
acum = int(0)

while cont < 10:
    print (f"El contador es: {cont}, el acumulador es: {acum}")
    nro = int(input("Ingrese un número: "))
    acum = acum + nro
    cont = cont +1

print (f"La suma de los números es: {acum}")   
print (f"El contador es: {cont}")

print("- -  - - -  - -")

print ("Ciclo 'for'")
acum2 = int(0)

for i in range(10):
    nro = int(input("Ingrese un número: "))
    acum2 = acum2 + nro

print (f"La suma de los números es: {acum2}")
print (f"El contador es: {i+1}")