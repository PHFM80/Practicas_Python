
def abrir_id():
    arch_id = open ("archivos_txt/id.txt", "r+", encoding="utf-8")
    lista_id = arch_id.readlines()
    arch_id.close()
    lista_id_2 = []
    for i in lista_id:
        i = i.replace("\n", "")
        lista_id_2.append(i)
    return lista_id_2

def abrir_nombre1():
    arch_nombre1 = open ("archivos_txt/nombre1.txt", "r+", encoding="utf-8")
    lista_nombre1 = arch_nombre1.readlines()
    arch_nombre1.close()
    lista_nombre1_2 = []
    for i in lista_nombre1:
        i = i.replace("\n", "")
        lista_nombre1_2.append(i)
    return lista_nombre1_2

def abrir_nombre2():
    arch_nombre2 = open ("archivos_txt/nombre2.txt", "r+", encoding="utf-8")
    lista_nombre2 = arch_nombre2.readlines()
    arch_nombre2.close()
    lista_nombre2_2 = []
    for i in lista_nombre2:
        i = i.replace("\n", "")
        lista_nombre2_2.append(i)
    return lista_nombre2_2

def abrir_apellido1():
    arch_apellido1 = open ("archivos_txt/apellido1.txt", "r+", encoding="utf-8")
    lista_apellido1 = arch_apellido1.readlines()
    arch_apellido1.close()
    lista_apellido1_2 = []
    for i in lista_apellido1:
        i = i.replace("\n", "")
        lista_apellido1_2.append(i)
    return lista_apellido1_2

def abrir_apellido2():
    arch_apellido2 = open ("archivos_txt/apellido2.txt", "r+", encoding="utf-8")
    lista_apellido2 = arch_apellido2.readlines()
    arch_apellido2.close()
    lista_apellido2_2 = []
    for i in lista_apellido2:
        i = i.replace("\n", "")
        lista_apellido2_2.append(i)
    return lista_apellido2_2

def abrir_edad ():
    arch_edad = open ("archivos_txt/edad.txt", "r+", encoding="utf-8")
    lista_edad = arch_edad.readlines()
    arch_edad.close()
    lista_edad_2 = []
    for i in lista_edad:
        i = i.replace("\n", "")
        lista_edad_2.append(i)
    return lista_edad_2

def abrir_dni():
    arch_dni = open ("archivos_txt/dni.txt", "r+", encoding="utf-8")
    lista_dni = arch_dni.readlines()
    arch_dni.close()
    lista_dni_2 = []
    for i in lista_dni:
        i = i.replace("\n", "")
        lista_dni_2.append(i)
    return lista_dni_2

def abrir_materia():
    arch_materia = open ("archivos_txt/materia.txt", "r+", encoding="utf-8")
    lista_materia = arch_materia.readlines()
    arch_materia.close()
    lista_materia_2 = []
    for i in lista_materia:
        i = i.replace("\n", "")
        lista_materia_2.append(i)
    return lista_materia_2

def abrir_notas():
    arch_notas = open ("archivos_txt/notas.txt", "r+")
    lista_notas = arch_notas.readlines()
    arch_notas.close()
    lista_notas_2 = []
    for i in lista_notas:
        i = i.replace("\n", "")
        i = i.replace("\t", "")
        lista_notas_2.append(i)
    return lista_notas_2

def imprimir_un_alumno(pos): 

    lista_id = abrir_id()
    lista_nombre1 = abrir_nombre1()
    lista_nombre2 = abrir_nombre2()
    lista_apellido1 = abrir_apellido1()
    lista_apellido2 = abrir_apellido2()
    lista_edad = abrir_edad()
    lista_dni = abrir_dni()
    lista_materia = abrir_materia()
    lista_notas = abrir_notas()

    print (f"\nid: {lista_id[pos]}  nombres: {lista_nombre1[pos]}{lista_nombre2[pos]} "
        f"\tapellidos: {lista_apellido1[pos]}{lista_apellido2[pos]}\n"
        f"\tEdad: {lista_edad[pos]} DNI: {lista_dni[pos]} Materia: {lista_materia[pos]}\n"
        f"\tNotas: {lista_notas[pos]}\n")

def imprmir_alumnos():

    lista_id = abrir_id()
    lista_nombre1 = abrir_nombre1()
    lista_nombre2 = abrir_nombre2()
    lista_apellido1 = abrir_apellido1()
    lista_apellido2 = abrir_apellido2()
    lista_edad = abrir_edad()
    lista_dni = abrir_dni()
    lista_materia = abrir_materia()
    lista_notas = abrir_notas()

    for pos in range(len(lista_id)):
        print (f"\nid: {lista_id[pos]}  nombres: {lista_nombre1[pos]}{lista_nombre2[pos]} "
        f"\tapellidos: {lista_apellido1[pos]}{lista_apellido2[pos]}\n"
        f"\tEdad: {lista_edad[pos]} DNI: {lista_dni[pos]} Materia: {lista_materia[pos]}\n"
        f"\tNotas: {lista_notas[pos]}\n")


