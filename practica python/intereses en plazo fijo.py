cont = 0
print ("Calcularemos la tasa de interes mensual y la tasa Nominal anual.  "
       "Para eso deberemos ingresar los siguientes datos.")
tna = float(input("Ingrese la Tasa de Interes Anual (TNA): "))
cantMes = int(input("Ingrese la cantida de mese que va a establecer el plazo fijo: "))
monto = int(input("Ingrese la suma de dinero a depositar: "))

#tnm es la tasa nominal mensual.  se calcula dividiendo la TNA en 12 meses
tnm = (tna/12)/100

for i in range(0, cantMes+1):
    print(". . . . . . . . . . . .")
    print(f"Para el mes {i}, el capital es ${round(monto, 2)}")
    print(f"La tasa nominal mensual es de: ${round(tnm, 4)}")
    interes = monto * tnm
    monto = monto + interes
    print(f"Los intereses del mes son de: ${round(interes, 2)}")
    print(f"El monto a retirar es de: ${round(monto, 2)}")
    print(". . . . . . . . . . . .")

print(f"El monto final es de ${round(monto, 2)}")
