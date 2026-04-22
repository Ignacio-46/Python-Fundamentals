# Sistema de Gestión de Consultas Médicas
# Desarrollar un programa en Python que permita gestionar consultas médicas utilizando listas paralelas.
# El sistema deberá mostrar un menú con las siguientes opciones:
# 1. Registrar nuevos pacientes. Solicitar y almacenar:
#     Nombre del paciente (solo letras y espacios)
#     Especialidad: C → Cardiología, T → Traumatología, P → Pediatría
#     Tiempo de espera (número entero positivo)
#     Número de consultorios (entero positivo)
# 2. Listar todos los pacientes: Mostrar todos los pacientes registrados con: Nombre, Especialidad, Tiempo de espera, Consultorio
# 3. Filtrar pacientes por especialidad: Solicitar una especialidad y mostrar todos los pacientes que correspondan a la misma.
# 4. Calcular promedio de tiempo de espera: Calcular y mostrar el promedio de los tiempos de espera de todos los pacientes.
# 5. Paciente con menor tiempo de espera: Mostrar el nombre del paciente con el menor tiempo de espera junto con su tiempo.
# 6. Pacientes por encima del promedio (alerta): Mostrar únicamente los pacientes cuyo tiempo de espera sea superior al promedio.
# 7. Buscar paciente por nombre: Solicitar un nombre y mostrar todos los datos del paciente si existe.
# 8. Contar pacientes por especialidad: Solicitar una especialidad y mostrar cuántos pacientes hay registrados en la misma.
# 9. Salir del programa: Finalizar la ejecución del sistema.

def main():
    pacientes  = []
    especialidades = []
    tiempo_espera = []
    consultorios = []

    opciones(pacientes, especialidades, tiempo_espera, consultorios)

def validacion_numero(mensaje, tipo):
    while True:
            try: # función validación de números
                if tipo == 1:
                    valor_int = int(input(mensaje))
                    return valor_int
                if tipo == 2:
                    valor_float = float(input(mensaje))
                    return valor_float
            except ValueError:
                print("Debe ingresar un valor numérico.")

def validacion_nombre(mensaje):
    letras = "abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    while True:
        nombre = input(mensaje).title().strip()
        if nombre == "":
            print("Error. Ingrese el nombre.")
            continue

        for letra in nombre:
            if letra not in letras:
                print("Error. Solo se permiten letras y espacios.")
                break
        else:
            return nombre

def validacion_categoria(mensaje):
    letras = "CTP"
    while True:
        categoria = input(mensaje).upper().strip()
        if categoria == "":
            print("Error. Ingrese la especialidad mencionada.")
            continue

        for letra in categoria:
            if letra not in letras:
                print("Error. Intente ingresar la especialidad mencionada.")
                break

        else:
            if categoria == "C":
                return "Cardiología"
            elif categoria == "P":
                return "Pediatría"
            elif categoria == "T":
                return "Traumatología"

def menu():
    print('''\n
      ***********************************************************   
      **----*** Sistema de Gestión de Consultas Médicas ***----**
      **|                                                     |** 
      **|   1. Registrar Nuevos Pacientes                     |**
      **|   2. Listar los pacientes                           |**
      **|   3. Filtrar Pacientes por especialidad             |**
      **|   4. Promedio de tiempo de espera                   |**
      **|   5. Paciente con menor tiempo de espera            |**
      **|   6. Detectar pacientes por encima del promedio     |**
      **|   7. Buscar Paciente por nombre                     |**
      **|   8. Contar pacientes por especialidad              |**
      **|   9. Salir del Programa                             |**
      **|                                                     |**
      **-------------------------------------------------------**
      ***********************************************************\n''')

    while True:
        opcion = validacion_numero("Seleccione la opción del menú: ",1)
        if 0 < opcion < 10:
            return opcion
        else:
            print(f"Opción Invalida: {opcion}.")

def registrar_pacientes(pacientes, especialidades, tiempo_espera, consultorios): #1

    paciente = validacion_nombre("Ingrese el 'nombre' del paciente: ")
    pacientes.append(paciente)

    especialidad = validacion_categoria("Ingrese las Especialidades 'C'(Cardiología),'T'(Traumatología),'P'(Pediatría): ")
    especialidades.append(especialidad)

    while True:
        duracion = validacion_numero("Ingrese la duración de la consulta: ",1)
        if duracion <= 0:
            print("Error. Tiene que ser positiva.")
            continue
        else:
            tiempo_espera.append(duracion)
            break

    while True:
        consultorio = validacion_numero("Ingrese el consultorio: ",1)
        if consultorio <= 0:
            print("Error. Tiene que ser positiva.")
            continue
        else:
            consultorios.append(consultorio)
            break

    print("\n---*** Se registró el Paciente ***---.\n")

def mostrar_pacientes(pacientes, especialidades, tiempo_espera, consultorios): #2
    if not pacientes:
        return None

    datos_pacientes = []
    for i in range(len(pacientes)):
        datos_pacientes.append((i + 1, pacientes[i], especialidades[i], tiempo_espera[i], consultorios[i]))

    return datos_pacientes

def listar_por_especialidad(pacientes, especialidades): #3
    if not pacientes:
        return None

    especial = validacion_categoria("Ingrese las Especialidades 'C'(Cardiología),'T'(Traumatología),'P'(Pediatría): ")

    lista = []
    for i in range(len(pacientes)):
        if especialidades[i] == especial:
            lista.append((pacientes[i], especialidades[i]))

    if not lista:
        return None

    return lista

def calcular_promedio_espera(tiempo_espera): #4
    if not tiempo_espera:
        return None

    suma = 0
    for i in range(len(tiempo_espera)):
        suma += tiempo_espera[i]

    return  suma/len(tiempo_espera)

def paciente_mas_rapido(pacientes, tiempo_espera): #5
    if not tiempo_espera:
        return None

    menor = tiempo_espera[0]
    pos = 0
    for i in range(len(tiempo_espera)):
        if tiempo_espera[i] < menor:
            menor = tiempo_espera[i]
            pos = i

    return pacientes[pos], menor

def alerta_superior_promedio(pacientes, tiempo_espera, promedio): #6
    print(f"El promedio es: '{promedio:.2f} minutos'.\n")

    for i in range(len(tiempo_espera)):
        if tiempo_espera[i] > promedio:
            print(f"ALERTA: '{pacientes[i]}' supera el promedio con {tiempo_espera[i]} minutos.")


def buscar_pacientes(pacientes, especialidades, tiempo_espera, consultorios): #7
    if not pacientes:
        return None

    nombre = validacion_nombre("Ingrese el nombre del paciente: ")

    lista = []
    for i in range(len(pacientes)):
        if pacientes[i] == nombre:
            lista.append((pacientes[i], especialidades[i], tiempo_espera[i], consultorios[i]))

    if not lista:
        return None

    return lista

def contar_por_especialidad(especialidades): #9
    if not especialidades:
        return None

    especial = validacion_categoria("Ingrese las especialidades 'C'(Cardiología),'T'(Traumatología),'P'(Pediatría): ")

    contador = 0
    for i in range(len(especialidades)):
        if especialidades[i] == especial:
           contador += 1

    return contador, especial

def opciones(pacientes, especialidades, tiempo_espera, consultorios):
    opcion = menu()
    while True:
        if opcion == 1:
            registrar_pacientes(pacientes, especialidades, tiempo_espera, consultorios)
        elif opcion == 2:
            datos = mostrar_pacientes(pacientes, especialidades, tiempo_espera, consultorios)
            if datos is not None:
                for i, nombre, especialidad, tiempo, salon in datos:
                    print(f"{i} - Paciente: {nombre} - Especialidad: {especialidad} - Tiempo de espera: {tiempo} minutos - Consultorio: {salon}.")
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 3:
            listar = listar_por_especialidad(pacientes, especialidades)
            if listar is not None:
                for nombre , especifico in listar:
                    print(f"Paciente: {nombre} - Especialidad: {especifico}")
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 4:
            promedio = calcular_promedio_espera(tiempo_espera)
            if promedio is not None:
                print(f"El promedio de los pacientes en espera es: '{promedio:.2f} minutos'.")
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 5:
            menos = paciente_mas_rapido(pacientes, tiempo_espera)
            if menos is not None:
                nombre, tiempo = menos
                print(f"El paciente más rapido fue '{nombre}' con '{tiempo} minutos'.")
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 6:
            promedio = calcular_promedio_espera(tiempo_espera)
            if promedio is not None:
                alerta_superior_promedio(pacientes, tiempo_espera, promedio)
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 7:
            encontrado = buscar_pacientes(pacientes, especialidades, tiempo_espera, consultorios)
            if encontrado is not None:
                for nombre, especialidad, tiempo, salon in encontrado:
                    print(f"El Paciente '{nombre}':\nEspecialidad: {especialidad} - Tiempo de espera: {tiempo} minutos - Consultorio: {salon}.")
            else:
                print("No se encontró el paciente.")
        elif opcion == 8:
            cantidad = contar_por_especialidad(especialidades)
            if cantidad is not None:
               contador , especialidad = cantidad
               if contador == 1:
                   print(f"Hubo '{contador}' paciente registrado en la especialidad '{especialidad}'.")
               elif contador == 0:
                   print(f"'NO' Hubo pacientes registrados en la especialidad '{especialidad}'.")
               else:
                   print(f"Hubo '{contador}' pacientes registrados en la especialidad '{especialidad}'.")
            else:
                print("No se ha registrado ningún paciente.")
        elif opcion == 9:
            print("\n---*** Fin del Programa ***---\n")
            return

        opcion = menu()

main()