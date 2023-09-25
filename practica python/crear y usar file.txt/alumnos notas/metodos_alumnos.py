import clase_alumnos as c_a
import os

alumno = []
notas = []

#Cargar datos de un alumno y las primeras notas
def ingresar_alumno():
    c_a.id = int (input ("Ingrese el ID del alumno: "))
    alumno.append(c_a.id)
    c_a.nombre1 = str (input ("Ingrese el 1er nombre del alumno: "))
    alumno.append(c_a.nombre1)
    c_a.nombre2 = str (input ("Ingrese el 2do nombre del alumno: "))
    alumno.append(c_a.nombre2)
    c_a.apellido1 = str (input ("Ingrese el 1er apellido del alumno: "))
    alumno.append(c_a.apellido1)
    c_a.apellido2 = str (input ("Ingrese el 2do apellido del alumno: "))
    alumno.append(c_a.apellido2)
    c_a.edad = int (input ("Ingrese la edad del alumno: "))
    alumno.append(c_a.edad)
    c_a.dni = int (input( "ingrese el DNI del alumno: "))
    alumno.append(c_a.dni)
    c_a.materia = str (input ("Ingrese la materia del alumno: "))
    alumno.append(c_a.materia)

    while True:
        nota = input("Ingrese la nota del alumno: ")
        if nota == "":
            break
        nota = int (nota)
        alumno.append(nota)
        notas.append(nota)
    
def cargar_alumno_a_txt():
    archivo_id = open ("id.txt", "a")
    id = c_a.id
    archivo_id.write("id")
    archivo_id.write(" \n")
    archivo_id.close()
    
    archivo_nombre1 = open ("nombre1.txt", "a")
    nombre1 = c_a.nombre1
    archivo_nombre1.write(nombre1)
    archivo_nombre1.write(" \n")
    archivo_nombre1.close()

    
    
    
    
    
    
    








