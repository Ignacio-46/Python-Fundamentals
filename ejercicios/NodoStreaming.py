# Examen Parcial: Gestión de Nodos de Streaming
# Eres el desarrollador backend encargado de monitorear la infraestructura de una nueva plataforma de streaming de anime.
# Necesitas registrar y analizar el estado de 4 servidores regionales para balancear la carga de tráfico.
# 1. TDA tdaServidorStreaming: Deberás completar la clase tdaServidorStreaming. Atributos:
# - id_servidor (int): Número de identificación (ej. 1, 2, 3...).
# - region (str): Código de la región del servidor.
# - trafico_actual_tb (float): Terabytes de tráfico siendo procesados.
# - capacidad_max_tb (float): Capacidad máxima del servidor en Terabytes.

# class tdaServidorStreaming:
#     def __init__(self, pid_servidor, pregion, ptrafico_actual, pcapacidad_max):
#         """ COMPLETAR LÓGICA AQUÍ """
#         pass
#
#     def calcular_porcentaje_carga(self):
#         """ COMPLETAR LÓGICA AQUÍ: Debe retornar el % de uso del servidor
#             (trafico_actual * 100 / capacidad_max) """
#         pass
#
#     def __str__(self):
#         return f"Server {self.id_servidor} [{self.region}] -> Tráfico: {self.trafico_actual_tb}/{self.capacidad_max_tb} TB | Carga: {self.calcular_porcentaje_carga():.2f}%"

#2. Gestionar una lista de 4 servidores. Implementar un menú:
# 1- Registrar Nodos de Servidor:
#   * Solicitar los datos para los 4 servidores.
#   * Validación 1 (String): La región DEBE ser estrictamente uno de los siguientes
#     códigos: "SA" (Sudamérica), "NA" (Norteamérica), "EU" (Europa) o "AS" (Asia).
#   * Validación 2 (Float): La capacidad máxima debe ser mayor a 0 y el tráfico actual
#     no puede ser negativo ni superar la capacidad máxima declarada para ese servidor.
#   * ¡Importante!: Si el usuario vuelve a elegir esta opción, la lista debe limpiarse
#     para no acumular más de 4 servidores.
# 2- Estado de la Red:
#   * Restricción: Solo accesible si los 4 servidores ya fueron cargados.
#   * Mostrar la información de los 4 servidores usando el método __str__.
# 3- Alerta de Saturación (Mayor Carga):
#   * Restricción: Solo accesible si los 4 servidores ya fueron cargados.
#   * Determinar qué servidor tiene el mayor porcentaje de carga utilizando el
#     método calcular_porcentaje_carga(). Mostrar los datos de ese servidor.
# 4- Salir: Finaliza el programa.

class tdaServidorStreaming:
     def __init__(self, pid_servidor, pregion, ptrafico_actual, pcapacidad_max):
         self.id_servidor = pid_servidor
         self.region = pregion
         self.trafico_actual = ptrafico_actual
         self.capacidad_max = pcapacidad_max

     def calcular_porcentaje_carga(self):
         return self.trafico_actual * 100 / self.capacidad_max

     def __str__(self):
         return f"Server {self.id_servidor} [{self.region}] -> Tráfico: {self.trafico_actual}/{self.capacidad_max} TB | Carga: {self.calcular_porcentaje_carga():.2f}%"

def validar_numero(mensaje, tipo):
    while True:
        try:
            if tipo == 1:
                numero_int = int(input(mensaje))
                if numero_int <= 0:
                    print("Error. Debe ingresar un número positivo")
                else:
                        return numero_int
            if tipo == 2:
                numero_float = float(input(mensaje))
                if numero_float <= 0:
                    print("Error. Debe ingresar un número positivo")
                else:
                    return numero_float
            if tipo == 3:
                numero_float = float(input(mensaje))
                if numero_float < 0:
                    print("Error. Debe ingresar un número positivo")
                else:
                    return numero_float
        except ValueError:
            print("Error. Debe ingresar un numero")

def validar_region(mensaje):
    while True:
        region = input(mensaje).upper()
        if region == "":
            print("Error. Ingrese el código")
            continue
        if region in ["SA","NA","EU","AS"]:
            return region
        else:
            print("Debe ingresar los códigos correctos (SA,NA,EU,AS)")

def registrar_nodo(lista_servidores):
    print("---*** Registro de los Servidores ***---\n")
    for i in range(len(lista_servidores)):
        id_servidor = validar_numero("Identificación del id: ",1)
        region = validar_region("Ingrese los códigos 'SA'(Sudamérica),'NA'(Norteamérica),'EU'(Europa),'AS'(Asia): ")
        capacidad_max = validar_numero("Ingrese la capacidad maxima: ",2)
        while True:
            capacidad_actual = validar_numero("Ingrese su capacidad actual: ",3)
            if capacidad_actual > capacidad_max:
                print("La capacidad actual no puede superar la capacidad maxima")
            else:
                break
        servidores = tdaServidorStreaming(id_servidor, region, capacidad_actual, capacidad_max)
        lista_servidores[i] = servidores

    print("\n---*** Carga Completa ***---")

def estado_red(lista_servidores):
    for servidor in lista_servidores:
        print(servidor)

def alerta_saturacion(lista_servidores):
    carga = lista_servidores[0]
    mayor_porcentaje_carga = lista_servidores[0].calcular_porcentaje_carga()
    for i in range (1,len(lista_servidores)):
        if lista_servidores[i].calcular_porcentaje_carga() > mayor_porcentaje_carga:
            mayor_porcentaje_carga = lista_servidores[i].calcular_porcentaje_carga()
            carga = lista_servidores[i]
    return carga

def iniciar_menu():
    salir = False
    lista_servidores = [0]*4
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_opciones(lista_servidores, opcion)

def mostrar_menu():
    while True:
        print('''\nMenú:
        1. Registrar los nodos
        2. Estado de red 
        3. Alerta de saturación (Mayor carga)
        4. Salir del programa\n''')
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción invalida. Ingrese (1-4)")

def ejecutar_opciones(lista_servidores, opcion):
    if opcion == 1:
        registrar_nodo(lista_servidores)
    elif opcion == 2:
        if lista_servidores[0] != 0:
            estado_red(lista_servidores)
        else:
            print("No está los 4 servidores registrados.")
    elif opcion == 3:
        if lista_servidores[0] != 0:
            carga = alerta_saturacion(lista_servidores)
            print(f"{carga}")
        else:
            print("No está los 4 servidores registrados.")
    elif opcion == 4:
        print("---*** Fin del Programa ***---")
        return True
    else:
        print(f"Error. Ingrese un número valido: {opcion}")
    return False

iniciar_menu()
