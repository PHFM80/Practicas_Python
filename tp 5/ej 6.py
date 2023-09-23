#Ciclo "while"
mes = int(0)
totalMes = int(0)
totalAnio = int (0)
while mes < 12:
    print (f"Usted esta en el mes n° {mes+1}")
    monto = int(input(f"Ingrese la cantidad de dinero a ahorrar: "))
    totalMes = totalMes + monto
    totalAnio =totalAnio + monto
    mes = mes + 1
    print(". . . . . . . . . .")
    print(f"Su total mensual es de: {totalMes}")

print (": : : : : : : : :")
print ("Ciclo 'while'")
print(f"Su total aual es de: {totalAnio}")
print(f"Usted ahorro durante {mes} meses")
print (": : : : : : : : :")
print (": : : : : : : : :")

#Ciclo "for"

totalMes2 = int(0)
totalAnio2 = int(0)

for i in range(1, 13):
    print (f"Usted esta en el mes n° {i}")
    monto = int(input(f"Ingrese la cantidad de dinero a ahorrar: "))
    totalMes2 = totalMes2 + monto
    print (f"Su total mensual es de: ${totalMes2}")
    totalAnio2 =totalAnio2 + monto

print (": : : : : : : : :")
print ("Ciclo 'for'")
print(f"Su total aual es de: {totalAnio2}")
print(f"Usted ahorro durante {i} meses")
