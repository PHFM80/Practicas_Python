import datetime as dt
from os import system
from time import sleep

from rich.table import Table
import time
from rich.live import Live



def hora():
    hoy = dt.datetime.today() 
    horaActual = hoy.strftime("%H:%M:%S")
    return horaActual
def fecha():
    hoy = dt.datetime.today()
    fechaActual = hoy.strftime("%d-%m-%y")
    return fechaActual



id = []
operacion = []
importe = []
fechas = []
horas = []
saldo = 0
cont_id = 0

print ("\t\tBienvenido al Cajero Automatico.\n")

while True:
    try:
        sleep(2)
        system ("cls")
        print ("\t\tBienvenido al Cajero Automatico.\n")
        opc = int (input("Menu del cajero:\n"
                        "\t1. Realizar un deposito en la cuenta.\n"
                         "\t2. Realizar un retiro de la cuenta.\n"
                          "\t3. Ver los movieminetos de la cuenta.\n"
                           "\t4. Salir del cajero.\n" 
                           f"\t\t\t\t\tEl saldo en la cuenta es: ${saldo} \n"))
        
        if opc == 1:
            cont_id += 1
            monto = float(input("Ingrese el monto que desea depositar: \n"))
            saldo += monto
            print (f"El número de la transaccion es: {cont_id}, la transaccion es un deposito, "
                   f"el monto a depositar es: {monto}, en la fecha: {fecha()} a las {hora()}")
            sleep(2)
            id.append(cont_id)
            importe.append(monto)
            fechas.append(fecha())
            horas.append(hora())
            operacion.append("Deposito")

        elif opc == 2:
            monto = float(input("Ingrese el monto que desea extraer: \n"))
            if saldo > monto:
                cont_id += 1
                saldo -= monto
                print (f"El número de la transaccion es: {cont_id}, la transaccion es una extracción, "
                    f"el monto a extraer es: {monto}, en la fecha: {fecha()} a las {hora()}")
                sleep(5)
                id.append(cont_id)
                importe.append(monto)
                fechas.append(fecha())
                horas.append(hora())
                operacion.append("Extracción")
            else:
                print ("El monto que desea extraer supera el saldo.")
            sleep(1)
        elif opc == 3:
                table = Table()
                table.add_column("Id")
                table.add_column("Operacion")
                table.add_column("Importe")
                table.add_column("Fecha")
                table.add_column("Hora")

                with Live(table, refresh_per_second=4):
                    for i in range(len(id)):
                        time.sleep(0.4)
                        table.add_row(str(id[i]), operacion[i], str(importe[i]), fechas[i], horas[i])

                print(f"\t\t\t\t\tEl saldo en la cuenta es: ${saldo} \n")
                sleep(5)
        elif opc == 4:
            system ("cls")
            print ("\nSaliendo del programa...\n"
                    "\t\t\t\tD & T\n"
                    "\t\t\tPropuestas Digitales\n"
                    "\t\t\t\t\t\tBY Pablo Flores\n")
            sleep(5)
            system ("cls")
            exit (0)
        else:
            print ("Usted debe ingresar una opcion correcta.\n")
    except ValueError:
        print ("Usted ingreso una letra.\nDebe Ingresar solo números.\n")