imp = int (input ("Ingrese el importe de la compra: "))

if imp >= 5000:
    total = imp * 0.82
elif imp >= 1000 and imp < 5000:
    total = imp * 0.9
else: total = imp

print ("El importe de la compra es: ", total)