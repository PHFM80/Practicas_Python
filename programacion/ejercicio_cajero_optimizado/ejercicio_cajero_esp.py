import pickle
import datetime
import os

class Usuario:
    def __init__(self, nombre_usuario, contrasena, nombre, apellido):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido

class AdministradorUsuarios:
    def __init__(self, archivo_datos_usuarios):
        self.archivo_datos_usuarios = archivo_datos_usuarios
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.archivo_datos_usuarios):
            with open(self.archivo_datos_usuarios, 'rb') as archivo:
                try:
                    usuarios = pickle.load(archivo)
                except EOFError:
                    usuarios = []
        else:
            usuarios = []
        return usuarios

    def guardar_usuarios(self):
        with open(self.archivo_datos_usuarios, 'wb') as archivo:
            pickle.dump(self.usuarios, archivo)

    def crear_usuario(self, nombre_usuario, contrasena, nombre, apellido):
        if not self.obtener_usuario_por_nombre(nombre_usuario):
            usuario = Usuario(nombre_usuario, contrasena, nombre, apellido)
            self.usuarios.append(usuario)
            self.guardar_usuarios()
            return True
        else:
            return False

    def obtener_usuario_por_nombre(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None

class Transaccion:
    def __init__(self, fecha, hora, tipo, monto, saldo):
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo
        self.monto = monto
        self.saldo = saldo

class AdministradorTransacciones:
    def __init__(self, archivo_transacciones):
        self.archivo_transacciones = archivo_transacciones

    def crear_transaccion(self, nombre_usuario, tipo_transaccion, monto):
        usuario = administrador_usuarios.obtener_usuario_por_nombre(nombre_usuario)
        if usuario:
            saldo_usuario = self.obtener_saldo_usuario(nombre_usuario)
            if tipo_transaccion == "Depósito":
                saldo_usuario += monto
            elif tipo_transaccion == "Retiro":
                saldo_usuario -= monto
            transaccion = Transaccion(datetime.date.today(), datetime.datetime.now().strftime("%H:%M"), tipo_transaccion, monto, saldo_usuario)
            with open(f"{nombre_usuario}_transacciones", "ab") as archivo:
                pickle.dump(transaccion, archivo)

    def obtener_saldo_usuario(self, nombre_usuario):
        try:
            with open(f"{nombre_usuario}_transacciones", "rb") as archivo:
                transacciones = []
                try:
                    while True:
                        transaccion = pickle.load(archivo)
                        transacciones.append(transaccion)
                except EOFError:
                    pass
                if transacciones:
                    return transacciones[-1].saldo
                else:
                    return 0
        except FileNotFoundError:
            return 0

administrador_usuarios = AdministradorUsuarios("datos_usuarios.pkl")
administrador_transacciones = AdministradorTransacciones("transacciones.pkl")

def menu_principal():
    while True:
        print("Bienvenido al Sistema Bancario")
        print("1. Crear una nueva cuenta")
        print("2. Ingresar")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            exit(0)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def crear_cuenta():
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    if administrador_usuarios.crear_usuario(nombre_usuario, contrasena, nombre, apellido):
        print("Cuenta creada con éxito.")
    else:
        print("El nombre de usuario ya existe. Por favor, elija un nombre de usuario diferente.")

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario = administrador_usuarios.obtener_usuario_por_nombre(nombre_usuario)
    if usuario and usuario.contrasena == contrasena:
        menu_usuario(nombre_usuario)
    else:
        print("Nombre de usuario o contraseña inválidos. Intente nuevamente.")

def menu_usuario(nombre_usuario):
    while True:
        print(f"Bienvenido, {nombre_usuario}")
        print("1. Depósito")
        print("2. Retiro")
        print("3. Transferencia")
        print("4. Consultar Saldo")
        print("5. Historial de Transacciones")
        print("6. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            deposito(nombre_usuario)
        elif opcion == "2":
            retiro(nombre_usuario)
        elif opcion == "3":
            transferencia(nombre_usuario)
        elif opcion == "4":
            consultar_saldo(nombre_usuario)
        elif opcion == "5":
            historial_transacciones(nombre_usuario)
        elif opcion == "6":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def deposito(nombre_usuario):
    monto = float(input("Ingrese la cantidad a depositar: "))
    if monto > 0:
        administrador_transacciones.crear_transaccion(nombre_usuario, "Depósito", monto)
        print("Depósito exitoso.")
    else:
        print("Monto inválido. Ingrese un valor positivo.")

def retiro(nombre_usuario):
    monto = float(input("Ingrese la cantidad a retirar: "))
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    if monto > 0 and monto <= saldo:
        administrador_transacciones.crear_transaccion(nombre_usuario, "Retiro", monto)
        print("Retiro exitoso.")
    else:
        print("Monto inválido o saldo insuficiente. Intente nuevamente.")

def transferencia(nombre_usuario):
    persona = input ("Ingrese el usuario de la persona a quien le va a trasferirir:\n")
    monto = float(input("Ingrese la cantidad a transferir: \n"))
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    if monto > 0 and monto <= saldo:
        administrador_transacciones.crear_transaccion(nombre_usuario, "Transferencia", monto)
        print("Transferencia exitosa.")
    else:
        print("Monto inválido o saldo insuficiente. Intente nuevamente.")

def consultar_saldo(nombre_usuario):
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    print(f"Su saldo actual es: ${saldo:.2f}")

def historial_transacciones(nombre_usuario):
    try:
        with open(f"{nombre_usuario}_transacciones", "rb") as archivo:
            transacciones = []
            try:
                while True:
                    transaccion = pickle.load(archivo)
                    transacciones.append(transaccion)
            except EOFError:
                pass
            if transacciones:
                print("Historial de Transacciones:")
                for transaccion in transacciones:
                    print(f"{transaccion.fecha} {transaccion.hora} - {transaccion.tipo}: ${transaccion.monto:.2f}, Saldo: ${transaccion.saldo:.2f}")
            else:
                print("No hay historial de transacciones disponible.")
    except FileNotFoundError:
        print("No hay historial de transacciones disponible.")

if __name__ == "__main__":
    menu_principal()
