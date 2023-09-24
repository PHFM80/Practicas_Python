class coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self):
        self.enMarcha = True
    def estado(self):
        if self.enMarcha == True:
            return "El coche esta en marcha"
        else:
            return "El coche NO esta en marcha"

print ("- - - - INSTANCIANDO UN 1er COCHE - - - - ")

miCoche = coche()

print (miCoche.estado())
print (f"El estade de enMarcha es: {miCoche.enMarcha}")
print (f"El alrgo del coche es: {miCoche.largoChasis} cm.")
print (f"Mi coche tiene {miCoche.ruedas} ruedas.")
miCoche.arrancar()
print (miCoche.estado())
print (f"El estade de enMarcha es: {miCoche.enMarcha}")

print ("- - - - INSTANCIANDO UN 2do COCHE - - - - ")

miCoche2 = coche()

miCoche2.ruedas = 3
print (miCoche2.estado())
print (f"El estade de enMarcha es: {miCoche2.enMarcha}")
print (f"El largo del coche es: {miCoche2.largoChasis} cm.")
print (f"Mi coche tiene {miCoche2.ruedas} ruedas.")

print (miCoche2.estado())
print (f"El estado de enMarcha es: {miCoche2.enMarcha}")

print ("- - - - INSTANCIANDO UN 3er COCHE - - - - ")

miCoche3 = coche()

print (miCoche3.estado())
print (f"El estade de enMarcha es: {miCoche3.enMarcha}")
print (f"El largo del coche es: {miCoche3.largoChasis} cm.")
print (f"Mi coche tiene {miCoche3.ruedas} ruedas.")
miCoche3.arrancar()
print (miCoche3.estado())
print (f"El estado de enMarcha es: {miCoche3.enMarcha}")
