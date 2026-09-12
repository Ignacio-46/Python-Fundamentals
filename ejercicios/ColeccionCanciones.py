#Consigna: Gestión de una colección de canciones
#Escribe un programa que gestione una lista de tus canciones favoritas.
#Cada canción en la lista debe tener un título, un género musical y una duración (en minutos).
#Los géneros musicales válidos son "Rock", "Pop", "Reggaeton".
#El programa debe mostrar un menú con las siguientes opciones:

#Agregar una nueva canción a la lista con su título, género y duración.
#Mostrar la lista de canciones, incluyendo títulos, géneros y duraciones.
#Mostrar las canciones de un género específico.
#Calcular la duración total de todas las canciones de la playlist.
#Encontrar la canción más corta.
#Identificar el género más popular dentro de las canciones cargadas en el sistema.
#Salir del programa.

canciones = []
generos = []
duracion = []

def menu ():
    print("Menú: ")
    eleccion = ("1. Agregar una nueva canción\n2. Mostrar la lista de la canciones\n3. Mostrar las canciones de un género especifico\n"
                "4. La duración total de la canciones\n5. La canción más corta\n"
                "6. El género más popular\n7. Salir\n")
    print(f"{eleccion}")

def agregar_canciones():
    while True:
        cancion = input("Ingrese el titulo de la canción: ").lower()
        if cancion.isnumeric():
            print("título Incorrecto.")
            continue
        cancion = str(cancion)
        break
    while True:
        genero = input("Ingrese el género musical (Rock, Pop, Reggaeton): ").lower()
        if genero == "rock":
            break
        elif genero == "pop":
            break
        elif genero == "reggaeton":
            break
        else:
            print("Género invalido.")
            continue
    while True:
        try:
            durante = float(input("Ingrese la duración de la canción (en minutos): "))
            canciones.append(cancion)
            generos.append(genero)
            duracion.append(durante)
            break
        except ValueError:
            print("Error. Ingresa un valor númerico\n")
    print("Canción agregada con éxito.\n")

def mostrar_canciones():
    for i in range(len(canciones)):
        print(f"Título: {canciones[i]}, Género: {generos[i]}, Duración: {duracion[i]} minutos.\n")

def genero_especifico():
    while True:
        especifico = input("Ingrese el género (Rock, Pop, Reggaeton): ").lower()
        if especifico in generos:
            for i in range(len(generos)):
                if generos[i] == especifico:
                    print(f"Título: {canciones[i]}, Duración: {duracion[i]} minutos.\n")
        else:
            print(f"No se encontró el género: {especifico} en la lista.\n")
        break

def duracion_total():
    suma = 0
    for i in range(len(duracion)):
        suma += duracion[i]
    print(f"La duración total de todas la canciones es de {suma} minutos.\n")

def cancion_mas_corta():
    menor = duracion[0]
    indice = 0
    for i in range(len(duracion)):
        if duracion[i] < menor:
            menor = duracion[i]
            indice = i
    print(f"La canción mas corta es '{canciones[indice]}' con una duración de {duracion[indice]} minutos.\n")

def genero_mas_popular():
    rock = 0
    pop = 0
    reggaeton = 0
    popular = None
    for i in range(len(generos)):
        if generos[i] == "rock":
            rock += 1
        if generos[i] == "pop":
            pop += 1
        if generos[i] == "reggaeton":
            reggaeton += 1

    if rock > pop and rock > reggaeton:
        popular = "rock"
    elif pop > rock and pop > reggaeton:
        popular = "pop"
    elif reggaeton > rock and reggaeton > pop:
        popular = "reggaeton"
    else:
        popular = "Empate entre géneros."

    print(f"El género más popular es: {popular}.\n")

while True:
    menu()
    opcion = input("Selecciona un opción: ")
    if not opcion.isnumeric():
        print("Opción Invalidad. Intente de nuevo.\n")
        continue
    opcion = int(opcion)
    if opcion == 1:
        agregar_canciones()
    elif opcion == 2:
        if canciones:
            mostrar_canciones()
        else:
            print("La lista esta vacía. Ingrese sus canciones.\n")
    elif opcion == 3:
        if canciones:
            genero_especifico()
        else:
            print("La lista esta vacía. Ingrese sus canciones.\n")
    elif opcion == 4:
        if canciones:
            duracion_total()
        else:
            print("La lista esta vacía. Ingrese sus canciones.\n")
    elif opcion == 5:
        if canciones:
            cancion_mas_corta()
        else:
            print("La lista esta vacía. Ingrese sus canciones.\n")
    elif opcion == 6:
        if canciones:
            genero_mas_popular()
        else:
            print("La lista esta vacía. Ingrese sus canciones.\n")
    elif opcion == 7:
            print("Saliendo del Programa\n")
            break
    else:
        print(f"Las opciones son de (1-7): {opcion}\n")
