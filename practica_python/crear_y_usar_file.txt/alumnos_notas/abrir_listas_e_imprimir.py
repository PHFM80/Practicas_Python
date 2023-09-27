

#def abrir_listas():
arch_id = open ("archivos_txt/id.txt", "r")
lista_id = arch_id.readlines()
arch_id.close()
lista_id_2 = []
for i in lista_id:
    i = i.replace("\n", "")
    lista_id_2.append(i)

arch_nombre1 = open ("archivos_txt/nombre1.txt", "r")
lista_nombre1 = arch_nombre1.readlines()
arch_nombre1.close()
lista_nombre1_2 = []
for i in lista_nombre1:
    i = i.replace("\n", "")
    lista_nombre1_2.append(i)

arch_nombre2 = open ("archivos_txt/nombre2.txt", "r")
lista_nombre2 = arch_nombre2.readlines()
arch_nombre2.close()
lista_nombre2_2 = []
for i in lista_nombre2:
    i = i.replace("\n", "")
    lista_nombre2_2.append(i)

arch_apellido1 = open ("archivos_txt/apellido1.txt", "r")
lista_apellido1 = arch_apellido1.readlines()
arch_apellido1.close()
lista_apellido1_2 = []
for i in lista_apellido1:
    i = i.replace("\n", "")
    lista_apellido1_2.append(i)

arch_apellido2 = open ("archivos_txt/apellido2.txt", "r")
lista_apellido2 = arch_apellido2.readlines()
arch_apellido2.close()
lista_apellido2_2 = []
for i in lista_apellido2:
    i = i.replace("\n", "")
    lista_apellido2_2.append(i)

arch_edad = open ("archivos_txt/edad.txt", "r")
lista_edad = arch_edad.readlines()
arch_edad.close()
lista_edad_2 = []
for i in lista_edad:
    i = i.replace("\n", "")
    lista_edad_2.append(i)

arch_dni = open ("archivos_txt/dni.txt", "r")
lista_dni = arch_dni.readlines()
arch_dni.close()
lista_dni_2 = []
for i in lista_dni:
    i = i.replace("\n", "")
    lista_dni_2.append(i)

arch_materia = open ("archivos_txt/materia.txt", "r")
lista_materia = arch_materia.readlines()
arch_materia.close()
lista_materia_2 = []
for i in lista_materia:
    i = i.replace("\n", "")
    lista_materia_2.append(i)

arch_notas = open ("archivos_txt/notas.txt", "r")
lista_notas = arch_notas.readlines()
arch_notas.close()
lista_notas_2 = []
for i in lista_notas:
    i = i.replace("\n", "")
    lista_notas_2.append(i)

def imprimir_un_alumno(pos): 
    print (f"\nid: {lista_id_2[pos]}  nombres: {lista_nombre1_2[pos]}{lista_nombre2_2[pos]} "
        f"\tapellidos: {lista_apellido1_2[pos]}{lista_apellido2_2[pos]}\n"
        f"\tEdad: {lista_edad_2[pos]} DNI: {lista_dni_2[pos]} Materia: {lista_materia_2[pos]}\n"
        f"\tNotas: {lista_notas_2[pos]}\n")

def imprmir_alumnos():
    for pos in range(len(lista_id_2)):
        print (f"\nid: {lista_id_2[pos]}  nombres: {lista_nombre1_2[pos]}{lista_nombre2_2[pos]} "
        f"\tapellidos: {lista_apellido1_2[pos]}{lista_apellido2_2[pos]}\n"
        f"\tEdad: {lista_edad_2[pos]} DNI: {lista_dni_2[pos]} Materia: {lista_materia_2[pos]}\n"
        f"\tNotas: {lista_notas_2[pos]}\n")


