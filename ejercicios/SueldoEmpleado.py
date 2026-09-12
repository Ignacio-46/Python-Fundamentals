# Parcial: Gestión de Sueldos de Empleados
# 1. Contexto del Problema: Como desarrollador interno de una agencia de software, se te ha solicitado crear un sistema base
# para procesar la liquidación mensual de un equipo de 5 empleados.
# El sistema debe permitir la carga de las horas trabajadas y las inasistencias, calcular el sueldo neto final
# y generar reportes estadísticos mediante el uso de Programación Orientada a Objetos (TDA) y estructuras de datos lineales.
# 2. Definición del TDA: tdaRegistroEmpleado Deberás utilizar y completar la lógica de la clase tdaRegistroEmpleado.
# Esta clase representa la información laboral mensual de un empleado específico. Atributos:
# legajo (int): Número de identificación del empleado.
# sueldo_base (float): Sueldo bruto mensual fijo del empleado.
# horas_extras (int): Cantidad de horas extras trabajadas en el mes (debe ser $\ge 0$).
# inasistencias (int): Días de ausencia en el mes (debe ser $\ge 0$).
# Plantilla Base:
# class tdaRegistroEmpleado:
#
#     def __init__(self, plegajo, psueldo_base, phoras_extras, pinasistencias):
#         """
#         Constructor de la clase.
#         Asigna los parámetros recibidos a los atributos del objeto.
#         """
#         self.legajo = plegajo
#         self.sueldo_base = psueldo_base
#         self.horas_extras = phoras_extras
#         self.inasistencias = pinasistencias
#
# 3. Requerimientos del Programa Principal: El programa deberá gestionar una lista llamada lis_empleados,
# inicializada para contener los 5 objetos del equipo. Debes implementar un menú de opciones con las siguientes funcionalidades:
# 1. Cargar Registros: Solicitar al usuario los datos de los 5 empleados.
#    Validación: Utilizar bloques try-except para capturar errores de entrada (ej. ingresar texto en lugar de números).
#    Asegurar que ni las horas extras ni las inasistencias sean valores negativos, y que el sueldo base sea mayor a cero.
# 2. Mostrar Registros: Listar de forma prolija los datos base de todos los empleados cargados.
# 3. Mayor Sueldo Neto: Calcular el sueldo neto de cada empleado basándose en la siguiente fórmula:
#    $S_{neto} = S_{base} + (H_{extras} \times 8500) - (I_{inasistencias} \times 12000)$
#    Determinar y mostrar por pantalla el legajo y el monto del empleado con el mayor sueldo neto final.
# 4. Estadísticas de Nómina: Calcular y mostrar el monto total que la empresa debe desembolsar para pagar todos los sueldos netos del mes.
#    Calcular y mostrar el sueldo neto promedio del equipo.
# 5. Salir: Finalizar la ejecución del programa.

class tdaRegistroEmpleado:
     def __init__(self, plegajo, psueldo_base, phoras_extras, pinasistencias):
         self.legajo = plegajo
         self.sueldo_base = psueldo_base
         self.horas_extras = phoras_extras
         self.inasistencias = pinasistencias

     def __str__(self):
         return f"Empleado: {self.legajo} -> Sueldo: ${self.sueldo_base:.2f} | Hs Extras: {self.horas_extras} hs | Inasistencias: {self.inasistencias} faltas"

def validacion_numero(mensaje, tipo):
    while True:
        try:
            if tipo == 1:
                numero_int = int(input(mensaje))
                if numero_int < 0:
                    print("Error. Debe ingresar un número positivo.")
                else:
                    return numero_int
            if tipo == 2:
                numero_float = float(input(mensaje))
                if numero_float < 0:
                    print("Error. Debe ingresar un número positivo.")
                else:
                    return numero_float
        except ValueError:
            print("Error. Ingrese un número.")

def registrar_empleados(lis_empleados):
    print("Registrar empleados: ")
    for i in range(len(lis_empleados)):
        while True:
            legajo = validacion_numero("Número de identificación del empleado: ", 1)
            if legajo == 0:
                print("La identificación tiene que ser mayor a 0")
            elif legajo > 5:
                print("Solo se identifica hasta 5 empleados")
            else:
                break
        sueldo_base = validacion_numero("Sueldo bruto mensual fijo del empleado: ",2)
        horas_extras = validacion_numero("Cantidad de horas extras trabajadas: ",1)
        inasistencias = validacion_numero("Días de ausencia: ", 1)
        lis_empleados[i] = tdaRegistroEmpleado(legajo, sueldo_base, horas_extras, inasistencias)

    print("\n---*** Registro Completo ***---")

def mostrar_empleados(lis_empleados):
    for empleados in lis_empleados:
        print(empleados)

def sueldo_neto(empleado):
    sueldo = empleado.sueldo_base + (empleado.horas_extras * 8500) - (empleado.inasistencias * 12000)
    return sueldo

def mayor_sueldo_neto(lis_empleados):
    empleado = lis_empleados[0]
    sueldo_mayor = sueldo_neto(lis_empleados[0])
    for i in range(1, len(lis_empleados)):
        if sueldo_neto(lis_empleados[i]) > sueldo_mayor:
            sueldo_mayor = sueldo_neto(lis_empleados[i])
            empleado = lis_empleados[i]
    return empleado, sueldo_mayor

def estadisticas_empleados(lis_empleados):
    total = 0
    for i in range(len(lis_empleados)):
        total += sueldo_neto(lis_empleados[i])
    promedio = total / len(lis_empleados)
    return total, promedio

def iniciar_menu():
    salir =  False
    lis_empleados = [0]*5
    while not salir:
        opciones = mostrar_menu()
        salir = ejecutar_opciones(opciones, lis_empleados)

def mostrar_menu():
    while True:
        print('''\nMenú:
    1. Registrar empleados
    2. Mostrar empleados
    3. Mayor sueldo neto
    4. Estadísticas empleados
    5. Salir del programa\n''')
        try:
            return int(input("Selecciones una opción: "))
        except ValueError:
            print("Opción invalida. Ingrese (1-5)")

def ejecutar_opciones(opciones, lis_empleados):
    if opciones == 1:
        registrar_empleados(lis_empleados)
    elif opciones == 2:
        if lis_empleados[0] != 0:
            mostrar_empleados(lis_empleados)
        else:
            print("No se ha registrado empleados.")
    elif opciones == 3:
        if lis_empleados[0] != 0:
            empleado, sueldo = mayor_sueldo_neto(lis_empleados)
            print(f"{empleado}| Mayor sueldo: ${sueldo}")
        else:
            print("No se ha registrado empleados.")
    elif opciones == 4:
        if lis_empleados[0] != 0:
            total, promedio = estadisticas_empleados(lis_empleados)
            print(f"Monto total de los sueldos de los empleados: ${total:.2f}")
            print(f"El promedio sueldo neto del equipo: ${promedio:.2f}")
        else:
            print("No se ha registrado empleados.")
    elif opciones == 5:
        print("---*** Fin del Programa ***---")
        return True
    else:
        print(f"Opción Invalida: {opciones}.")
    return False

iniciar_menu()
