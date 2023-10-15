from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf
from random import randint, uniform

# print ("Ejercicio 1\n"
#     "Una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática\n"
#      "el precio que debe cobrar a sus clientes por entrar.\n El programa debe preguntar al usuario:"
#       "la edad del cliente y mostrar el precio de la entrada.\n"
#        "Si el cliente es menor de 5 años puede entrar gratis, si tiene entre 5 y 18 años debe pagar\n"
#         "el 50% de la entrada y si es mayor de 18 años, entrada normal de 5000\n")

# valorEntrada = int (5000)

# while True:
#     try:
#         edad = int (input("Ingrese su edad:\n"))

#         if edad > 1 and edad < 5:
#             print (f"El valor de la entrada es: ${valorEntrada}.\n"
#                 "Usted puede ingresar gratis.\n")
#         elif edad >=5 and edad <= 18:
#             print (f"El valor de la entrada es: ${valorEntrada}.\n"
#                     f"Usted debe pagar: ${valorEntrada*0.5}.\n")
#         elif edad >18:
#             print (f"El valor de la entrada es: ${valorEntrada}.\n"
#                     f"Usted debe pagar: ${valorEntrada}.\n")
#         elif edad == 0:
#             salir_dyt_by_pf()
#     except ValueError:
#         salir_dyt_by_pf()


#ejercicio 2
# def dia_de_la_semana(dia):
#     if dia == 1:
#         dia2 = "lunes"
#     elif dia == 2:
#         dia2 = "martes"
#     elif dia == 3:
#         dia2 = "miercoles"
#     elif dia == 4:
#         dia2 = "jueves"
#     elif dia == 5:
#         dia2 = "viernes"
#     elif dia == 6:
#         dia2 = "sábado"
#     elif dia == 7:
#         dia2 = "domingo"
#     return (print (f"Hoy es {dia2}"))

# print ("Ejercicio 2\n"
#     "Imagine que ha realizado una compra en un supermercado. Ahora un programa calculará el precio final\n"
#     " Si paga al Contado tendrá 10% de descuento2\n"
#     " Si paga con Débito: Visa o Maestro se mantiene el precio2\n"
#     " Si paga con Crédito: Visa o Mastercard colocaré un aumento del 10%\n"
#     "Además los días miércoles existe un descuento adicional si se paga con tarjeta debito Maestro del 15 %\n")


# while True:
#     dia = int (randint(1,7))
    
#     dia_de_la_semana (dia)
#     opc = int (input("determine la forma de pago:\n"
#                     "1_ si va a pagar en efectivo.\n"
#                     "2_ si va a pagar con tarjeta de debito.\n"
#                     "3_ si va a pagar con tarjeta de credito.\n"
#                     "4_ para detener la ejecucion del programa.\n"))
    
#     valorCompra = int (input("Ingrese el monto de la compra.\n"))

#     montoFinal = 0
#     if opc == 1:
#         montoFinal = valorCompra * 0.9
#         print (f"\nEl monto total a pagar es: ${montoFinal}\n")
#     elif opc == 2:
#         montoFinal = valorCompra 
#         print (f"\nEl monto total a pagar es: ${montoFinal}\n")
#         if dia == 3:
#             print ("¡¡¡Hoy es Miercoles!!!\n"
#                 "Tiene un descuento especial por pagar con debito.\n")
#             montoFinal = valorCompra *0.85
#             print (f"\nEl monto total a pagar es: ${montoFinal}\n")
#     elif opc == 3:
#         montoFinal = valorCompra * 1.1
#         print (f"\nEl monto total a pagar es: ${montoFinal}\n")

#     elif opc == 4:
#         salir_dyt_by_pf()
        
# print ("Ejercicio 3\n"
#     "Una pizzería ofrece pizzas vegetarianas además de las comunes. El usuario deberá seleccionar una de las siguientes opciones\n"
#     "Pizza I = jamón, queso y pimientos\n"
#     "Pizza II = pimiento, queso y aceitunas\n"
#     "Pizza III = jamón, queso y ananá\n"
#     "Piza IV = espárragos, queso y tomate\n"
#     "En función de su respuesta muestre un menú con las opciones disponibles para que elija. Al final se debe mostrar"
#     "por pantalla la pizza elegida y si es vegetariana o no y todos los ingredientes que lleva. \n")

# while True:
#     opc = input("Seleccione el tipo de pizza:\n"
#                 "I_ para Pizza I\n"
#                 "II_ para Pizza II\n"
#                 "III_ para Pizza III\n"
#                 "IV_ para Pizza IV\n"
#                 "V_ para salir\n").upper()
#     if opc == "I":
#         print ("\nEsta pizza contiene: jamón, queso, pimientos.\n"
#                "NO es vegetariana.\n")
#     elif opc == "II":
#         print ("\nEsta pizza contiene: pimientos, queso y aceitunas.\n"
#                "¡¡Es vegetariana!!\n")
#     elif opc == "III":
#         print ("\nEsta pizza contiene: jamón, queso y anana.\n"
#                "NO es vegetariana.\n")
#     elif opc == "IV":
#         print ("\nEsta pizza contiene: esparragos, queso tomates.\n"
#                "¡¡Es vegetariana!!\n")
#     elif opc == "V":
#         salir_dyt_by_pf()  
#     else:
#         print ("Ingrese una opcion valida")

# print ("Ejercicio 4.\n"
#     "La escala de Richter es una medida de la fuerza de un terremoto. Cada paso en la escala,\n"
#     "significa un aumento de diez veces en la fuerza de un terremoto. La siguiente tabla describe los\n"
#     "efectos de terremotos de diferentes magnitudes en la escala de Richter. Usar función random para obtener una magnitud aleatoria\n")


# nro = round(float(uniform(0, 9)), 1)

# print (f"La magnitud del terremoto registrado en la escala de ritcher es: {nro}\n")
# if nro < 4:
#     print ("Sin Daños\n")
# elif nro >=4 and nro <=5.9:
#     print ("Daños a edificios mal cosntruidos.\n")
# elif nro >=6 and nro <=6.9:
#     print ("Muchos edificios dañados, algunos colapsados.\n")
# elif nro >=7 and nro <=7.9:
#     print ("Muchos edificios destruidos.\n")
# elif nro >= 8:
#     print ("Mayoria de las estrucuras caen.\n")


print ("DESAFÍO\n"
"En un país se utilizan diferentes tasas impositivas según el sueldo bruto anual del contribuyente.\n"
"Los contribuyentes casados suman sus ingresos y pagan impuestos sobre el total.\n"
"La siguiente tabla muestra los cálculos de la tasa de impuestos\n"
"Categoría Sueldo Bruto anual Tasa Impositiva\n"
"A Menor o igual a 300000 3%\n"
"B Entre 300000 y 450000 8%\n"
"C Entre 450000 y 700000 13%\n"
"D Entre 700000 y 1200000 20%\n"
"E Más de 1200000 35%\n"
"a. Diseñe un programa que calcule el impuesto a pagar teniendo en cuenta las siguientes entradas: soltero/a o\n"
"casado/a, si es casado/a debe indicar dos sueldos, si es soltero/a uno. El código debe indicar en cual categoría\n"
"esta el contribuyente, el impuesto que deberá pagar y cuál es el sueldo mensual. Analícelo detenidamente, hay varias\n"
"formas de resolverlo, puede llegar a resolverlo con 30 líneas de código. Recuerde que la solución además de\n"
"contener poco código debe ser también también apreciable \n")          


def tasa_impositiva(s_total):
    if s_total <= 300000:
        impuesto = s_total * 0.03
    elif s_total > 300000 and s_total <= 450000:
        impuesto = s_total * 0.08
    elif s_total > 450000 and s_total <=700000:
        impuesto = s_total * 0.13
    elif s_total > 700000 and s_total <=1200000:
        impuesto = s_total * 0.2
    elif s_total > 1200000:
        impuesto = s_total * 0.35
    return (print(f"El impuesto total que debe pagar es de: ${round(impuesto,2)}"))

opc = input("¿Usted es casado? si/no.\n").upper()
if opc == "SI":
    sueldo1 = int(input("Ingrese el monto de su sueldo mensual:\n"))
    sueldo2 = int(input("Ingrese el monto del sueldo mensual de su esposo/a:\n"))
    s_total = sueldo1 * 12 + sueldo2 * 12
    tasa_impositiva(s_total)
elif opc == "NO":
    sueldo1 = int(input("Ingrese el monto de su sueldo mensual :\n"))
    s_total = sueldo1 * 12
    tasa_impositiva(s_total)
else:
    print ("Ingrese una opcion valida.\n")
