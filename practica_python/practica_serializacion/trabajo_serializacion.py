import pickle

lista_nombres = ["pedro", "Ana", "miguel", "Isabel", "Mariana"]
lista_apelidos = ["gomez", "gutierrez", "cocola", "Allende", "Flores"]
lista_edad = [ 20, 44, 70, 90, 25]
datos_completos = []
for i in range(len(lista_nombres)):
    lista_pasajera =[]
    nombre = lista_nombres[i]
    lista_pasajera.append(nombre)
    apellido = lista_apelidos[i]
    lista_pasajera.append(apellido)
    edad = lista_edad[i]
    lista_pasajera.append(edad)
    datos_completos.append(lista_pasajera)

print (f"esta es la lista recien armada:\n {datos_completos}")


fichero_binario = open("E:\Desarrollo_de_sofware\Practicas_Python\practica_python\practica_serializacion\external_files\lista_de_datos", "wb")
pickle.dump(datos_completos, fichero_binario)
fichero_binario.close()

fichero = open("E:\Desarrollo_de_sofware\Practicas_Python\practica_python\practica_serializacion\external_files\lista_de_datos", "rb")
lista = pickle.load(fichero)
fichero.close()

print (f"esta es la lista desarmada:\n {lista}")
lista_nombres_1 = []
lista_apelidos_1 = []
lista_edades_1 = []
for i in lista:
    for j in range(len(i)):
        pass
                   
        
