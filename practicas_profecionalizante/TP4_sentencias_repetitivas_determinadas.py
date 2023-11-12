#TP Nro 4: Sentencias Repetitivas Determinadas
from random import randint
#1) Dada la siguiente lista de lenguajes, deberá obtener la siguiente salida
lenguajes = ["Python", "C", "Java", "Javascript", "Kotlin"]
# El 1° lenguaje que aprendi fue Python
# El 2° lenguaje que aprendi fue C
# El 3° lenguaje que aprendi fue Java
# El 4° lenguaje que aprendi fue Javascript
# El 5° lenguaje que aprendi fue Kothlin
for i in range (len(lenguajes)):
    print (f"El {i+1}° lenguaje que aprendi es: {lenguajes[i]}.")
print ("")

#2) Crear una lista que contenga las edades de sus compañeros y calcule la edad promedio del curso
edades = [21,18,23,33,42,20,18,23,22,29]
print (f"La lista de edades es: {edades}")
print (f"La edad promedio de las edades es: {sum(edades)/len(edades)}")


# 3) Deberá crear una lista con los impuestos que pagó este último mes. Ahora imagine que usted cuenta 
# actualmente con $10000. ¿Cuántos impuestos alcanza a pagar y cuanto es la suma total que deberá pagar?
# Tenga en cuenta todas las posibilidades, si el monto le alcanza para pagar todo, algunos impuestos o solo uno, etc
sueldo = 10000
impuestos =  []
valorImpuestos = []
while True:
    tipoImp = input("Ingrese el tipo de impuesto: \n")

    if tipoImp == "":
        break
    else:
        valor = int (input("Ingrese el monto del impuesto: \n"))
        impuestos.append(tipoImp)
        valorImpuestos.append(valor)

for i in range(len(valorImpuestos)):
    print (f"El {i+1}° impuesto es: {impuestos[i]}; y su monto es de: ${valorImpuestos[i]}")

impPagado = []
impNoPagado = []
montoNoPagado = []
nuevoSaldo = 0
montoPagado = 0
for i in range(len(impuestos)):
    if valorImpuestos[i] <= sueldo:
        impPagado.append(impuestos[i])
        montoPagado += valorImpuestos[i]
        sueldo = sueldo - valorImpuestos[i]
        nuevoSaldo = sueldo
    elif valorImpuestos[i] > sueldo:
        impNoPagado.append(impuestos[i])
        montoNoPagado.append(valorImpuestos[i])

for i in impPagado:
    print (f"Impuesto pagado: {i}")

for i in range(len(impNoPagado)):
    print (f"Impuesto ´NO´ pagado: {impNoPagado[i]}, saldo: {montoNoPagado[i]}")
    
print (f"El total de impuestos pagados es: ${montoPagado}")
print (f"El saldo de su dinero es: ${nuevoSaldo}")


#4) Crear un rango del 1 al 10, luego imprimir solo los valores pares del rango
num1 = int (input("Ingrese el primer numero de la lista: \t"))
num2 = int (input("Ingrese el segundo numero de la lista: \t"))
lista=(list(range(num1, num2)))
print (lista)
for i in range(len(lista)) :
    if lista[i] % 2 == 0 :
        print (lista[i])

#5) Teniendo en cuenta los meses del año, en el primer mes el gasto en internet fue de 4000, pero el mismo 
#aumentó cada tres meses un 20%. ¿Cuánto pagó cada mes y cuanto pago en total en el abono de internet?
gastoInternet = 4000
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviemba", "Diciembre"]
#print (f"En el mes de {meses[0]} el costo de internet fue de: ${gastoInternet}")
gastoTotal = 0
cont = 0
for i in range(len(meses)):
    cont += 1
    if cont == 2:
        print (f"En el mes de {meses[i]}, el costo de internet fue de: ${gastoInternet}")
        gastoInternet = gastoInternet * 1.2
        gastoTotal = gastoTotal + gastoInternet
        cont = cont - 3
    elif cont < 2:
        gastoTotal = gastoTotal + gastoInternet
        print (f"En el mes de {meses[i]}, el costo de internet fue de: ${gastoInternet}")
print (f"El total abonado de internet fue de :{gastoTotal}")


#7) Ingresar un número entero positivo por teclado y calcular su factorial. El factorial de un número se 
#obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
num = int(input("Ingresar un número entero positivo por teclado y se calculara su factorial:\n"))

resultado = 1
for i in range(1, num + 1):
    resultado *= i

print(f"El factorial de {num} es: {resultado}")


#8) Desarrollar un programa que encuentre el número más chico, de varios números ingresados por teclado.
while True:
    num = int(input("Ingrese un numero: \n "))
    if num!=0:
        menor = num
        mayor = 0
        if num > mayor:
            mayor = num
        elif num < menor:
            menor = num
    elif num == 0:
        break
print (f"El mayor numero ingresado es: {mayor}\n"
       f"El menor numero ingresado es: {menor}\n")

#9) Ahora desarrolle un programa que pregunte al usuario si desea encontrar el número más grande o 
#el más chico de una serie de números ingresados por teclado

listaNumeros = []
while True:
    #num = int(input("Ingrese un numero distinto de 0.\nCuando ingrese 0 se terminara la ejecucion del programa de llenado.\n"))
    print ("Ingrese un numero distinto de 0.\nCuando ingrese 0 se terminara la ejecucion del programa de llenado.\n")
    num = randint(0,100) 
    if num != 0:
        listaNumeros.append(num)
    elif num == 0:
        break

print (listaNumeros)
listaNumeros.sort()
print (listaNumeros) 
print ("Si desea buscar el mayor de los numeros ingresados, presione M.\n"
       "Si desea buscar el menor de los numeros ingresados, presione m.\n")
opc = input("Ingrese una opcion:\n")
if opc == "M":
    print (f"El numero mas grande de la lista es: {listaNumeros[len(listaNumeros)-1]}")
elif opc == "m":
    print (f"El numero mas pequeño de la lista es: {listaNumeros[0]}")
else:
    print ("Opcion invalida.")



# DESAFÍO
# Dada una cantidad X de números seleccionada por el usuario. Se le pedirá al mismo introducir dichos números. Luego el programa debe:
# i) Verificar que el usuario no solicite introducir una cantidad X de números menor o igual a 0
# ii) Verificar que los números que ingrese el usuario no sean menores o iguales a 0
# iii) Mostrar el orden del número introducido (1er número a ingresar, “2do número a ingresar, etc)
# iv) Calcular la cantidad de números pares introducidos
# v) La sumatoria de números impares introducidos 

listaNumeros = []

while True:
    cantNum = int(input("Ingrese la cantidad de numeros que quiere agregar a la lista:\n"))
    contNum = 0
    contPares = 0
    sumImpares = 0
    if cantNum <= 0:
        print ("No puede ingresar una cantida gual o menor a 0")
    elif cantNum >= 1:
        while contNum < cantNum:
            num = int ( input("Ingrese un numero:\n"))
            if num <= 0:
                print ("No puede ingresar un numero igual o menor a 0\nSiga Intentando.\n")
            else:
                print (f"{contNum+1}° número a ingresar: {num}")
                if num % 2 == 0:
                    contPares += 1
                else:
                    sumImpares += num
                listaNumeros.append (num)
                contNum +=1
        break
print (f"La lista de numeros es: {listaNumeros}\n"
       f"La cantidad de números pares es: {contPares}\n"
       f"La suma de los números impares es: {sumImpares}\n")






