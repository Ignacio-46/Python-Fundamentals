# Ejercicio 3: Control de Flota de Camiones 🚛
# Este es un poco más complejo en la lógica de "Carga", similar al stock pero con un límite
# máximo (capacidad).
# Datos por camión:
# ● Patente (String).
# ● Tipo de Carga (S = Seca, R = Refrigerada, P = Peligrosa).
# ● Kilometraje (Entero positivo).
# ● Carga Actual (Toneladas, decimal positivo).
# Menú de opciones:
# 1. Ingresar Camión: Pedir datos.
# 2. Mostrar Flota: Listar todos los camiones.
# 3. Promedio de Kilometraje: Calcular el promedio de km de toda la flota.
# 4. Camión más Nuevo: Asumiendo que menos kilometraje es más nuevo, mostrar el de menor km.
# 5. Alerta de Mantenimiento: Listar camiones que superen los 100,000 km.
# 6. Cargar Camión: Elegir un camión y aumentar su "Carga Actual".
# ○ Desafío extra: Preguntar antes cuál es la capacidad máxima y validar que la nueva
# carga no la supere.
# 7. Salir.

patentes = []
tipos = []
kilometros = []
cargas = []

def menu():
    print("""Menú:
    1. Ingresar camión
    2. Mostrar flota
    3. Promedio kilometraje
    4. Camión mas nuevo
    5. Mantenimiento
    6. Carga actual
    7. Eliminar camión
    8. Salir\n""")

def validar_numero(mensaje, tipo):
    while True:
        try:
            if tipo == 1:
                valor_int = int(input(mensaje))
                return valor_int
            if tipo == 2:
                valor_float = float(input(mensaje))
                return valor_float
        except ValueError:
            print("Debe ingresar un valor numérico.")

def agregar_camion():
    #Patente(String).
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    while True:
        nombre = input("Ingrese la patente del camión: ").upper()
        if nombre == "":
            print("Error. Ingrese la patente.")
            continue

        valido = True
        for letra in nombre:
            if letra not in letras:
                valido = False
                break

        if valido:
            patentes.append(nombre)
            break
        else:
            print("Error. No se permite símbolos.")
            continue

    #Tipo de Carga (S = Seca, R = Refrigerada, P = Peligrosa).
    categoria = "SRP"
    while True:
        seccion = input("Ingrese el tipo de carga: ").upper()
        if seccion == "":
            print("Error. Ingrese la carga.")

        valido = True
        for letra in seccion:
            if letra not in categoria:
                valido = False
                break

        if valido:
            if seccion == "S":
                reseccion = "Seca"
            elif seccion == "R":
                reseccion = "Refrigerada"
            else:
                reseccion = "Peligrosa"
            tipos.append(reseccion)
            break
        if not valido:
            print("Error de carga. Ingrese solo S,R o P")
            continue

    #Kilometraje (Entero positivo).
    while True:
        kilometro = validar_numero("Ingrese el kilometraje: ",1)
        if kilometro < 0:
            print("Error. Los kilómetros tienen que ser positivo.")
            continue
        else:
            kilometros.append(kilometro)
            break

    #Carga Actual (Toneladas, decimal positivo).
    while True:
        carga = validar_numero("Ingrese la carga: ",2)
        if carga < 0:
            print("Error. La carga tiene que ser positiva.")
            continue
        else:
            cargas.append(carga)
            break

    print("\n---*** Se registró el camión ***---\n")

def mostrar_camion():
    for i in range(len(patentes)):
        print(f"{i + 1}. Camión: {patentes[i]}, Tipo: {tipos[i]}, Kilometraje: {kilometros[i]} km, Carga: {cargas[i]} toneladas.")
    print("\n")

def promedio_km():
    suma = 0
    for kilo in kilometros:
        suma += kilo
    promedio = suma/len(kilometros)
    print(f"El promedio de todo el kilometraje es: {promedio} km.")
    print("\n")

def mas_nuevo():
    menor = kilometros[0]
    indice = 0
    for i in range(len(kilometros)):
        if kilometros[i] < menor:
            menor = kilometros[i]
            indice = i
    print(f"El camión mas nuevo con menos kilometraje es: '{patentes[indice]}' con '{kilometros[indice]}' km")
    print(f"\n")

def mantenimiento():
    mantener = False
    for i in range(len(kilometros)):
        if kilometros[i] > 100000:
            mantener = True
            print(f"Los camiones registrado en mantenímiento:")
            print(f"{i + 1}. Camión: {patentes[i]}, Tipo: {tipos[i]}, Kilometraje: {kilometros[i]} km, Carga: {cargas[i]} toneladas.\n")

    if not mantener:
        print("No se ha registrado un camión en mantenímiento\n")

def carga_actual():
    mostrar_camion()
    # Pedimos el índice (el número de la izquierda que mostraste en la lista)
    while True:
        indice_usuario = validar_numero("Ingrese el indice del camión para aumentar la carga: ", 1)
        # Ajustamos porque el usuario ve 1, pero las listas empiezan en 0
        indice = indice_usuario - 1
        if 0 <= indice < len(tipos): # Validamos que el índice exista
            aumento = validar_numero("Ingresar aumento: ", 2)
            if aumento > 0:
                cargas[indice] += aumento
                print(f"Se aumentó la carga del camión '{patentes[indice]}'.\n")
                break
            else:
                print("La carga debe ser positiva.")
                continue
        else:
            print("Error.La carga no existe.")
            continue

def eliminar_camion():
    mostrar_camion()
    # Pedimos el índice (el número de la izquierda que mostraste en la lista)
    while True:
        indice_usuario = validar_numero("Ingrese el indice para eliminar camión : ", 1)
        # Ajustamos porque el usuario ve 1, pero las listas empiezan en 0
        indice = indice_usuario - 1
        if 0 <= indice < len(tipos):  # Validamos que el índice exista
            patentes.pop(indice)
            tipos.pop(indice)
            kilometros.pop(indice)
            cargas.pop(indice)
            print(f"El camión fue eliminado.\n")
            break
        else:
            print("Error. No existe INDICE.")
            continue

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_camion()
        elif opcion == 2:
            if patentes:
                mostrar_camion()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 3:
            if patentes:
                promedio_km()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 4:
            if patentes:
                mas_nuevo()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 5:
            if patentes:
                mantenimiento()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 6:
            if patentes:
                carga_actual()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 7:
            if patentes:
                eliminar_camion()
            else:
                print("Lista vacía. Ingrese sus patentes.\n")
        elif opcion == 8:
            print("Saliendo del programa.\n")
            break
        else:
            print("La opción es entre (1-8).\n")
            continue
    except ValueError:
        print(f"Opción invalida.\n")
        continue
