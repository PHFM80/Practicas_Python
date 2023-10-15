import json

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre_usuario, contrasena, nombre, apellido):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = 0
        self.movimientos = []

    def agregar_movimiento(self, tipo, monto):
        self.movimientos.append({"tipo": tipo, "monto": monto})

# Lista para almacenar usuarios registrados
usuarios_registrados = []

# Función para cargar usuarios desde un archivo JSON
def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios_registrados.extend(json.load(archivo))
    except FileNotFoundError:
        pass

# Función para guardar usuarios en un archivo JSON
def guardar_usuarios():
    with open("usuarios.json", "w") as archivo:
        json.dump([vars(user) for user in usuarios_registrados], archivo)

# Función para crear un nuevo usuario
def crear_usuario():
    # Solicitar datos del usuario
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña segura: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    # Verificar si el nombre de usuario ya existe
    if any(user.nombre_usuario == nombre_usuario for user in usuarios_registrados):
        print("El nombre de usuario ya existe. Intente con otro.")
    else:
        nuevo_usuario = Usuario(nombre_usuario, contrasena, nombre, apellido)
        usuarios_registrados.append(nuevo_usuario)
        print("Usuario creado con éxito.")

# Función para transferir dinero
def transferir_dinero(usuario):
    destinatario = input("Ingrese el nombre de usuario del destinatario: ")
    monto = float(input("Ingrese el monto a transferir: "))

    if usuario.saldo > 0:
        # Agregar el movimiento al remitente
        usuario.agregar_movimiento("Transferencia saliente", monto)

        # Si el destinatario no existe, crear una cuenta temporal
        destinatario_temporal = next((user for user in usuarios_registrados if user.nombre_usuario == destinatario), None)
        if destinatario_temporal is None:
            destinatario_temporal = Usuario(destinatario, "", "", "")
            usuarios_registrados.append(destinatario_temporal)

        # Agregar el movimiento al destinatario
        destinatario_temporal.agregar_movimiento("Transferencia entrante", monto)
    else:
        print("Saldo insuficiente para realizar transferencias.")

# Función para ver los movimientos de un usuario
def ver_movimientos(usuario):
    for movimiento in usuario.movimientos:
        print(f"Tipo: {movimiento['tipo']}, Monto: {movimiento['monto']}")

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    for usuario in usuarios_registrados:
        if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
            menu_usuario(usuario)
            return
    print("Nombre de usuario o contraseña incorrectos.")

# Función del menú de inicio de sesión
def menu_login():
    while True:
        print("1. Iniciar sesión")
        print("2. Crear usuario nuevo")
        print("3. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para depositar dinero
def depositar_dinero(usuario):
    monto = float(input("Ingrese el monto a depositar: "))
    usuario.saldo += monto
    print(f"Depósito exitoso. Saldo actual: {usuario.saldo}")

# Función para retirar dinero
def retirar_dinero(usuario):
    if usuario.saldo > 0:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= usuario.saldo:
            usuario.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {usuario.saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    else:
        print("Saldo insuficiente para realizar retiros.")

# Función para ver los movimientos de un usuario
def ver_movimientos(usuario):
    for movimiento in usuario.movimientos:
        print(f"Tipo: {movimiento['tipo']}, Monto: {movimiento['monto']}")

# Función del menú de usuario
def menu_usuario(usuario):
    while True:
        print(f"Bienvenido, {usuario.nombre} {usuario.apellido}")
        print(f"Saldo actual: {usuario.saldo}")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Transferir dinero")
        print("4. Ver movimientos")
        print("5. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            depositar_dinero(usuario)
        elif opcion == "2":
            retirar_dinero(usuario)
        elif opcion == "3":
            transferir_dinero(usuario)
        elif opcion == "4":
            ver_movimientos(usuario)
        elif opcion == "5":
            print("Cerrando sesión. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función del menú principal
def menu_principal():
    cargar_usuarios()
    while True:
        print("1. Español")
        print("2. English")
        print("3. Salir")
        opcion = input("Elija un idioma: ")

        if opcion == "1":
            menu_login()
        elif opcion == "2":
            print("English menu")
        elif opcion == "3":
            print("Gracias por usar el cajero automático.")
            guardar_usuarios()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu_principal()





