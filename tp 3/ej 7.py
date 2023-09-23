print ("un individuo desea invertir su capital en un banco, \n y desea saber cuanto dinero ganará despues de un mes, \n si el banco paga a razon de 7% mensual.")
print ("")
capital = int(input("Ingrese el capital a invertir: $"))
print ("- -  - - -  - -")
interes = capital * 0.07
gananciaFinal = interes + capital
print (f"La ganancia final es: ${gananciaFinal}")