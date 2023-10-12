import pickle

class usuario:

    def __init__(self, user, contrasenia):
       
        self.user = user
        self.contrasenia = contrasenia

        #el comando siguiente se puede y debe borrar
        print (f"Se ha creado una persona nueva cuyo nombre es: {self.user}")

    def __str__(self):
        return "{} {} {}".format(self.user, self.contrasenia)
        
class lista_usuarios:

    personas = []

    def __init__(self):
        listaDePersonas = open ("archivos_cajero\datos_de_usuarios", "ab+")
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
        listaDePersonas = open("archivos_cajero\datos_de_usuarios", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
    
    def mostrarFicheroExterno (self):
        print ("las personas en el fichero externo son: ")
        for i in (self.personas):
            print (i)


miListaPersonas = lista_usuarios()



miListaPersonas.mostrarFicheroExterno()
