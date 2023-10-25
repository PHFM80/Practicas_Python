import pickle
import datetime
from os import system
from time import sleep
from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf

# Obtener la fecha actual
fecha_actual = datetime.date.today().strftime("%d-%m-%y")
# Obtener la hora actual
hora_actual = datetime.datetime.now().time().strftime("%H:%M")

class claseUsuario:

    def __init__(self, usuario, password, nombre, apellido):

        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "{} {} {} {}".format(self.usuario, self.password, self.nombre, self.apellido)

class lista_usuarios:
    personas = []
    # Carga todos los datos de los usuarios a la lista personas
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
            print (f"Usuario: {i.usuario},\tPassword: {i.password}.\n"
                   f"nombre: {i.nombre},\tApellido: {i.apellido}")
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("archivos_cajero\datos_de_usuarios", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
     
    def compararUsuario(self):
        while True:
            usuario = input("Ingrese un nombre de usuario: \n")
            if any(i.usuario == usuario for i in self.personas):
                print("El usuario ya existe. Deberá crear un nombre de usuario nuevo.")
            else:
                print("Usuario válido. Puede continuar.")
                break
        return usuario

    def verificarUsuario(self, usuario):
        for i in self.personas:
            if i.usuario == usuario:
                return True
        
    def compararPassword(self, contr):
        for i in self.personas:
            if i.password == contr:
                return True

listaPrincipalDeUsuarios = lista_usuarios()

class transaccion:
    def __init__(self, fecha, hora, tipo, monto, saldo):
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo
        self.monto = monto
        self.saldo = saldo
    def __str__(self):
        return "{} {} {} {} {}".format(self.fecha, self.hora, self.tipo, self.monto, self.saldo)
    
# Crea y guarda los datos de las transacciones hechas por cada usuario
class lista_transacciones:

    transaccion_usuario = []

    # crear el archivo cuando se crea un usuario nuevo.  Exclusivo para ese usuario
    def crear_archivo_transacciones(usuario):
        archivo = open (f"archivos_cajero\{usuario}", "wb+")
        fecha = fecha_actual
        hora = hora_actual
        tipo = "apertura de cuenta"
        monto = 0
        saldo = 0
        transaccion1 = transaccion(fecha, hora, tipo, monto, saldo)
        pickle.dump(transaccion1, archivo)
        archivo.close()

    # abrir el archivo para el usuario que ingreso
    def abrir_archivo_usuario(self, user):
        archivo = open (f"archivos_cajero\{user}", "wb+")
        self.transaccion_usuario = pickle.load(archivo)
        archivo.close()
        del(archivo)

    def hacer_deposito(self, user):
        lista_transacciones.abrir_archivo_usuario()
        archivo = open (f"archivos_cajero\{user}", "wb+")
        saldo1 = 0
        for i in self.transaccion_usuarios:
            print (f"El saldo es: {i.saldo}")
            saldo1 = i.saldo

        monto = input ("Ingrese el monto a depositar:\n")
        fecha = fecha_actual
        hora = hora_actual
        tipo = "Deposito"
        saldo = saldo1 + monto
        transaccion1 = transaccion(fecha, hora, tipo, monto, saldo)
        pickle.dump(transaccion1, archivo)
        archivo.close()

   



#listaDeTransaccionPorUsuario = lista_transacciones

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

    usuario1 = claseUsuario(usuario, password, nombre, apellido)
    listaPrincipalDeUsuarios.agregarPersona(usuario1) 
    lista_transacciones.crear_archivo_transacciones(usuario)

### modulos del menu de transacciones del cajero
#modulo de deposito
def deposito(usuario):
    system("cls")
    print("Sección de depositos del cajero automático de IES 9023.\n"
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print (usuario)
    user = usuario
    lista_transacciones.abrir_archivo_usuario(user)
    lista_transacciones.hacer_deposito(user)
    

#Modulo para ingresar al cajero con un usuario ya existente
def ingresar_al_cajero():
    while True:
        system("cls")
        print("Sección de ingreso al cajero automático de IES 9023.\n"
              "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        usuario = input("Por favor ingrese su nombre de usuario:\n")
        password = input("Por favor ingrese su contraseña.\n")
        if listaPrincipalDeUsuarios.verificarUsuario(usuario) and listaPrincipalDeUsuarios.compararPassword(password):
            print("Ingresando al menú principal de usuario...\n")
            sleep(2)
            system("cls")

            while True:
                system("cls")
                print("Sección de transacciones del cajero automático de IES 9023.\n"
                    "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                try:
                    opc = int(input("Seleccione la opción que desea consultar\n"
                                    "\t1. Depósito.\n"
                                    "\t2. Extracción.\n"
                                    "\t3. Transferencia.\n"
                                    "\t4. Consultar saldo.\n"
                                    "\t5. Consultar Movimientos.\n"
                                    "\t6. Salir del programa.\n"))
                    if opc == 1:
                        deposito(usuario)
                    elif opc == 2:
                        pass
                    elif opc == 3:
                        pass
                    elif opc == 4:
                        pass
                    elif opc == 5:
                        pass
                    elif opc == 6:
                        salir_dyt_by_pf()
                        pass
                    else:
                        print("Ingrese una opción correcta")
                except ValueError:
                    print("Ingresó una letra, debe ingresar solo números.")
        elif not listaPrincipalDeUsuarios.verificarUsuario(usuario):
            print("El usuario no existe.\nDeberá crear un nuevo usuario.\n")
            sleep(2)
            system("cls")
            break
        elif listaPrincipalDeUsuarios.verificarUsuario(usuario) and not listaPrincipalDeUsuarios.compararPassword(password):
            print("Contraseña Incorrecta.\n")
            sleep(2)
            system("cls")


user = "pablito1"
deposito(user)
