nombre = ["pablo", "emi", 1 , "luchi"]

for i in range(0, len(nombre)):
     print(f"la posicion es {i+1} y el valor de la lista es'{nombre[i]}'")
    
   
otro = input("ingrese un valor: ")
nombre.append(otro)
 
for i in range(0, len(nombre)):
     print(f"la posicion es {i+1} y el valor de la lista es'{nombre[i]}'")