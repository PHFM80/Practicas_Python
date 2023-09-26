print ("El sueldo neto de un vendedor se calcula como la suma del sueldo básico de $100.000 más el 12% del monto total vendido.  \nCalcular y mostrar el sueldo neto de un vendedor conociendo el monto de las 3 ventas que hizo en el mes. ")

venta1= int(input("Ingrese el monto de la 1er venta: $"))
venta2= int(input("Ingrese el monto de la 2da venta: $"))
venta3= int(input("Ingrese el monto de la 3er venta: $"))

sueldoFijo = int(100000)
comision = (venta2 + venta3 + venta1) * 0.12

print (f"Sueldo fijo = ${sueldoFijo}")
print (f"Comision = ${comision}")
print ("- -  - - -  - -")
print (f"EL sueldo neto es: ${sueldoFijo + comision}")
