from random import randint

def meses(dia):
    if dia == 0: return("Enero")
    elif dia == 1: return("Febrero")
    elif dia == 2: return("Marzo")
    elif dia == 3: return("Abril")
    elif dia == 4: return("Mayo")
    elif dia == 5: return("Junio")
def zapatos(nun):
    if nun == 0: return("Modelo 1")
    elif nun == 1: return("Modelo 2")
    elif nun == 2: return("Modelo 3")
    elif nun == 3: return("Modelo 4")
    elif nun == 4: return("Modelo 5")
    elif nun == 5: return("Modelo 6")
def max_ventas_mensual(totVentasLista):
    max = 0
    for x in totVentasLista:
        if x > max:
            max = x
    return (max)

print ("En una Zapatería se conocen las ventas mensuales de 6 modelos de zapatos desde enero "
"hasta junio, cuyo inventario inicial fue de 30 pares de cada modelo.\n"
"Escriba un diagrama de flujo que proporcione la información que necesita el dueño para "
"realizar los pedidos del segundo semestre del año:\n"
"a) Cuales modelos de zapatos debe pedir porque ya no tiene existencias?\n"
"b) Cual modelo fue el menos vendido?\n"
"c) En que mes se vendieron más zapatos ?\n"
"d) Cual es el mes en que más se vendieron zapatos de los modelo 3 ?\n"
"e) Total de zapatos vendidos en estos 6 meses ?\n")


matrizVentas = []
for i in range(6):
    matrizVentas.append ([0]*6)

#carga manual de ventas de zapatos
# for i in range(6):
#     for j in range(6):
#         vendido = int( input (f"Para el mes {meses(i)}, ingrese cuantos {zapatos(j)} vendio: \n") )
#         matrizVentas[i][j] = vendido 

#carga automatica de ventas de zapatos
for i in range(6):
    for j in range(6):
        matrizVentas[i][j] = randint(0,5)

#impresion de matriz
for i in range(len(matrizVentas)):
    print ("\n")
    for j in range(len(matrizVentas[i])):
        print (matrizVentas[i][j], end=(" "))
print ("")
#calculo de ventas mensuales
totVentasLista = []
for i in range (len(matrizVentas)) :
    totVentas = sum(matrizVentas[i])
    #print (f"En el mes de: {meses(i)} la cantidad de zapatillas vendidas fue: {totVentas}\n")
    totVentasLista.append(totVentas)
        


#calculo de ventas por zapatillas
totCantZapLista = []
for i in range(len(matrizVentas)):  
    num2 = 0
    for j in range(len(matrizVentas[i])):
        num = matrizVentas [j] [i]
        num2 += num
    totCantZapLista.append(num2) 

        
        
print ("\na)")
for i in range(len(totCantZapLista)):
    if i in totCantZapLista == 0:
        print (f"El modelo {zapatos(i)}, se encuenra sin stock.")
    else:
        print (f"En el modelo {zapatos(i)}, hay un stock de: {30-totCantZapLista[i]} zapatos.")


print ("\nb)")
minZap = 30
for x in totCantZapLista:
    if x < minZap:
        minZap = x

for j in range(len(totCantZapLista)):
    if totCantZapLista[j] == minZap:
        print (f"La zapatilla menos vendida fue la {zapatos(j)}\n "
               f"con un total de: {minZap} zapatillas vendidas.")


print ("\nc)")
for j in range(len(totVentasLista)):
    if totVentasLista[j] == max_ventas_mensual(totVentasLista):
        print (f"En el mes de {meses(j)}, se vendieron mas zapatillas, "
               f"con un total de: {max_ventas_mensual(totVentasLista)} zapatillas.")

print ("\nd)")
listaNum = []
for i in range(len(matrizVentas)):
    for j in range(len(matrizVentas[i])):
        num = matrizVentas[i][2]
    listaNum.append(num)
    print (f"En el mes de {meses(i)} se vendieron {listaNum[i]} zapatillas del modelo 3.")

print ("\ne)")
print (f"El total de zapatos vendidos en los 6 meses es de: {sum(totCantZapLista)} zapatos.")

