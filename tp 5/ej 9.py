valHoraD = 100
valorHoraP = 150
valorHoraI = 220
horTrabD = 0
horTrabP = 0
horTrabI = 0
acumSueldoD = int(0)
acumsueldoP = 0
acumSueldoI = 0
acumHorasD = 0
acumHorasP = 0
acumHorasI = 0
totEmpD = 0
totEmpP = 0
totempI = 0

while True:
    resp = input('''Bienvenido al sistema de sueldos.
las categorias de empleados son:
D_ Data Entry
P_ Programador
I_ Ingeniero
S_ Salir del sistema
Ingrese una categoria:    ''').upper()
    print("- - - - - - - - -")
    if resp == "D":
        totEmpD += 1
        horas = int(input("Ingrese la cantidad de horas trabajas por este empleado: "))
        acumHorasD += horas
        sueldo = horas * valHoraD
        acumSueldoD += sueldo
        print("- - - - - - - - -")
    elif resp == "P":
        totEmpP += 1
        horas = int(input("Ingrese la cantidad de horas trabajas por este empleado: "))
        acumHorasP += horas
        sueldo = horas * valorHoraP
        acumsueldoP += sueldo
        print("- - - - - - - - -")
    elif resp == "I":
        totempI += 1
        horas = int(input("Ingrese la cantidad de horas trabajas por este empleado: "))
        acumHorasI += horas
        sueldo = horas * valorHoraI
        acumSueldoI += sueldo
        print("- - - - - - - - -")
    elif resp == "S":
        print("- - - - - - - - -")
        totEmp = totEmpD + totempI + totEmpP
        totHoras = acumHorasD + acumHorasI + acumHorasP
        totSueldo = acumSueldoD + acumSueldoI + acumsueldoP
        print("Total de empleados: ", totEmp)
        print("Total de horas trabajadas: ", totHoras)
        print("Total de sueldos: ", totSueldo)
        print(": : : : : : : : : :")
        print(f"Total de empleados Data Entry: {totEmpD}")
        print(f"Total de empleados Programador: {totEmpP}")
        print(f"Total de empleados Ingeniero: {totempI}")
        print(": : : : : : : : : :")
        print(f"Total de horas trabajadas Data Entry: {acumHorasD}")
        print(f"Total de horas trabajadas Programador: {acumHorasP}")
        print(f"Total de horas trabajadas Ingeniero: {acumHorasI}")
        print(": : : : : : : : : :")
        print(f"Total de sueldos Data Entry: {acumSueldoD}")
        print(f"Total de sueldos Programador: {acumsueldoP}")
        print(f"Total de sueldos Ingeniero: {acumSueldoI}")
        print(": : : : : : : : : :")
        print("Saliendo del sistema")
        print("- - - - - - - - -")
        break
    else:
        print(": : : : : : : : : :")
        print("Ingrese una categoria valida")
        print(": : : : : : : : : :")






