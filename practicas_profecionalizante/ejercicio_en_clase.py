from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf 
from random import uniform
from os import system
# nro = int (input("Ingrese un numero por teclado y el programa determinara si es par o impar.\n"))

# if  nro % 2 == 0:
#     print ("el numero es par.")
# else:
#     print ("el numero es impar")


# print ("imagine que ha pagado en el supermercado una comprar\n"
#         "haga un programa que calculeel precio final.\n"
#         "1_ si paga de contado tendra un 10% de descuento.\n"
#         "2_ si paga con debito manteine el precio.\n"
#         "3_ si paga con tarjeta de credito tiene un 10 % de recargo.\n")
# valorCompra = int (input("Ingrese el monto de la compra.\n"))

# opc = int (input("determine la forma de pago:\n"
#                 "1_ si va a pagar en efectivo.\n"
#                 "2_ si va a pagar con tarjeta de debito.\n"
#                 "3_ si va a pagar con tarjeta de credito.\n"))

# if opc == 1:
#     print (f"\nEl monto total a pagar es: ${valorCompra * 0.9}")
# elif opc == 2:
#     print (f"\nEl monto total a pagar es: ${valorCompra}")
# elif opc == 3:
#      print (f"\nEl monto total a pagar es: ${valorCompra * 1.1}")


# precio_entrada = 3000


# while True:
#     try:
#         print("Opciones de descuento:\n"
#             "1. Egresado de la UNCuyo\n"
#             "2. Docente de la UNCuyo\n"
#             "3. Alumno de la UNCuyo\n"
#             "4. Jubilado de la UNCuyo\n"
#             "5. Persona discapacitada\n"
#             "6. No soy parte de la UNCuyo\n"
#             "7. Salir del programa\n")

#         opcion = int(input("Ingrese el número de la opción correspondiente: "))

#         if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
#             precio_entrada *= 0.5
#         elif opcion == 5:
#             precio_entrada = 0
#         elif opcion == 6:
#             precio_entrada   
#         elif opcion == 7:
#             salir_dyt_by_pf() 
#         else:
#             print("Opción incorrecta. No se aplica descuento.")

#         print(f"El precio de entrada es: {precio_entrada}")
#     except ValueError:
#         print ("ingreso una letra.\nDebe ingresar solo numeros")

# 
system("cls")
nro = float(uniform(0, 9))

print (f"El terremoto registrado en la escala de ritcher es: {round(nro, 1)}\n")
if nro < 4:
    print ("Sin Daños\n")
elif nro >=4 and nro <=5.9:
    print ("Daños a edificios mal cosntruidos.\n")
elif nro >=6 and nro <=6.9:
    print ("Muchos edificios dañados, algunos colapsados.\n")
elif nro >=7 and nro <=7.9:
    print ("Muchos edificios destruidos.\n")
elif nro >= 8:
    print ("Mayoria de las estrucuras caen.\n")

