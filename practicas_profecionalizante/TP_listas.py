# Tp Listas
print ("Operaciones con listas.\n 1- Crear una lista llamada amigos con un mínimo de 5 amigos"
       "2- Crear una lista con las edades de tus amigos\n"
        "3- Añadir un compañero de este curso a esa lista amigos \n"
        "4- Insertar 3 amigos más del trabajo a la lista, uno al comienzo, otro al final y otro en el medio\n"
        "5- Buscar el amigo más grande de tu lista (buscar por nombre) y reemplazarlo por la rectora del IES.\n"
        "6- Borrar un amigo.\n"
        "7- Crear una lista vacía y completarla por teclado con los nombres de las personas que viste"
         "el día de hoy\n")

def agregra_nombre_edad():
    nom = input ("Ingrese el nombre del amigo:\n").capitalize()
    edad = int (input ("Ingrese la edad de su amigo:\n"))
    return nom, edad

# 1 agregando la cantidad de amigos a lista
# 2 agregando la edad de los amigos a la lista 
# # codigo para agragar a los amigos uno por uno con sus edades     
# # print ("\nIgrese 5 amigos ocn sus edades.\n")
# # amigos = []
# # edades = []
# # for i in range(5):
# #     nom, edad = agregra_nombre_edad()
# #     amigos.append(nom)
# #     edades.append(edad)

# # print (amigos)
# # print (edades)
# Forma con la lista ya creada
amigos = ["Maraino", "Marcelo", "Marcos", "Maria", "Marianela"]
edades = []

# Agregando edades
for i in range(len(amigos)):
    edad = int (input("Ingrese la edad del primer amigo:\n"))
    edades.append(edad)


# 3 añadiendo un amigo de este curso a la lista
print ("\nAñada un amigo de este curso.\n")
nom, edad = agregra_nombre_edad()
amigos.append(nom)
edades.append(edad)

print (amigos)
print (edades)

# 4 ingresando ammigos al comienzo al final y al medio de la lista
print ("\nIngresando un amigo al principio de la lista")
nom, edad = agregra_nombre_edad()
amigos.insert(0, nom)
edades.insert(0, edad)

print ("\nIngresando un amigo al final de la lista")
nom, edad = agregra_nombre_edad()
amigos.append(nom)
edades.append(edad)

print ("\nIngresando un amigo al medio de la lista")
mitad = len(amigos)//2
nom, edad = agregra_nombre_edad()
amigos.insert(mitad, nom)
edades.insert(mitad, edad)


print (amigos)
print (edades)

# 5 Buscar el amigo más grande de tu lista (buscar por nombre) y reemplazarlo por la rectora del IES.\n"
print ("Se buscara al amigo más grande de tu lista (buscar por nombre) y sera reemplazado por la rectora del IES.\n")
for i in range(len(amigos)):
    print (f"{i}) {amigos[i]}, {edades[i]}")
nom2 = input ("Seleccione el nombre del amigo a reemplazar:\n").capitalize()
pos = amigos.index (nom2)
amigos.pop(pos)
edades.pop(pos)
amigos.insert (pos, "Rectora IES")
edades.insert (pos, 00)

print (amigos)
print (edades)

# 6 Borrar un amigo de la lista
for i in range(len(amigos)):
    print (f"{i}) {amigos[i]}, {edades[i]}")
nom2 = input ("seleccione un amigo de la lista, para eliminarlo:\n").capitalize()
pos = amigos.index (nom2)
amigos.pop(pos)
edades.pop(pos)

print (amigos)
print (edades)

# 7- Crear una lista vacía y completarla por teclado con los nombres de las personas que viste el día de hoy
amigosHoy = []
print ("crearemos un a lista con los amigos que viste hoy.\nPresiona enter cuando termines.\n")
while True:
    nom3 = input("Ingrese el nombre de un amigo:\n")
    if nom3 == "":
        break
    else:
        amigosHoy.append(nom3)
print (amigosHoy)



# Crear una lista llamada sistemasoperativos y guardar en ella 5 elementos que
# Imprima toda la lista.
# Ahora imprima solo el primer y ultimo elemento de la lista
sistemasoperativos =["Android", "IOS", "Mac", "Linux", "Windows"]

print (sistemasoperativos)
print (f"La lista de sistemas operaticvos es: {sistemasoperativos}")
for i in range (len(sistemasoperativos)):
    print (f"El {i+1}° sistema es: {sistemasoperativos[i]}\n")

print ("Imprimiendo el 1er y ultimo sistema opeativo.\n")
print (f"El 1er sistema operativo es: {sistemasoperativos[0]}\n")
print (f"El ultimo sistema operativo es: {sistemasoperativos[len(sistemasoperativos)-1]}\n")


# Crear una lista relacionada a la tecnologia, guardar en ella 7 elementos que sean
#diferentes tipos de datos (str, int, int, str, float,str, float) y caractericen a esta lista.
#Imprimir los valores guardados.
# Ahora modificar el segundo elemento
# Elimina el 4to elemento

tecnologia = ["Memoria RAM", 256, 1028, "Windows", 25.25, "PC",52.52]

print (tecnologia)
print (f"La lista de sistemas operaticvos es: {tecnologia}")
for i in range (len(tecnologia)):
    print (f"El {i+1}° elemento es: {tecnologia[i]}.  Y su tipo es: {type(tecnologia[i])}")
print ("")

tecnologia.pop(1)
tecnologia.append(512)
for i in range (len(tecnologia)):
    print (f"El {i+1}° elemento es: {tecnologia[i]}.  Y su tipo es: {type(tecnologia[i])}")
print ("")

tecnologia.pop(3)
for i in range (len(tecnologia)):
    print (f"El {i+1}° elemento es: {tecnologia[i]}.  Y su tipo es: {type(tecnologia[i])}")
print ("")

# DESAFIO
# Crear un programa que lea por teclado números y los guarde en una lista,
# el programa pedirá tantos números como se le desee dar, el proceso finaliza cuando el usuario ingresa un 0.
# Al finalizar mostrar el máximo número introducido, el mínimo y la longitud de la lista.

print ("Ingrese numeros por teclado, se podra detener el ingreso de numeros al ingresar el ´0´.")
listaNum = []
while True:
    num = int(input("Ingrese un numero:\t "))
    if num == 0: break
    else: listaNum.append(num)
print (f"El número maximo de la lista es: {max(listaNum)}.\n"
       f"El número mínimo de la lista es: {min(listaNum)}.\n"
       f"El largo de la lista es: {len(listaNum)}.\n")







