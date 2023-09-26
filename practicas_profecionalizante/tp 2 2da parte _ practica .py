import math

print ("\nDESAFÍO ARITMÉTICA"
"Estás organizando una fiesta para tus amigos y necesitás calcular cuánto vino comprar.\n" 
"Una caja de vino contiene 6 botellas, cada botella contiene 0,75 litros.\n" 
"Una medida estándar de vino es 0.175 litros. Debés invitar a 20 personas a la fiesta.\n" 
"Prepara las constantes y variables para llevar a cabo el cálculo.\n" 
"Responde luego las siguientes preguntas:\n" 
"\ta. ¿Cuántos vasos llenos de vino obtienes por botella?\n" 
"\tb. ¿Cuánto vino queda en cada botella, considerando que no podes llenar copas de vino de distintas botellas?\n" 
"\tc. Todos han confirmado su asistencia, ¿cuántas personas estarán en la fiesta?\n"
"\td. 3 personas no toman alcohol, ahora ¿cuántas personas tenés que considerar?\n"
"\te. Si todas las personas toman 4 copas de vino y solo considera copas llenas.\n"
"\t\tI. ¿Cuántas botellas de vino necesitara? ¿Cuántas cajas de vino necesitará?\n"
"\t\tII. Y si considera las cantidades totales de vino ¿Cuántas botellas de vino necesitara?"
            "¿Cuántas cajas de vino necesitará?\n"
"\t\tIII. Considerando que solo puede comprar los vinos por caja completa "
            "¿cuantas botellas llenas de vino quedarán después de la fiesta? \n")

caja_vino = 6
botella = 0.75
vaso_de_vino = 0.175
cant_invitados = int(input("Ingrese la cantidad de invitados\n"))

print("a. ¿Cuántos vasos llenos de vino obtienes por botella?\n")
vasos_lleno = botella // vaso_de_vino
print(f"De cada botella se llenan {math.ceil(vasos_lleno)} vasos.\n")

print("b. ¿Cuánto vino queda en cada botella, considerando que no podes llenar copas de vino de distintas botellas?\n")
resto_botella = botella % vaso_de_vino
print (f"Lo que queda en cada botella es: {round(resto_botella, 3)} cc.\n")

print("c. Todos han confirmado su asistencia, ¿cuántas personas estarán en la fiesta?\n")
invit_confirmados = int(input ("Ingrese la cantidad de invitados que confirmaron su asistencia: \n"))
print (f"\nInvité a {cant_invitados}, confirmaron su asistencia: {invit_confirmados}.\n"
       f"Asistiran a la fiesta {invit_confirmados}")

print ("\nd. 3 personas no toman alcohol, ahora ¿cuántas personas tenés que considerar?\n")
invit_que_tomal_alcohol = invit_confirmados - 3
print (f"las personas que toman alcohol son: {invit_que_tomal_alcohol}")

print ("\ne. Si todas las personas toman 4 copas de vino y solo considera copas llenas.\n"
"I. ¿Cuántas botellas de vino necesitara? ¿Cuántas cajas de vino necesitará?\n")

botellas_necesarias = ((invit_que_tomal_alcohol * 4) * botella) / vasos_lleno
print (f"Se necesitaran: {math.ceil(botellas_necesarias)} botellas\n")
cajas_necesarias = botellas_necesarias / caja_vino
print (f"Se necesitaran: {math.ceil(cajas_necesarias)} cajas\n")

print ("\ne. Si todas las personas toman 4 copas de vino y solo considera copas llenas.\n"
"II. Y si considera las cantidades totales de vino ¿Cuántas botellas de vino necesitara?"
        "¿Cuántas cajas de vino necesitará?\n")
copas_X_botella = botella/vaso_de_vino
botellas_necesarias_totales = ((invit_que_tomal_alcohol * 4 ) * botella) / copas_X_botella
cajas_necesarias_totales = math.ceil(botellas_necesarias_totales / caja_vino)

print (f"La cantidad de botellas totales usando todo el vino son: {math.ceil(botellas_necesarias_totales)} botellas")
print (f"La cantidad de cajas totales usando todo el vino son: {cajas_necesarias_totales} cajas de vino")

print ("\ne. Si todas las personas toman 4 copas de vino y solo considera copas llenas.\n"
"III. Considerando que solo puede comprar los vinos por caja completa " 
        "¿cuantas botellas llenas de vino quedarán después de la fiesta? \n")
        
resto_botella_final_fiesta = (math.ceil(cajas_necesarias) * caja_vino) % botellas_necesarias

print (f"Quedaran despues de la fiesta: {math.ceil(resto_botella_final_fiesta)} botellas")

