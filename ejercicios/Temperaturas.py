# EJERCICIO: Sistema de Registro y Análisis de Temperaturas Diarias
# El programa debe gestionar temperaturas registradas a lo largo de varios días.
# MENÚ DEL PROGRAMA
# 1. Registrar un nuevo día:
#  Día (string o número, lo que vos quieras)
#  Temperatura máxima (float, puede ser negativa)
#  Temperatura mínima (float, puede ser negativa)
#  Estado climático (carácter):
#  S = Soleado
#  N = Nublado
#  L = Lluvioso
#  V = Ventoso
# 2. Mostrar todos los registros cargados: Día – Temp Max – Temp Min – Estado
# 3. Mostrar la temperatura más alta registrada. Debe mostrar todos los datos del día que tuvo la máxima temperatura máxima.
# 4. Mostrar la temperatura más baja registrada. Debe mostrar todos los datos del día con la mínima temperatura mínima.
# 5. Calcular el promedio de temperaturas de un estado climático. El usuario ingresa S/N/L/V.
# 6. Listar días fríos (cuando la temperatura mínima sea ≤ 5° C). Mostrar todos sus datos.
# 7. Modificar la temperatura de un día. Mostrar lista numerada. Seleccionar día por índice. Ingresar nueva temp máxima y mínima
# 8. Salir

dias = []
minimos = []
maximos = []
climaticos = []

def menu():
    print("""Menú:
    1. Agregar días
    2. Mostrar días
    3. Temperatura Máxima
    4. Temperatura Minimo
    5. Promedio de Temperaturas
    6. Lista de días frío
    7. Modificar temperatura
    8. Salir\n""")

def validar_numeros(mensaje, tipo):
    while True:
        try:
            if tipo == 1:
                valor_int = int(input(mensaje))
                return valor_int
            if tipo == 2:
                valor_float = float(input(mensaje))
                return  valor_float
        except ValueError:
            print("Debe ingresar un valor numérico.")

def agregar_dias():
    while True:
        numero1 = validar_numeros("Ingrese el día: ",1)
        if numero1 <= 0:
            print("Error. Los dias tienen que ser positiva.")
            continue
        else:
            dias.append(numero1)
            break

    while True:
        numero2 = validar_numeros("Ingrese la temperatura máxima: ",2)
        if numero2 == "":
            print("Error. Error. Ingrese la temperatura.")
            continue
        else:
            maximos.append(numero2)
            break

    while True:
        numero3 = validar_numeros("Ingrese la temperatura minima: ",2)
        if numero3 == "":
            print("Error. Ingrese la temperatura.")
            continue
        else:
            minimos.append(numero3)
            break

    categoria = "SNLV"
    while True:
        clima = input("Ingrese el clima S(Soleado), N(Nubloso), L(Lluvioso), V(Ventoso): ").upper()
        if clima == "":
            print("Error. Ingrese el clima.")
            continue

        valido = True
        for letra in clima:
            if letra not in categoria:
                valido = False
                break

        if clima == "S":
            reclima = "Soleado"
        elif clima == "N":
            reclima = "Nublado"
        elif clima == "L":
            reclima = "Lluvioso"
        else:
            reclima = "Ventoso"

        if valido:
            climaticos.append(reclima)
            break
        if not valido:
            print("No existe tal clima. Seleccione S,N,L o V.\n")
            continue

    print("\n---*** se registró el día en la lista ***---\n")

def mostrar_dias():
    for i in range(len(dias)):
        print(f"{i + 1}. Días: {dias[i]}, Temperatura Max: {maximos[i]}°C, Temperatura Min: {minimos[i]}°C, Estado: {climaticos[i]}")
    print("\n")

def mas_baja():
    menor = minimos[0]
    indice = 0
    for i in range(len(minimos)):
        if minimos[i] < menor:
            menor = minimos[i]
            indice = i
    print(f"La Temperatura mas baja es '{menor}°C' en el día '{dias[indice]}', Estado: {climaticos[indice]}.\n")

def mas_alta():
    mayor = maximos[0]
    indice = 0
    for i in range(len(maximos)):
        if maximos[i] > mayor:
            mayor = maximos[i]
            indice = i
    print(f"La Temperatura mas alta es '{mayor}°C' en el día '{dias[indice]}', Estado: {climaticos[indice]}.\n")

def promedio_temp():
    mostrar_dias()
    categoria = "SNLV"
    while True:
        clima = input("Ingrese el clima S(Soleado), N(Nubloso), L(Lluvioso), V(Ventoso): ").upper().strip()
        if clima == "":
            print("Error. Ingrese el clima.")
            continue

        if clima not in categoria:
            print("No existe tal clima. Seleccione S,N,L o V.\n")
            continue

        total = 0
        cantidad = 0
        for i in range(len(climaticos)):
            if climaticos[i] == clima:
                suma = (maximos[i] + minimos[i])/2
                total += suma
                cantidad += 1

        if cantidad == 0:
            print("El estado existe pero no se ha registrado temperaturas.")
            continue

        promedio = total/cantidad

        if clima == "S":
           reclima = "Soleado"
        elif clima == "N":
           reclima = "Nublado"
        elif clima == "L":
           reclima = "Lluvioso"
        else:
           reclima = "Ventoso"

        print(f"El promedio de las temperaturas es: '{promedio}°C' del estado '{reclima}'.")
        break

def dias_frio():
    frio = False
    for i in range(len(minimos)):
        if minimos[i] <= 5:
            frio = True
            print(f"El día mas frío es el 'dia {dias[i]}', con una temperatura Min: '{minimos[i]}°C', Estado: {climaticos[i]}.")
    print("\n")

    if not frio:
        print(f"No se ha registrado los dias mas frío menos a 5°C.\n")

def modificar_dia():
    mostrar_dias()
    while True:
        indice_usuario = validar_numeros("Ingrese el indice para modificar las temperaturas: ",1)
        indice = indice_usuario -1
        if 0 <= indice < len(climaticos):
            minimo = validar_numeros("Ingrese la temperatura minima: ",2)
            minimos[indice] = minimo
            maxima = validar_numeros("Ingrese la temperatura maxima: ",2)
            maximos[indice] = maxima
            print(f"Las Temperatura min y max del indice '{indice + 1}' fueron modificadas.\n")
            break
        else:
            print("No existe INDICE.")
            continue

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_dias()
        elif opcion == 2:
            if dias:
                mostrar_dias()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 3:
            if dias:
                mas_alta()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 4:
            if dias:
                mas_baja()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 5:
            if dias:
                promedio_temp()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 6:
            if dias:
                dias_frio()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 7:
            if dias:
                modificar_dia()
            else:
                print("Lista vacía. Registre los dias.\n")
        elif opcion == 8:
            print("Fin del Programa.\n")
            break
        else:
            print("La opción es entre (1-8).\n")
            continue
    except ValueError:
        print("Opción Invalida. Ingrese un valor numérico.\n")
        continue












