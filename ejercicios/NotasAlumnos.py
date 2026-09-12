# Ejercicio 1: Gestión de Notas de Alumnos 🎓
# Este ejercicio pone a prueba tu capacidad de filtrar por condiciones (aprobado/desaprobado)
# y calcular promedios.
# Datos por alumno:
# ● Nombre (String).
# ● Materia (M = Matemática, L = Lengua, H = Historia, G = Geografía).
# ● Nota (Decimal entre 1.0 y 10.0).
# ● Asistencias (Entero positivo).
# Menú de opciones:
# 1. Registrar Alumno: Pedir datos. Validar que la materia sea un caracter válido y la nota
# esté en rango.
# 2. Listar Alumnos: Mostrar todos los datos cargados.
# 3. Calcular Promedio por Materia: El usuario ingresa una materia (ej: 'M') y el programa
# muestra el promedio de notas de esa materia.
# 4. Alumno Destacado: Mostrar los datos del alumno con la nota más alta de todo el sistema.
# 5. Reporte de Libres: Listar alumnos con menos de 5 asistencias.
# 6. Corregir Nota: Listar alumnos, seleccionar uno y actualizar su nota (útil para practicar la modificación de datos).
# 7. Salir.

alumnos = []
materias = []
notas = []
asistencias = []

def menu():
    print("""Menú:
    1. Registrar alumnos
    2. Lista de los alumnos
    3. Promedio de la materia
    4. Alumno destacado
    5. Reporte de libres
    6. Modificar notas
    7. Salir\n""")

def pedir_numero(mensaje, accion):
    while True:
        try:
            if accion == 1:
                valor_int = int(input(mensaje))
                return valor_int
            if accion == 2:
                valor_float = float(input(mensaje))
                return valor_float
        except ValueError:
            print("Debe ingresar un valor numérico.")

def agregar_alumnos():
    letras_validas = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        nombre = input("Ingrese el nombre del alumno: ").strip()
        if nombre == "":
            print("Error. Ingrese el nombre")
            continue

        es_valido = True
        for letra in nombre:
            if letra not in letras_validas:
                es_valido = False
                break

        if es_valido:
            alumnos.append(nombre)
            break
        else:
            print("Error. Ingrese el nombre.")

    materias_validas = ["M","L","H","G"]
    while True:
            materia = input("Ingrese la materia: M(Matemáticas), L(Lengua), H(Historia), G(Geografía): ").upper()
            if materia == "":
                print("Error. Ingrese la categoria.")
                continue

            es_valido = True
            for letra in materia:
                if letra not in materias_validas:
                    es_valido = False
                    break

            if es_valido:
                materias.append(materia)
                break
            if not es_valido:
                print("No existe tal materia.")

    while True:
        nota = pedir_numero("Ingrese la nota del alumno: ",2)
        if nota < 1 or nota > 10:
            print(f"La nota es entre (1-10)")
            continue
        else:
            notas.append(nota)
            break

    while True:
        asistencia = pedir_numero("Ingrese la asistencia del alumno: ",1)
        if asistencia < 0:
            print(f"Error. No puede ser negativo")
            continue
        else:
            asistencias.append(asistencia)
            break

    print("\nSe registró el alumno en la lista.\n")

def mostrar_alumnos():
    for i in range(len(alumnos)):
        print(f"{i + 1}. Alumno: {alumnos[i]}, Materia: {materias[i]}, Nota: {notas[i]}, Asistencia: {asistencias[i]}.")
    print("\n")

def promedio_materia():
    mostrar_alumnos()
    caracteres = "MLHG"
    while True:
        caracter = input("Ingrese la materia M(Matemáticas), L(Lengua), H(Historia), G(Geografía): ").upper()
        if caracter == "":
            print("Error. Ingrese el carácter de la materia.")
            continue

        valido = True
        for letra in caracter:
            if letra not in caracteres:
                valido = False

        if valido:
            suma = 0
            cantidad = 0
            for i in range(len(materias)):
                if materias[i] == caracter:
                    suma += notas[i]
                    cantidad += 1

            if cantidad == 0:
                print(f"La materia existe pero no se ha registrado notas de los alumnos.")
                continue

            promedio = suma/cantidad

            if caracter == "M":
                recaracter = "Matemáticas"
            elif caracter == "L":
                recaracter = "Lengua"
            elif caracter == "H":
                recaracter = "Historia"
            else:
                recaracter = "Geografía"

            print(f"El promedio de la materia '{recaracter}' es '{promedio}'.\n")
            break

        if not valido:
            print("Error. No existe tal materia seleccione M,L,H o G.")
            continue

def alumno_destacado():
    mayor = notas[0]
    indice = 0
    for i in range(len(notas)):
        if notas[i] > mayor:
            mayor = notas[i]
            indice = i
    print(f"El alumno mas destacado es '{alumnos[indice]}' con una nota de '{mayor}'. Materia: {materias[indice]}, Asistencia: {asistencias[indice]}.\n")

def reporte_libres():
    print("Alumnos con menos de 5 asistencias: ")
    minimo = 5
    libres = False
    for i in range(len(asistencias)):
        if asistencias[i] < minimo:
            libres = True
            print(f"{i +1}. '{alumnos[i]}' tiene '{asistencias[i]}' asistencias. Materia: {materias[i]}, Nota: {notas[i]}.")
    print("\n")

    if not libres:
        print("No se registró alumno con menos de 5 asistencia.\n")

def corregir_notas():
    mostrar_alumnos()
    while True:
        seleccionado = input("Seleccione el alumno: ").lower()
        indice = -1
        for i in range(len(alumnos)):
            if alumnos[i] == seleccionado:
                indice = i
                break

        if indice == -1:
            print("Error de nombre o no se registró tal alumno.\n")
            continue

        while True:
            nota_nueva = pedir_numero("Modifique la nota del alumno: ", 2)
            if nota_nueva < 1 or nota_nueva > 10:
                print("La nota es entre (1-10).")
                continue
            else:
                for i in range(len(notas)):
                    notas[indice] = nota_nueva
                print(f"La nota de '{seleccionado}' fue modificada.\n")
                break
        break
    mostrar_alumnos()

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_alumnos()
        elif opcion == 2:
            if alumnos:
                mostrar_alumnos()
            else:
                print("La lista está vacía. Registre los alumnos.\n")
        elif opcion == 3:
            if alumnos:
                promedio_materia()
            else:
                print("La lista está vacía. Registre los alumnos.\n")
        elif opcion == 4:
            if alumnos:
                alumno_destacado()
            else:
                print("La lista está vacía. Registre los alumnos.\n")
        elif opcion == 5:
            if alumnos:
                reporte_libres()
            else:
                print("La lista está vacía. Registre los alumnos.\n")
        elif opcion == 6:
            if alumnos:
                corregir_notas()
            else:
                print("La lista está vacía. Registre los alumnos.\n")
        elif opcion == 7:
            print("Fin del programa.\n")
            break
        else:
            print(f"La opción es entre (1-7): {opcion}.\n")
            continue
    except ValueError:
            print("Opción Invalida. Ingrese un valor numérico.\n")
            continue










