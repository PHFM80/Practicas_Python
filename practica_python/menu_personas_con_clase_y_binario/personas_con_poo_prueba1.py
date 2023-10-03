import pickle

class persona:

    def __init__(self, nombre, edad, sexo):
       
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        #el comando siguiente se puede y debe borrar
        print (f"Se ha creado una persona nueva cuyo nombre es: {self.nombre}")

    def __str__(self):
        return "{} {} {} ".format(self.nombre, self.edad, self.sexo)
        
class lista_personas:

    personas = []

    def __init__(self):
        listaDePersonas = open ("archivos_externos\datos_de_personas_prueba1", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print (f"se cargaron {len(self.personas)} desde el fichero externo")
        except:
            print ("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for i in self.personas:
            print (i)
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("archivos_externos/datos_de_personas_prueba1", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
    
    def mostrarFicheroExterno (self):
        print ("las personas en el fichero externo son: ")
        for i in (self.personas):
            print (i)


miListaPersonas = lista_personas()
personita = persona("martin", 32, "masc")
miListaPersonas.agregarPersona(personita)
personita = persona("marcela", 52, "fem")
miListaPersonas.agregarPersona(personita)
miListaPersonas.mostrarFicheroExterno()
