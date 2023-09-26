import os
def crear_archivo(nombre):
    archivo =open(f'{nombre}.txt','w')
    archivo.close()

def modificar_archivo(ruta,texto):
    if os.path.exists(f'{ruta}.txt'):
        archivom =open(f'{ruta}.txt','w')
        archivom.write(texto)
        archivom.close()
    else:
        print("El archivo no existe")
    
def borrar_archivo(archivoBorrar):
    if os.path.exists(f'{archivoBorrar}.txt'):
        os.remove(f'{archivoBorrar}.txt')
    else:
        print("El archivo no existe")
   
def abrir_archivo(archivoAbrir):
    if os.path.exists(f'{archivoAbrir}.txt'):
        abierto = open(f'{archivoAbrir}.txt')
        text = abierto.read()
        print(text)
        abierto.close()

    else:
        print("El archivo no existe")

ciclo = True

while ciclo:
    menu = ("ESTAS SON LAS OPERACIONES QUE PUEDE RELAIZAR \n 1 Crear archivo \n 2 Modificar archivo \n 3 Borrar archivo \n 4 Abrir archivo \n 5 SALIR")
    print (menu)
    opcion = input("ESCRIBA EL NUMERO DE LA OPERACION QUE DESEA REALIZAR = ")
    if opcion == "1":
        nombre = input("ingrese el nombre del archivo a crear=")
        crear_archivo(nombre)

    elif opcion == "2":
       ruta = input("ingrese el nombre del archivo a modificar = ")
       texto = input("ingreseel el texto que se agregara al archivo = ")
       modificar_archivo(ruta,texto)

    elif opcion == "3": 
        archivoBorrar = input("ingrese el nombre del archivo que desea borrar=")  
        borrar_archivo(archivoBorrar)
        
    elif opcion == "4":
        archivoAbrir = input("ingrese el nombre del archivo que desea abrir=")  
        abrir_archivo(archivoAbrir)
         
    elif opcion == "5":
        break
# REALIZADO POR: GUSTAVO ARCHUNDIA GARCIA II-402