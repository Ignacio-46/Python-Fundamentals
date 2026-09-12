# Parcial: Gestión de Datos Meteorológicos
# 1. Contexto del Problema
# Como desarrollador en el Servicio Meteorológico Nacional, se te ha encomendado la creación de un sistema para registrar y analizar el clima
# de una semana laboral (5 días). El sistema debe permitir la carga de datos, el procesamiento estadístico
# y la generación de reportes mediante el uso de Programación Orientada a Objetos (TDA) y estructuras de datos lineales.
# 2. Definición del TDA: tdaRegistroDiario
# Atributos:
# día (int): Número del día (1 para lunes, 2 para martes, etc.).
# temp_max (float): Temperatura máxima registrada.
# temp_min (float): Temperatura mínima registrada.
# precipitación (float): Milímetros (mm) de lluvia (debe ser $\ge 0 $).
# Plantilla Base:
# class tdaRegistroDiario:
#     def __init__(self, dia, ptemp_max, ptemp_min, precipitacion):
#         self.dia = dia
#         self.temp_max = ptemp_max
#         self.temp_min = ptemp_min
#         self.precipitacion = precipitacion
# 3. Requerimientos del Programa Principal
# El programa deberá gestionar una lista llamada lis_registro_diario, inicializada para contener los 5 objetos de la semana.
# Debes implementar un menú de opciones con las siguientes funcionalidades:
# 1. Cargar Registros: * Solicitar al usuario los datos de los 5 días de la semana.
#    Validación: Utilizar bloques try-except para capturar errores de entrada (ej. ingresar texto en lugar de números).
#    Asegurar que la precipitación no sea negativa.
# 2. Mostrar Registros: * Listar de forma prolija los datos de todos los días cargados.
# 3. Mayor Amplitud Térmica: * Calcular y mostrar el día con la mayor diferencia entre la temperatura máxima y mínima
#    ($\Delta T = T_{max} - T_{min}$)
# 4. Estadísticas de Precipitación: * Calcular y mostrar la suma total de lluvia caída en la semana y el promedio diario.
# 5. Salir: * Finalizar la ejecución del programa.

class tdaRegistroDiario:
     def __init__(self, dia, temp_max, temp_min, precipitacion):
         self.dia = dia
         self.temp_max = temp_max
         self.temp_min = temp_min
         self.precipitacion = precipitacion

     def __str__(self):
         return f"Día: {self.dia} -> Temp Max: {self.temp_max}° | Temp Min: {self.temp_min}° | Precipitación: {self.precipitacion} mm."

def validacion_numero(mensaje):
     while True:
         try:
             numero_float = float(input(mensaje))
             if numero_float < 0:
                 print("Error. Debe ser un número positivo.")
             else:
                 return numero_float
         except ValueError:
             print("Error. Deber ingresar un número.")

def registrar_carga(lis_registro_diario):
     print("\n---*** Carga Inicial ***---\n")
     for i in range(len(lis_registro_diario)):
         print(f"Día: {i + 1}")
         temp_max = validacion_numero("Ingrese la temperatura maxima: ")
         temp_min = validacion_numero("Ingrese la temperatura minima: ")
         precipitacion = validacion_numero("Ingrese la precipitación: ")
         carga = tdaRegistroDiario(i+1, temp_max, temp_min, precipitacion)
         lis_registro_diario[i] = carga
     print("\n---*** Carga Completa ***---")

def mostrar_carga(lis_registro_diario):
    for carga in lis_registro_diario:
         print(carga)

def diferencia_amplitud(temperatura):
    diferencia = temperatura.temp_max - temperatura.temp_min
    return diferencia

def mayor_amplitud_termica(lis_registro_diario):
    amplitud = lis_registro_diario[0].temp_max - lis_registro_diario[0].temp_min
    dia = lis_registro_diario[0]
    for i in range(1,len(lis_registro_diario)):
        if diferencia_amplitud(lis_registro_diario[i]) > amplitud:
            amplitud = diferencia_amplitud(lis_registro_diario[i])
            dia = lis_registro_diario[i]
    return dia, amplitud

def total_promedio_precipitacion(lis_registro_diario):
     total = 0
     for i in range(len(lis_registro_diario)):
        total += lis_registro_diario[i].precipitacion
     promedio = total/len(lis_registro_diario)
     return total, promedio

def iniciar_menu():
     salir = False
     lis_registro_diario = [0]*5
     while not salir:
         opcion = mostrar_menu()
         salir = ejecutar_opciones(opcion,lis_registro_diario)

def mostrar_menu():
     while True:
         print('''\nMenú:
    1. Registrar carga del día
    2. Mostrar carga del día
    3. Mayor Amplitud Térmica
    4. Estadística precipitación
    5. Salir del programa\n''')
         try:
            return int(input("Seleccione una opción: "))
         except ValueError:
                print(f"Opción invalida debe ingresar (1-5)")

def ejecutar_opciones(opcion, lis_registro_diario):
    if opcion == 1:
        registrar_carga(lis_registro_diario)
    elif opcion == 2:
        if lis_registro_diario[0] != 0:
            mostrar_carga(lis_registro_diario)
        else:
            print("No hay carga realizada.")
    elif opcion == 3:
        if lis_registro_diario[0] != 0:
            dia, amplitud = mayor_amplitud_termica(lis_registro_diario)
            print(f"{dia} -> Amplitud: {amplitud}°")
        else:
            print("No hay carga realizada.")
    elif opcion == 4:
        if lis_registro_diario[0] != 0:
            total, promedio = total_promedio_precipitacion(lis_registro_diario)
            print(f"La precipitación total es: {total:.2f} mm")
            print(f"\nEl promedio diario es: {promedio:.2f} mm")
        else:
            print("No hay carga realizada.")
    elif opcion == 5:
        print("---*** Programa finalizado ***---\n")
        return True
    else:
        print(f"Opción invalida: {opcion}")
    return False

iniciar_menu()