import numpy as np

class Banco:

    def __init__(self, pid, pnombre, pdni, ptipo_operation, pmonto, pfecha, pestado):
        self.id = pid
        self.nombre = pnombre
        self.dni = pdni
        self.tipo_operacion = ptipo_operation
        self.monto = pmonto
        self.fecha = pfecha
        self.estado = pestado

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Dni: {self.dni} | Operacion: {self.tipo_operacion} | Monto: ${self.monto} | Estado: {self.estado}"

def validar_numero(mensaje):
    while True:
        try:
            numero_int = int(input(mensaje))
            if numero_int < 0:
                print("El numero tiene que ser positivo.")
            else:
                return numero_int
        except ValueError:
            print("Error. Ingrese un número valido.")

def colallena(tope,fin_cola):
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

def ruta_importacion():
    return r"C:\Users\Parcial Banco\clientes.txt"

def ruta_excedente():
    return r"C:\Users\Parcial Banco\clientes_sin_turno.txt"

def ruta_historial():
    return r"C:\Users\Parcial Banco\historial_atenciones.txt"

def importar_cliente(tope, importado, fin_cola, cola_pendientes): #1
    if importado:
        print("Ya se importaron los clientes.")
        return importado, tope

    try:
        with open(ruta_importacion(), "r") as archivo:
            contador_encolar = 0
            contador_excedentes = 0
            for linea in archivo:

                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                if len(partes) != 6:
                    print(f"Linea incorrecta: {linea}")
                    break

                id,nombre,dni,tipo_operacion,monto,fecha = partes
                dni = int(dni)
                monto = float(monto)

                if colallena(tope, fin_cola):
                    with open(ruta_excedente(), "a") as archivo_cliente:
                        archivo_cliente.write(f"{id},{nombre},{dni},{tipo_operacion},{monto},{fecha}\n")
                        contador_excedentes += 1
                else:
                    cliente = Banco(id, nombre, dni, tipo_operacion, monto, fecha, "Pendiente")
                    tope = encolar(cola_pendientes, tope, cliente)
                    contador_encolar += 1

            if contador_excedentes > 0:
                print("La cola está completa")
            if contador_encolar > 0:
                print(f"Se importaron {contador_encolar} clientes.")

    except FileNotFoundError:
        print("No existe el archivo.")

    return True, tope

def atencion_cliente(tope, cola_pendientes): #2
    if colavacia(tope):
        print("La cola de los clientes está vacía.")
    else:
        cliente_atendido, tope = desencolar(cola_pendientes, tope)
        print(f"{cliente_atendido}")
        cliente_atendido.estado = "Atendido"
        cajero = input("Ingrese la observación: ")
        print(f"{cliente_atendido}")
        with open(ruta_historial(), "a") as archivo:
            archivo.write(f"{cliente_atendido} | Observación: {cajero}\n")

    return tope

def consultar_cola(tope, cola_pendientes): #3
    if colavacia(tope):
        print("La cola de los clientes está vacía.")
    else:
        print("Consulta cola actual: ")
        for i in range(tope):
            print(f"{i + 1}. {cola_pendientes[i]}")

def informar_monto(tope, cola_pendientes): #4
     if colavacia(tope):
         print("La cola de los clientes está vacía.")
     else:
         mayor = cola_pendientes[0].monto
         menor = cola_pendientes[0].monto
         pos_mayor = 0
         pos_menor = 0
         total = cola_pendientes[0].monto
         for i in range(1, tope):
            if cola_pendientes[i].monto > mayor:
                mayor = cola_pendientes[i].monto
                pos_mayor = i

            if cola_pendientes[i].monto < menor:
                menor = cola_pendientes[i].monto
                pos_menor = i

            total += cola_pendientes[i].monto

         print(f"El monto mayor:\n{cola_pendientes[pos_mayor]}\nEl monto menor:\n{cola_pendientes[pos_menor]}")
         print(f"El monto total: ${total}")

def iniciar_menu():
    salir = False
    importado = False
    tope = 0
    fin_cola = 10
    cola_pendientes = np.zeros(shape = (fin_cola), dtype = object)
    while not salir:
        opcion = mostrar_menu()
        salir, importado, tope = ejecutar_opciones(opcion, importado, tope, fin_cola, cola_pendientes)

def mostrar_menu():
    while True:
        print('''\nMenú:
    1. Importar clientes 
    2. Atender cliente
    3. Consultar cola actual
    4. Informe de montos
    5. Salir\n''')
        return validar_numero("Seleccione una opción: ")

def ejecutar_opciones(opcion, importado, tope, fin_cola, cola_pendientes):
    if opcion == 1:
        importado, tope = importar_cliente(tope, importado, fin_cola, cola_pendientes)
    elif opcion == 2:
        tope = atencion_cliente(tope, cola_pendientes)
    elif opcion == 3:
        consultar_cola(tope, cola_pendientes)
    elif opcion == 4:
        informar_monto(tope, cola_pendientes)
    elif opcion == 5:
        print("---*** Fin del Programa ***---")
        return True, importado, tope
    else:
        print("La opción es de (1-5)")
    return False, importado, tope

iniciar_menu()