import random

# lista1 = ["pablo", "gabriel", "matias", "rafael", "sofia", "Franco"]
# lista1_1 = [1, 2, 3, 4, 5, 6]
# lista1_2 = [42, 35, 20, 21, 19, 22]

# matriz = []

# for i in range(len(lista1)):
#     datitos = []
#     datitos.append(lista1_1[i])
#     datitos.append(lista1[i])
#     datitos.append(lista1_2[i])
#     print (datitos)
#     matriz.append(datitos)
    
# print (f"esta es la matriz: \n{matriz}")
# print ("")

# print("\nmatriz en forma de matriz con corchetes\n")
# for i in matriz:
#     print (i)

# print ("\n Matriz en forma de matriz sin corchetes.\n")
# print ("id\tnombre  \tedad")
# for i in matriz:
#     print ("")
#     for j in i:
#         print (j, end=" \t  ")





#lista2 = [0, 1, 2]

# cadena = "ies9023"
# print (cadena[3:5])
# print (cadena [::])
# print (cadena [:2])
# print (cadena [3:])

# lista2.insert(1,1)
# print (lista2)
# print (sum(lista2[0:3]))



# matriz2 = [[1,2,3],[4,5,6],[7,8,9]]

# print (matriz2)

# for i in matriz2:
#     print ("\n")
#     for j in i:
# #         print (j, end="\t") 
matriz3 = []
for i in range (5):
    matriz3.append([0]*5)

for i in range (5):
    for j in range(5):
        matriz3[i][j] = random.randint(0,9)


print (matriz3)
print("")
for i in matriz3:
    print("\n")
    for j in i:
        print(j, end="\t")












