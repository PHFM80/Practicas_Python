temp1 = int(input("Ingrese la primer temeperatura: "))

temp2 = int(input("Ingrese la segunda temeperatura: "))

temp3 = int(input("Ingrese la tercera temeperatura: "))

prom = (temp1+temp2+temp3)/3

print (f"El promedio de temperaturas es: {prom}°")
if temp1 > prom:
    print("La primera temperatura es mayor al promedio")
elif temp2 > prom:
    print("La segunda temperatura es mayor al promedio")
elif temp3 > prom:
    print("La tercera temperatura es mayor al promedio")
else: 
    print("NO existen temperaturas mayores al promedio")