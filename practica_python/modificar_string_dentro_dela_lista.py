mi_lista = ["pablo \n", "\n flores", "esta en", "su \n casa", "\n"]
mi_lista2 = []
print (mi_lista)



# if not any ([c.isdigit() for c in contr]):
#             print ("La contraseña debe tener al menos un número.\n Contraseña Insegura")

for i in mi_lista:
    i = i.replace("\n", "")
    mi_lista2.append(i)

      

print (mi_lista)
print (mi_lista2)