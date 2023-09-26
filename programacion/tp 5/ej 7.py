#Ciclo while
cont = 0
acumPos = 0
acumNeg = 0
nro = int(0)
maxCant = int(input("Ingrese la cantidad de números que va a contabilizar: "))

print ("ciclo 'while'")
while cont < maxCant:
    cont = cont + 1
    nro = int(input("Ingrese un número: "))
    if nro > 0:
        acumPos = acumPos + 1
    else:
        acumNeg = acumNeg + 1


print(f"Número de positivos: {acumPos}")

print(f"Número de negativos: {acumNeg}")

print(f"cantidad de números: {cont}")
print ("- -  - - -  - -")
#ciclo for

acumPos2 = 0
acumNeg2 = 0
maxCant2 = int(input("Ingrese la cantidad de números que va a contabilizar: "))

print ("ciclo 'for'")
for i in range(0, maxCant2):
    nro2 = int(input("Ingrese un número: "))
    if nro2 > 0:
        acumPos2 = acumPos2 + 1
    else:
        acumNeg2 = acumNeg2 + 1

print(f"Número de positivos: {acumPos2}")

print(f"Número de negativos: {acumNeg2}")

print(f"cantidad de números: {i+1}")
