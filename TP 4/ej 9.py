#ingreso de datos
print ("Los tipos de servicios son:\nA) Basico\nB) Intermedio\nC) VIP")
tipoBus = input("Ingrese el tipo de servicio: ").upper()
cantPers = int(input("Ingrese la cantidad de personas: "))
kmRec = int(input("Ingrese los kilometros a recorrer: "))

#Asignacion de valores
valorBusA = int(2)
ValorBusB = int(3)
valorBusC = int(4)

if tipoBus == "A":
    servicio = "Servicio Básico"
elif tipoBus == "B":
    servicio = "Servicio Intermedio"
elif tipoBus == "C":
    servicio = "Servicio VIP"

#logica del programa
if tipoBus == "A" and cantPers < 20:
    valorViaje = kmRec * valorBusA * 20
    valorPers = round(valorViaje / cantPers, 2)
elif tipoBus == "A" and cantPers >= 20:
    valorViaje = kmRec * valorBusA * cantPers
    valorPers = round(valorViaje / cantPers, 2)
if tipoBus == "B" and cantPers < 20:
    valorViaje = kmRec * ValorBusB * 20
    valorPers = round(valorViaje / cantPers, 2)
elif tipoBus == "B" and cantPers >= 20:
    valorViaje = kmRec * ValorBusB * cantPers
    valorPers = round(valorViaje / cantPers, 2)
if tipoBus == "C" and cantPers < 20:
    valorViaje = kmRec * valorBusC * 20
    valorPers = round(valorViaje / cantPers, 2)
elif tipoBus == "C" and cantPers >= 20:
    valorViaje = kmRec * valorBusC * cantPers
    valorPers = round(valorViaje / cantPers, 2)

print (f'''Elservicio seleccionado es: {servicio}
El valor del servicio es: ${valorViaje}
El valor del viaje por persona es: ${valorPers}''')