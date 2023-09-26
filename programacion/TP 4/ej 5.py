edad = int (input("Ingresa la edad del individuo: "))
talla = int (input("Ingrese la estatura del individuo en centimetros: "))
peso = int ( input("Ingrese el peso del individuo: "))
tallaMt = talla/100
imc = peso / pow(tallaMt, 2)
imc = round(imc, 1)

print("- -  - - -  - -")

print("El IMC del individuo es: ", imc)
print("- -  - - -  - -")
if imc <22.0 and edad < 45:
    print("Riesgo Bajo")
elif imc < 22.0 and edad >= 45:
    print("Riesgo Moderado")
elif imc > 22.0 and edad >=45:
    print("Riesgo Alto")
else: 
    print("Riesgo Moderado")

