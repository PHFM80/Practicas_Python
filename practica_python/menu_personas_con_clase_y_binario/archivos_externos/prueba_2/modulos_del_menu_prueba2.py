import pickle
import clase_del_menu_prueba2 as c_p

listaPrincipalDePersonas = []

def ingresar_persona():

    print ("la ultima ID es: ")
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
        listaPrincipalDePersonas.append(personita)
        print ("Acaba de ingresar los datos de la persona.\n")
    elif resp == "NO":
        print ("Volviendo al menu principal.")
        #break
    else:
        print ("Ingrese una opción correcta")










