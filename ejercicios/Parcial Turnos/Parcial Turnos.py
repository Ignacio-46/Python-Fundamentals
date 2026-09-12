#Modelo segundo Parcial de Algoritmo y Programacion
#Roldan Ignacio C1

import numpy as np

class Pacientes:

    def __init__(self, pid, pnombre, phora, pestado, pedad, pfecha):
        self.id = pid
        self.nombre = pnombre
        self.hora = phora
        self.estado = pestado
        self.edad = pedad
        self.fecha = pfecha

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Hora: {self.hora}hs | Estado: {self.estado} | Edad: {self.edad} años | Fecha: {self.fecha}'

def validar_numero(mensaje):
    while True:
        try:
            numero_int = int(input(mensaje))
            if numero_int <= 0:
                print("El valor debe ser positivo")
            else:
                return numero_int
        except ValueError:
            print("Error. Ingrese un número valido")

def colallena(tope, fin_cola):
    return tope == fin_cola - 1

def colavacia(tope):
    return tope == 0

def encolar(cola, tope, nuevo):
    cola[tope] = nuevo
    tope += 1
    return tope

def desencolar(tope, cola):
    if tope == 0:
        return None, tope

    turno_saliente = cola[0]
    for x in range(tope - 1):
        cola[x] = cola[x + 1]
    cola[tope - 1] = None
    tope -= 1
    return turno_saliente, tope

def rutas_turnos():
    return r"C:\Users\Parcial Turnos\turnos.txt"

def rutas_sin_turnos():
    return r"C:\Users\Parcial Turnos\sin_turnos.txt"

def importar_turnos(importado, tope_atencion, tope_clinica, fin_cola, cola_atencion, cola_clinica):
    if importado:
        print(f"Se importaron todos los turnos.")
        return importado, tope_atencion, tope_clinica

    try:
        with open(rutas_turnos(), "r") as archivo:
            importa = 0
            excedente = 0
            for linea in archivo:

                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                if len(partes) != 6:
                    print(f"Línea inválida: {linea}")
                    continue

                id, nombre, hora, estado, edad, fecha = partes
                edad = int(edad)
                turno = Pacientes(id, nombre, hora, "Pendiente", edad, fecha)

                if edad < 13:# ATENCIÓN
                    if not colallena(tope_atencion, fin_cola):
                        tope_atencion = encolar(cola_atencion, tope_atencion, turno)
                        importa += 1
                    else:
                        with open(rutas_sin_turnos(), "a") as archivo_atencion:
                            archivo_atencion.write(linea + "\n")
                            excedente += 1
                else:# CLÍNICA
                    if not colallena(tope_clinica, fin_cola):
                        tope_clinica = encolar(cola_clinica, tope_clinica, turno)
                        importa += 1
                    else:
                        with open(rutas_sin_turnos(), "a") as archivo_clinica:
                            archivo_clinica.write(linea + "\n")
                            excedente += 1

            if importa > 0:
                print(f"Se importaron {importa} turnos del archivo.")
            if excedente > 0:
                print(f"Cola excedida. Se importaron {excedente} turnos en historial sin turnos.")

    except FileNotFoundError:
        print("El archivo no existe")

    return True, tope_atencion, tope_clinica

def atender_turnos(tope_atencion, tope_clinica, cola_atencion, cola_clinica):
    if colavacia(tope_atencion) and colavacia(tope_clinica):
        print("La cola de turnos está vacía")
        return tope_atencion, tope_clinica

    while True:
        paciente = input("Ingrese A (Atención) o C (Clínica Médica): ").strip().upper()
        if paciente == "A":
            turno_atendido, tope_atencion = desencolar(tope_atencion, cola_atencion)
            print(f"{turno_atendido}")
            turno_atendido.estado = "Tomado"
            print(turno_atendido)
            break
        elif paciente == "C":
            turno_atendido, tope_clinica = desencolar(tope_clinica, cola_clinica)
            print(f"{turno_atendido}")
            turno_atendido.estado = "Tomado"
            print(turno_atendido)
            break
        else:
            print("Error. Ingrese A o C")

    return tope_atencion, tope_clinica

def Informar_turnos(tope_atencion, tope_clinica, cola_atencion, cola_clinica):
    if colavacia(tope_atencion) and colavacia(tope_clinica):
        print("La cola de turnos está vacía")
        return
    else:
        print("\nAtención:")
        for i in range(tope_atencion):
            print(f"{i + 1}. {cola_atencion[i]}")

        print("\nClínica:")
        for i in range(tope_clinica):
            print(f"{i + 1}. {cola_clinica[i]}")

def iniciar_menu():
    salir = False
    importado = False
    tope_atencion = 0
    tope_clinica = 0
    fin_cola = 10
    cola_atencion = np.zeros(shape = fin_cola, dtype=object)
    cola_clinica = np.zeros(shape = fin_cola, dtype=object)
    while not salir:
        opcion = mostrar_menu()
        salir, importado, tope_atencion, tope_clinica = ejecutar_opciones(opcion, importado, tope_atencion, tope_clinica, fin_cola, cola_atencion, cola_clinica)

def mostrar_menu():
    print("""
1. Importar Turnos
2. Atender Turnos
3. Informar Pacientes
4. Salir
""")
    return validar_numero("Seleccione la opción: ")

def ejecutar_opciones(opcion, importado, tope_atencion, tope_clinica, fin_cola, cola_atencion, cola_clinica):
    if opcion == 1:
        importado, tope_atencion, tope_clinica = importar_turnos(importado, tope_atencion, tope_clinica, fin_cola, cola_atencion, cola_clinica)
    elif opcion == 2:
        tope_atencion, tope_clinica = atender_turnos(tope_atencion, tope_clinica, cola_atencion, cola_clinica)
    elif opcion == 3:
        Informar_turnos(tope_atencion, tope_clinica, cola_atencion, cola_clinica)
    elif opcion == 4:
        print("Fin del programa")
        return True, importado, tope_atencion, tope_clinica
    else:
        print("Opción inválida")
    return False, importado, tope_atencion, tope_clinica

iniciar_menu()
