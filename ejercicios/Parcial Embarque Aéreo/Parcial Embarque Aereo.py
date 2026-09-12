import numpy as np

class Pasajeros:

    def __init__(self, pid, pnombre, ppasaporte, pdestino, pasiento, pequipaje_kg, pfecha, pestado):
        self.id = pid
        self.nombre = pnombre #(str)
        self.pasaporte = ppasaporte #(str)
        self.destino = pdestino #(str)
        self.asiento = pasiento #(str)
        self.equipaje_kg = pequipaje_kg #(float)
        self.fecha = pfecha
        self.estado = pestado #(str)

    def __str__(self):
        return f"ID: {self.id}. [Nombre: {self.nombre} | Pasaporte: {self.pasaporte} | Destino: {self.destino} | Asiento: {self.asiento} | Equipaje: {self.equipaje_kg}kg | Fecha: {self.fecha} | Estado: {self.estado}]"

def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Valor invalido. Tiene que ser positivo.")
            else:
                return numero
        except ValueError:
            print("Error. Tiene que ingresar un número.")

def colallena(tope, fin_cola):
    return tope == fin_cola

def colavacia(tope):
    return tope == 0

def encolar(cola, tope, nuevo):
    cola[tope] = nuevo
    tope += 1
    return tope

def desencolar(cola, tope):
    if tope == 0:
        return None, tope

    atencion_saliente = cola[0]
    for x in range(tope - 1):
        cola[x] = cola[x + 1]
    cola[tope - 1] = None
    tope -= 1
    return atencion_saliente, tope

def rutas_pasajeros():
    return r"C:\Users\Parcial Embarque Aéreo\Pasajeros.txt"

def rutas_Historial_embarques():
    return r"C:\Users\Parcial Embarque Aéreo\historial_embarques.txt"

def rutas_pasajeros_sin_lugar():
    return r"C:\Users\Parcial Embarque Aéreo\pasajeros_sin_lugar.txt"

def importar_pasajeros(importado, tope, fin_cola, cola_pendientes):  # 1
    if importado:
        print("Se importaron todo los pasajeros.")
        return importado, tope

    try:
        with open(rutas_pasajeros(), "r") as archivo:
            excedente = 0
            importa = 0
            for linea in archivo:

                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                if len(partes) != 7:
                    print(f"Linea invalida: {linea}")
                    continue

                id, nombre, pasaporte, destino, asiento, equipaje_kg, fecha = partes
                try:
                    equipaje_kg = float(equipaje_kg)
                except ValueError:
                    print(f"Equipaje invalido en linea: {linea}")
                    continue

                if colallena(tope, fin_cola):
                    with open(rutas_pasajeros_sin_lugar(), "a") as archivo:
                        archivo.write(f"{id}, {nombre}, {pasaporte}, {destino}, {asiento}, {equipaje_kg}, {fecha}" + "\n")
                        excedente += 1
                else:
                    pasajero = Pasajeros(id, nombre, pasaporte, destino, asiento, equipaje_kg, fecha, "Pendiente")
                    tope = encolar(cola_pendientes, tope, pasajero)
                    importa += 1

            if excedente > 0:
                print(f"La cola alcanzó su capacidad maxima: {excedente} pasajeros.")
            if importa > 0:
                print(f"Se importaron {importa} pasajeros.")

    except FileNotFoundError:
        print("El archivo no existe.")

    return True, tope

def embarcar_pasajeros(tope, cola_pendientes):  # 2
    if colavacia(tope):
        print("La cola de pasajeros está vaciá.")
    else:
        pasajero_atendido, tope = desencolar(cola_pendientes, tope)
        print(f"Pasajero en espera:\n{pasajero_atendido}")
        while True:
            embarcar_pasajero = input("Marcár pasajero con 'embarcado': ")
            if embarcar_pasajero == "embarcado":
                pasajero_atendido.estado = embarcar_pasajero
                print(f"Pasajero Embarcado:\n{pasajero_atendido}")
                with open(rutas_Historial_embarques(), "a") as archivo:
                    archivo.write(f"{pasajero_atendido}\n")
                break
            else:
                print("Marque bien por favor.")
                continue

    return tope

def consulta_pendientes(tope, cola_pendientes): #3
    if colavacia(tope):
        print("La cola de pasajeros está vaciá.")
    else:
        print(f"Consulta de pasajeros en espera: ")
        for i in range(tope):
            print(f"{i + 1}. {cola_pendientes[i]}.")

def informar_equipaje(tope, cola_pendientes): #4
    if colavacia(tope):
        print("La cola de pasajeros está vaciá.")
    else:
        peso_pesado = cola_pendientes[0].equipaje_kg
        peso_liviano = cola_pendientes[0].equipaje_kg
        total_equipaje = cola_pendientes[0].equipaje_kg
        pos_pesado = 0
        pos_liviano = 0
        for i in range(1, tope):

            if cola_pendientes[i].equipaje_kg > peso_pesado:
                peso_pesado = cola_pendientes[i].equipaje_kg
                pos_pesado = i

            if cola_pendientes[i].equipaje_kg < peso_liviano:
                peso_liviano = cola_pendientes[i].equipaje_kg
                pos_liviano = i

            total_equipaje += cola_pendientes[i].equipaje_kg

        print(f"Equipaje Pesado:\n{cola_pendientes[pos_pesado]}")
        print(f"Equipaje Liviano:\n{cola_pendientes[pos_liviano]}")
        print(f"Total de equipajes: {total_equipaje}kg")

def iniciar_menu():
    salir = False
    importado = False
    tope = 0
    fin_cola = 10
    cola_pendientes = np.zeros(shape = 10, dtype = object)
    while not salir:
        opcion = mostrar_menu()
        salir, importado, tope = ejecutar_opciones(opcion, importado, tope, fin_cola, cola_pendientes)

def mostrar_menu():
    while True:
        print(f'''\nMenú: 
    1. Importar pasajeros
    2. Embarcar pasajeros
    3. Consultar pasajeros pendientes
    4. Informar equipaje
    5. Salir\n''')
        return validar_numero("Seleccione un opción: ")

def ejecutar_opciones(opcion, importado, tope, fin_cola, cola_pendientes):
    if opcion == 1:
        importado, tope = importar_pasajeros(importado, tope, fin_cola, cola_pendientes)
    elif opcion == 2:
        tope = embarcar_pasajeros(tope, cola_pendientes)
    elif opcion == 3:
        consulta_pendientes(tope, cola_pendientes)
    elif opcion == 4:
        informar_equipaje(tope, cola_pendientes)
    elif opcion == 5:
        print("Saliendo...!!")
        return True, importado, tope
    else:
        print("La opción es de (1-5).")
    return False, importado, tope

iniciar_menu()
