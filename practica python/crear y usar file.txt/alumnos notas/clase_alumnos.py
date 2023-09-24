class alumnos:
    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, edad, dni, materia, notas):
        self.id = id
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.dni = dni
        self.materia = materia
        self.notas = notas
    
    def estado_alumno(self):
        print (f"ID: {self.id}  {self.nombre1} {self.nombre2}, {self.apellido1} {self.apellido2}\n"
               f"edad: {self.edad} \t DNI: {self.dni} \t Materia: {self.materia}\n"
               f"Notas: {self.notas} \n")
        
    

alumno = []
nota =[]



