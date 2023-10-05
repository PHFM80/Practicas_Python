import pickle
import clase_del_menu_prueba2 as c_p


class listaDePersonas:

    persona =[]

    def __init__(self):
        listaDePersonas = open ("archivos_externos\datos_de_personas_prueba2", "ab+")
        listaDePersonas.seek(0)
        try:
            self.persona = pickle.load(listaDePersonas)
            print (f"se cargaron {len(self.persona)} desde el fichero externo")
        except:
            print ("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
            

    def guardar_datos_en_lista(self, personita):
        self.persona.append(personita)
        self.guardar_personas_en_fichero_externo()

    
    def guardar_personas_en_fichero_externo(self):
        listaDePersonas = open("archivos_externos/datos_de_personas_prueba2", "wb")
        pickle.dump(self.persona, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrar_fichero_externo(self):
        print ("las personas en el fichero externo son: ")
        for i in self.persona:
            print (i)
        print (f"El numero de la ultima persona es: {len(self.persona)}")

    def desarmar_e_iterar_datos():
        

        pass

listaPrincipalDePersonas = listaDePersonas()


def ingresar_persona():

    print (f"La ultima ID es:  ")
    id = input ("Ingrese la ID de la persona:  ")
    nomb1 = input ("Ingrese el 1er nombre de la persona:  ")
    nomb2 = input ("Ingrese el 2do nombre de la persona: ")
    ape1 = input ("Ingrese el 1er apellido de la persona: ")
    ape2 = input ("Ingrese el 2do apellido de la persona: ")
    dni = input ("Ingrese el DNI de la persona: ")
    edad = input ("Ingrese la edad de la persona: ")
    f_nac = input ("Ingrese la fecha de nacimiento de la persona."
                "con el siguiente formato DD-MM-YYYY : ")
    
    personita = c_p.persona(id, nomb1, nomb2, ape1, ape2, dni, edad, f_nac)    
    resp = input ("¿Esta seguro de guardar los datos?\n"
                "\tSI _ para ingresar los datos.\n"
                "\tNO _ para volver al inicio.\n").upper()
    if resp == "SI":
        print (f"esta es la personita creada\n {personita}")
        listaPrincipalDePersonas.guardar_datos_en_lista(personita)
        print ("Acaba de ingresar los datos de la persona.\n")

    elif resp == "NO":
        print ("Volviendo al menu principal.")
        
    else:
        print ("Ingrese una opción correcta")







