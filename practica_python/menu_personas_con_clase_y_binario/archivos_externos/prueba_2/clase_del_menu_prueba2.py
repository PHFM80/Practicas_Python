
class persona:
    def __init__(self, id, nomb1, nomb2, ape1, ape2, dni, edad, fNac):
        self.id = id
        self.nomb1 = nomb1
        self.nomb2 = nomb2
        self.ape1 = ape1
        self.ape2 = ape2
        self.dni = dni
        self.edad = edad
        self.fNac = fNac

        print (f"Se ha creado una persona nueva.  ID: {self.id}  Nombre: {self.nomb1}")

    def __str__(self):
        return " {} {} {} {} {} {} {} {} ".format(self.id, self.nomb1, self.nomb2, self.ape1, self.ape2, self.dni, self.edad, self.fNac)
