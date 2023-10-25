from mis_paquetes.salir_del_sistema_dyt_by_pablo_flores import salir_dyt_by_pf
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

def menu_principal_eng():
    while True:
        print("Welcome to the Banking System")
        print("1. Create a new account")
        print("2. Sign In")
        print("3. Exit")
        opcion = input("Select an option: ")
        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            salir_dyt_by_pf()
        else:
            print("Invalid option. Please select a valid option.")

def crear_cuenta():
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    if administrador_usuarios.crear_usuario(nombre_usuario, contrasena, nombre, apellido):
        print("Cuenta creada con éxito.")
    else:
        print("The username already exists. Please choose a different username.")

def iniciar_sesion():
    nombre_usuario = input("Enter your username: ")
    contrasena = input("Enter your password: ")
    usuario = administrador_usuarios.obtener_usuario_por_nombre(nombre_usuario)
    if usuario and usuario.contrasena == contrasena:
        menu_usuario(nombre_usuario)
    else:
        print("Invalid username or password. Please try again.")

def menu_usuario(nombre_usuario):
    while True:
        print(f"Welcome, {nombre_usuario}")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Log Out")
        opcion = input("Select an option: ")
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
            print("Invalid option. Please select a valid option.")

def deposito(nombre_usuario):
    monto = float(input("Enter the amount to deposit:"))
    if monto > 0:
        administrador_transacciones.crear_transaccion(nombre_usuario, "Deposit", monto)
        print("Successful deposit.")
    else:
        print("Invalid amount. Enter a positive value.")

def retiro(nombre_usuario):
    monto = float(input("Enter the amount to withdraw: "))
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    if monto > 0 and monto <= saldo:
        administrador_transacciones.crear_transaccion(nombre_usuario, "withdraw", monto)
        print("Successful withdrawal.")
    else:
        print("Invalid amount or insufficient balance. Please try again.")

def transferencia(nombre_usuario):
    persona = input ("Ingrese el usuario de la persona a quien le va a trasferirir:\n")
    monto = float(input("Enter the amount to transfer:  \n"))
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    if monto > 0 and monto <= saldo:
        administrador_transacciones.crear_transaccion(nombre_usuario, "Transfer", monto)
        print("Successful transfer.")
    else:
        print("Invalid amount or insufficient balance. Please try again.")

def consultar_saldo(nombre_usuario):
    saldo = administrador_transacciones.obtener_saldo_usuario(nombre_usuario)
    print(f"Your current balance is: ${saldo:.2f}")

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
                print("Transaction History: ")
                for transaccion in transacciones:
                    print(f"{transaccion.fecha} {transaccion.hora} - {transaccion.tipo}: ${transaccion.monto:.2f}, Saldo: ${transaccion.saldo:.2f}")
            else:
                print("No transaction history available.")
    except FileNotFoundError:
        print("No transaction history available.")

if __name__ == "__main__":
    menu_principal_eng()
