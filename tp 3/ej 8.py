print ('''Una universidad desea conocer losporcentajes de mujeres y hombres en al carrera de Desarrollo de Software.
  Se solicita unprograma para cargar la cantidad de mujeres y la cantidad de hombres, y que el mismo calcule y emita
por pantalla losporcentajes corresondientes.''')
print("")
cantHomb = int(input("ingrese la cantidad de hombres: "))
cantMujer = int(input("Ingrese la cantidad de  mujeres: "))
print ("- -  - - -  - -")
totAlumnos = cantHomb + cantMujer
porcHombres = (cantHomb * 100) / totAlumnos
porcMujer = (cantMujer * 100) / totAlumnos
print (f'''La cantidad total de alumnos es: {totAlumnos}.
El porentaje de hombres es: {round(porcHombres, 1)}%
El porcentaje de mujeres es: {round(porcMujer, 1)}''')

