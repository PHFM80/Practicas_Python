#Ingreso de datos
print('''Los tipos de hamburguesas son:
      S _ Simple
      D _ Doble
      T _ Triple''')

tipoHamb = input('Ingrese el tipo de hamburguesa: ').upper()
cantHamb = int(input("Ingrese la cantidad de hamburguesas que desea llevar: "))
print('''Tipo de pago:
      E _ Efectivo
      T _ Tarjeta decredito (con recargo)''')
tipoPago = input("Seleccione el tipo de pago: ").upper()
print ("- -  - - -  - -")
#Asignacion de variables
if tipoPago == "E":
    medioPago = "Efectivo"
elif tipoPago == "T":
    medioPago = "Tarjeta"

if tipoHamb == "S":
   hamburguesa = "simple"
   valorHamb = int(20)
elif tipoHamb == "D":
    hamburguesa = "doble"
    valorHamb = int(25)
elif tipoHamb == "T":
    hamburguesa = "triple"
    valorHamb = int(28)

#logica del programa
if tipoPago == "E":
    if tipoHamb == "S":
        precio = cantHamb * valorHamb
    elif tipoHamb == "D":
        precio = cantHamb * valorHamb
    elif tipoHamb == "T":
        precio = cantHamb * valorHamb

elif tipoPago == "T":
    if tipoHamb == "S":
        precio = (cantHamb * valorHamb) * 1.05
    elif tipoHamb == "D":
        precio = (cantHamb * valorHamb) * 1.05
    elif tipoHamb == "T":
        precio = (cantHamb * valorHamb) * 1.05

print (f'''El tipo de hamburguesa que selecciono es: "{hamburguesa}"
El valor de la misma es de: ${valorHamb}
La cantidad de hamburguesas que va a llevar es de: "{cantHamb}"
El medio de pago seleccionado es: "{medioPago}"
El total a pagar por el pedido es: ${precio} ''')


