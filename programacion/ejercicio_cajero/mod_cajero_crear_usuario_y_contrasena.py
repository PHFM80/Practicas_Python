import pickle

class classUsuario:

    def __init__(self, usuario, password, nombre, apellido):

        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "{} {} {} {}".format(self.usuario, self.password, self.nombre, self.apellido)
        
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
  
    def compararUsuario(self):
        while True:
            usuario = input("Ingrese un nombre de usuario: \n")
            if any(i.usuario == usuario for i in self.personas):
                print("El usuario ya existe. Deberá crear un nombre de usuario nuevo.")
            else:
                print("Usuario válido. Puede continuar.")
                break
        return usuario


listaPrincipalDeUsuarios = lista_usuarios()


#modulo pala verificacion de la creacion de la contraseña
def verificarPassword():
    while True:
        print("Ingrese una contraseña y el programa le indicará si es segura o no.\n"
              "La contraseña debe contener mínimo 10 caracteres.\n"
              "Debe contener al menos una minúscula, una mayúscula y un número.\n"
              "No puede haber espacios en blanco en la contraseña.\n")
        contr = input("Ingrese una contraseña segura: \n")

        if len(contr) < 10:
            print("La contraseña debe tener 10 caracteres o más. Contraseña Insegura.")
        elif not any(c.isdigit() for c in contr):
            print("La contraseña debe tener al menos un número. Contraseña Insegura.")
        elif not any(c.islower() for c in contr):
            print("La contraseña debe tener letras minúsculas. Contraseña Insegura.")
        elif not any(c.isupper() for c in contr):
            print("La contraseña debe tener letras mayúsculas. Contraseña Insegura.")
        elif ' ' in contr:
            print("La contraseña no debe tener espacios. Contraseña Insegura.")
        else:
            print("La contraseña es segura.")
            return contr


#Modulo par la creacion del usuario y la contraseña.  evitando la duplicacion de usuario
# y verificando la contraseña segura.
def crear_usuario():
    mijo = listaPrincipalDeUsuarios.compararUsuario()
    usuario = mijo
    #usuario = listaPrincipalDeUsuarios.compararUsuario()
    #primero verificar la unicidad del nombre de usuario, luego seguir con la carga de datos.
    contr = verificarPassword()
    password = contr
    #realizar el correcto ingreso de la contraseña
    nombre = input ("Ingrese su nombre:\n")
    apellido = input ("Ingrese su apellido:\n")

    usuario1 = classUsuario(usuario, password, nombre, apellido)
    listaPrincipalDeUsuarios.agregarPersona(usuario1) 



#Modulo para ingresar al cajero con un usuario ya existente
def ingresar_al_cajero ()
    pass