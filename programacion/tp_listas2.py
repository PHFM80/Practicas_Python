from random import randint

#Problema 1:
print ("Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga"
" por teclado de todos los datos imprimir los datos de las personas mayores de edad (mayores o iguales a 18 años)\n")
nombres = []
edades = []

for i in range(5):
    nombre = input (f"Ingrese el nombre de la {i+1} persona: \n")
    nombres.append(nombre)
    edad = input (f"Ingrese la edad de la {i+1} persona: \n")
    edades.append(edad)
for i in range(5):
    print (f"El nombnre de la {i+1} persona es: {nombres[i]}.  Y su edad es: {edades[i]}.\n")
for nombre, edad in zip (nombres, edades):
    print (f"El nombre de la persona es: {nombre}.  Y su edad es: {edad}.\n")

#Problema 2:
print ("Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar"
"una tercer lista que surja de la suma de los elementos de la misma posición de cada lista.  Mostrar esta tercer lista.")
lista1 = []
lista2 = []
rango = int (input ("Ingrese la cantidad de numeros a ingresar a la lista: \n"))
for i in range (rango):     #llenado de las listas en forma automatica
    nro1 = randint (0, 20)
    nro2 = randint (0, 20)
    lista1.append(nro1)
    lista2.append(nro2)
suma = []
for i in range (rango):     #Recorrida de las listas y sumado de las mismas
    nro_sum = lista1[i] + lista2[i]
    suma.append(nro_sum)
suma2 = []
for nro1, nro2 in zip(lista1, lista2):
    nro_suma2 = nro1 + nro2
    suma2.append(nro_suma2)
print (f"lista1: {lista1}")
print (f"lista2: {lista2}")
print (f"suma1: {suma}")
print (f"suma2: {suma2}")

#problema 3
print ("En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:\n"
"a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)\n"
"b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar Muy Bueno si la nota"
" es mayor o igual a 8, Bueno si la nota está entre 4 y 7, y colocar Insuficiente si la nota es inferior a 4.\n"
"c) Imprimir cuantos alumnos tienen la leyenda “MuyBueno”.\n")
nombres_alumnos = []
notas_alumnos = []
rango3 = int (input("Ingrese la cantidad de alumnos del curso:\n"))
for i in range(rango3):
    nombre = input (f"Ingrese el nombre de la {i+1} persona: \n")
    nombres_alumnos.append(nombre)
    nota = randint(1, 10)
    notas_alumnos.append(nota)
al_mb = 0
for i in range(rango3):
    condicion = "Insuficiente"
    if notas_alumnos[i]>= 8:
        condicion = "Muy Bueno"
        al_mb += 1
    elif notas_alumnos[i]>=4 and notas_alumnos[i] <= 7:
        condicion = "Bueno"
    print (f"pos {i+1}) Nombre: {nombres_alumnos[i]}; notas: {notas_alumnos[i]}; condicion: {condicion}.\n")
print (f"La cantidad de alumos en la condicin Muy Buenos es de: {al_mb}")

#ejercicio 4 - tirada de dados
print ("Ejercicio 1.- Escriba un programa que permita generar el lanzamiento de dos dados, diez veces, si la suma de los dos da 7, se "
"muestra un mensaje de: “GANASTE”, y cuente la cantidad de veces que ganaste, utilice la generación de números aleatorios")

# Inicializar el contador de victorias
victorias = 0

# Realizar 10 lanzamientos de dados
for _ in range(10):
    # Generar dos números aleatorios entre 1 y 6 para simular el lanzamiento de dos dados
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    # Calcular la suma de los resultados de los dos dados
    suma = dado1 + dado2

    # Mostrar los resultados del lanzamiento de los dados
    print(f"Lanzamiento: Dado 1: {dado1}, Dado 2: {dado2}, Suma: {suma}")

    # Verificar si la suma es igual a 7
    if suma == 7:
        print("GANASTE")
        victorias += 1

# Mostrar el total de victorias
print(f"Total de veces que ganaste: {victorias}")


#Ejercicio 5 - Adivina el numero
print ("La computadora pensará un número aleatorio entre 1 y 10, y te pedirá que intentes adivinarlo. La computadora te dirá si "
"cada intento es muy alto o muy bajo. Tú ganas si adivinas el número en 4 (cuatro) intentos o menos.\n Este es un buen juego para "
"codificar ya que usa números aleatorios y bucles, y recibe entradas del usuario en un programa corto. Aprenderás cómo convertir "
"valores a diferentes tipos de datos, y por qué es necesario hacer esto.\nDado que este programa es un juego, nos referiremos al"
"usuario como el jugador. Pero llamarlo “usuario” también sería correcto.")

# Pedir el nombre del jugador
nombre_jugador = input("¡Hola! Por favor, introduce tu nombre: ")

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = randint(1, 10)

print(f"Hola, {nombre_jugador} ¡Estoy pensando en un número entre 1 y 10! Tienes 4 intentos para adivinarlo.")

# Iniciar el bucle para los intentos
intentos = 0
while intentos < 4:
    intento = int(input("Introduce el número:\n "))
    intentos += 1

    if intento == numero_aleatorio:
        print(f"¡Felicidades, {nombre_jugador}! ¡Has adivinado el número {numero_aleatorio} en {intentos} intentos!")
        break
    elif intento < numero_aleatorio:
        print("El número es más alto. ¡Sigue intentando!")
    else:
        print("El número es más bajo. ¡Sigue intentando!")

# Si el jugador no adivina en 4 intentos
if intentos == 4:
    print(f"Lo siento, {nombre_jugador}. El número que estaba pensando era {numero_aleatorio}. ¡Mejor suerte la próxima vez!")

#Ejercicio 6 - Verificar Contraseña
#    Crear un programa de validación de contraseñas, este debe cumplir con los siguientes requisitos:
#  La contraseña debe contener mínimo 10 caracteres
#  Debe contener al menos; minúscula, mayúscula y números
#  No puede haber espacios en blancos en la contraseña
#  Si cumple con todos estos requisitos debe retornar el mensaje, 
# “La Contraseña es segura”
#    Datos de entrada
#  Contraseña
#    Proceso
#  Validación de la longitud 
#  Comprobación de mayúsculas y minúsculas
#  Comprobación de números y espacios
#    Datos de salida
#  Si no cumple requisitos imprimir errores y el mensaje
# “La contraseña no es segura”
#  Si cumple requisitos imprimir mensaje de “La contraseña es segura”


while True:
    opc = int (input("Ingrese una opcion:\n1. Para contnuar.\n Cualquier otro numero para salir."))
    if opc == 1:
        print ("Ingrese una contraseña y el programa le indicara si es segura o no.")

        contr = input ("Ingrese una contraseña segura: \n")

        if len(contr) < 10:
            print ("La contraseña debe tener 10 caracterres o mas. \nContraseña Insegura.\n")
        elif not any ([c.isdigit() for c in contr]):
            print ("La contraseña debe tener al menos un número.\n Contraseña Insegura")
        elif not any ([c.islower() for c in contr]):
            print ("La contraseña debe tener letras minusculas.\n Contraseña Insegura")
        elif not any ([c.isupper() for c in contr]):
            print ("La contraseña debe tener letras mayusculas.\n Contraseña Insegura")
        elif (contr.count(" ")>0):
            print ("La contraseña no debe tener espacios.\n Contraseña Insegura")
        else:
            print ("La contraseña es Segura")
    else:
        print ("Saliendo del programa")
        break



