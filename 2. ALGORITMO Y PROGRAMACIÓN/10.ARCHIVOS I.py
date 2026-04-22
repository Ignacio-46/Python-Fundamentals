#Los archivos permiten almacenar información de nuestros programas, tal que podemos
#crear, leer, modificar y eliminar los archivos

#Funcion open() : Es una función principalmente para trabajar archivos en Python
#open(nombre_archivo, modo)
# r => read (leer)
# a => append (anexar)
# w => write(escribir)
# x => create(crear)

#Otro modo:
# r+ => Lectura y escritura.
# w+ => Lectura y escritura. Si el archivo ya existe, se sobreescribe, si no existe, se crea uno nuevo
# a+ => Léctura y agregar. Si el archivo no existe, se crea para escritura.

#Crear un archivo
print("---*** Creando un Archivo ***---***")
mi_archivo = "Mi_Archivo.txt"
#Abrir el archivo de modo escritura ("w")
# archivo = open(mi_archivo, "w")                            Se abre el archivo
# archivo.write("Hola, como estás Nacho?\n")                 Se escribe el archivo
# archivo.write("Creando mi nuevo archivo\n")                Se escribe el archivo
# archivo.close()                                            Se cierra el archivo
# print(f"Se creo el archivo {mi_archivo}\n")                Se imprime el archivo

#Con bloque "with" facilita el manejo de abrir y cerra el archivo sin llamar close()
with open(mi_archivo, "w") as archivo:
    archivo.write("Hola, como estás Nacho?\n") #Se escribe el archivo
    archivo.write("Creando mi nuevo archivo\n")

print(f"Se creo el archivo {mi_archivo}\n")

#Se crea el archivo de modo exclusivo con try y except
print("---*** Se crea un archivo en modo exclusivo ***---")
#1° nombre_archivo normal
nombre_archivo = "Nombre_Archivo.txt"
try:
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Se crea el archivo en modo exclusivo\n")
        archivo.write("Creando nombre del archivo\n")            #Este código lo que hace es escribir un texto
    print(f"Se creo el archivo {nombre_archivo}\n")              #en el archivo creado
except FileExistsError as e:
    print(f"El archivo '{nombre_archivo}' ya existe")
    print(f"Detalle del error: {e}")
#2° nombre_archivo para que demuestre que el archivo ya existe
nombre_archivo = "Nombre_Archivo.txt"
try:
    with open(nombre_archivo, "x") as archivo: #La "x" crea si no existe el archivo (si existe => error)
        archivo.write("Se crea el archivo en modo exclusivo\n")
        archivo.write("Creando nombre del archivo\n")            #En este código al cambiar la "w" por las "x"
    print(f"Se creo el archivo {nombre_archivo}\n")              #te tira el error del que archivo ya existe
except FileExistsError as e:
    print(f"El archivo '{nombre_archivo}' ya existe")
    print(f"Detalle del error: {e}\n")

#Leer un archivo con metodos de read(), readline() o readlines().
print("---*** Leyendo un archivo ***---")

mi_nombre_archivo = "Mi_Archivo.txt"

#Leer un archivo usando el metodo readlines()
with open(mi_nombre_archivo, "r") as archivo:
    #print(archivo.readlines())  Lee todas las líneas del archivo y te lo muestra en forma de lista
    lineas = archivo.readlines()
    for linea in lineas:          #De esta forma lee el archivo recorriendo la lista con for
        print(linea)

#Lee el contenido del archivo usando read()
with open(mi_nombre_archivo, "r") as archivo:
    print(archivo.read()) #Lee el contenido del archivo completamente o de una sola vez

#Se anexa o se agrega información con "a", como se utiliza el metodo append()
print("---*** Anexar un archivo ***---")

nombre_archivo = "Nombre_Archivo.txt"

with open(nombre_archivo, "a") as archivo:
    archivo.write("Se anexa el archivo\n")
    archivo.write("Se ha anexado información en el archivo\n")

print(f"Se anexa información en el archivo: {nombre_archivo}\n")
