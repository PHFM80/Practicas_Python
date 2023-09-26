#Ciclo "while"
cont = 0
acum = int(0)
nro1 = int(input("Ingrese el primer número de la multiplicacion: "))
nro2 = int(input("Ingrese el segundo número de la multiplicacion: "))

while cont < nro2:
    acum = acum + nro1
    cont = cont + 1
print ("Ciclo 'while'")

print ("El resultado de la multiplicacion es: ", acum)
print (f"El contador es: {cont}")

#Ciclo "for"
acum2 = int(0)
for i in range(nro2):
    acum2 = acum2 + nro1

print (f"La multiplicacion es: {acum2}")
print (f"el acumulador del ciclo for es: {i+1}")


