# for i in ["Regulariza", "Recursa","Promociona"]:
#     print (f"este resultado {i} tal vez lo obtendra al finalizar el cursado de la materia. ")


# c = 0
# for i in [2,3,4,5,8,9]:
#     c +=1 
#     print (f"El {c} * mes de mayor inflación en este año fue el {i} mes del año") 
# print(f"La Inflación del mes {i + 1}° será record")

# meses =["mayo", "junio", "diciembre"]

# feriados = ["inamovibles", "turisticos" ]
# for i in range(len(meses)): 
#     print(f"\n El mes {meses[i]} tiene feriados: ")
#     for j in range(len(feriados)): 
#         if feriados[j]== "turisticos":
#             break 
#         print(feriados[j], end="")


def ordenar(modo, lista):
    desorden = True
    if modo == 1:
        while desorden:
            desorden = False
            for i in range(len(lista)-1):
                if lista[i]> lista[i + 1] :
                    desorden = True
                    m = lista[i + 1]
                    lista[i+1]= lista[i]
                    lista[i] =m
    return lista


def ordenar2(modo, lista):
    desorden = True
    if modo == 2:
        while desorden:
            desorden = False
            for i in range(len(lista)-1):
                if lista[i]< lista[i + 1] :
                    desorden = True
                    m = lista[i + 1]
                    lista[i+1]= lista[i]
                    lista[i] =m
    return lista

lista = [8, 3, 1, 7, 3, 7,21, 4]
lista2 = [8, 3, 1, 7, 3, 7,21, 4]
orden1 = ordenar(1, lista)
orden2 = ordenar2(2, lista2)

print (f"esta es la lista ordenada en forma ascendente: {orden1}")

print (f"esta es la lista ordenada en forma descendente: {orden2}\n")


