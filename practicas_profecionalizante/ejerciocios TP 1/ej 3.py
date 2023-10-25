"""Ejercicio 3
Ahora deberá crear estas 5 variables: materiapreferida, pasatiempo, deporte, familia, nrodemascotas
Inicializarlas por teclado
Luego Imprima por pantalla la siguiente frase:
Mi materia preferida en el colegio es Programación. Mi pasatiempo preferido es dormir. Practico correr como
deporte. En mi familia somos 4 personas y 2 mascotas
Tenga en cuenta cómo hacer para mostrar texto con variables, todo en un mismo texto."""

materiapreferida = input("Ingrese materia preferida: ")
pasatiempo = input("Ingrese pasatiempo preferido: ")
deporte = input("Ingrese deporte preferido: ")
familia = int(input("Ingrese cuantos miembros son en su familia: "))
nrodemascotas = int(input("Ingrese numero de mascotas: "))

print (f"Mi materia preferida en el colegio es {materiapreferida}. Mi pasatiempo preferido es {pasatiempo}."
       f" Practico {deporte} como deporte. "
       f"\nEn mi familia somos {familia} personas y {nrodemascotas} mascotas")



