print ('''Tres personas deciden invertir su dinero para fundar una empresa.
 Cada una de ellas invierte una cantidad distinta de dinero.
 Obtener el porcentaje que invierte cada uno consrespecto a la cantidad total invertida''')
print("")
cap1 = int(input("ingrese el capital de la 1er persona: $"))
cap2 = int(input("ingrese el capital de la 2da persona: $"))
cap3 = int(input("ingrese el capital de la 3er persona: $"))
print   ("")
inverTotal = cap1 + cap2 + cap3
porcenInvers1 = (100*cap1)/inverTotal
porcenInvers2 = (100*cap2)/inverTotal
porcenInvers3 = (100*cap3)/inverTotal
print (f"La inversión total es: ${inverTotal}")
print (f'''El porcentaje de inversion de la primer persona es: {round(porcenInvers1, 1)}%.
El porcentaje de inversion de la segunda persona es: {round(porcenInvers2, 1)}%.
El porcentaje de inversion de la tercer persona es: {round(porcenInvers3, 1)}%.''')