class alumno:
    def __init__(self, claveAlum, dni, nombre, apellido, materia, notas):
        self.claveAlum = claveAlum
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.notas = notas

alumnos = []
notas = []

def ingresar_alumno():
    claveAlum = input("Ingrese la clave del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    materia = input("Ingrese la materia del alumno: ")
    notas = []
    while True:
        nota = input("Ingrese la nota del alumno: ")
        if nota == "":
            break
        notas.append(nota)
    alumnos.append(alumno(dni, nombre, apellido, materia, notas))

def mostrar_alumnos():
    for alumno in alumnos:
        print(alumno.claveAlum, alumno.dni, alumno.nombre, alumno.apellido, alumno.materia, alumno.notas)

def agregar_nota():
    

def modificar_nota():
    dni = input("Ingrese el DNI del alumno a modificar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            print("Ingrese la nueva nota del alumno: ")
            while True:
                nota = input("Ingrese la nota del alumno: ")
                if nota == "":
                    break
                alumno.notas.append(nota)

def eliminar_alumno():
    dni = input("Ingrese el DNI del alumno a eliminar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            alumnos.remove(alumno)

def modificar_datos():
    dni = input("Ingrese el DNI del alumno a modificar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            materia = input("Ingrese la materia del alumno: ")
            notas = []
            while True:
                nota = input("Ingrese la nota del alumno: ")
                if nota == "":
                    break
                notas.append(nota)
            alumno.nombre = nombre
            alumno.apellido = apellido
            alumno.materia = materia
            alumno.notas = notas

def salir():
    print("Adios, vuelve pronto.")
    exit()

#Menu Principal
 
print("Bienvenido al ingreso de alumnos.\n")


while True:
    print("Seleccione una de las opciones.\n"
      "1. Ingresar un alumno\n"
      "2. Mostrar todos los alumnos\n"
      "3. Agregar una nota.\n"
      "4. Modificar una nota.\n"
      "5. Eliminar un alumno.\n"
      "6. Modificar datos de un alumnos.\n"
      "7. Salir\n")
    opcion = int(input("Ingrese una opcion: \n"))
    if opcion == 1:
        ingresar_alumno()
    elif opcion == 2:
        mostrar_alumnos()
    elif opcion == 3:
        agregar_nota()
    elif opcion == 4:
        modificar_nota()
    elif opcion == 5:
        eliminar_alumno()
    elif opcion == 6:
        modificar_datos()
    elif opcion == 7:
        salir()
    else:
        print("Opcion incorrecta")

print("Adios, vuelve pronto.")

        