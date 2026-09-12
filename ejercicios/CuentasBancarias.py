# Ejercicio 2: Administración de Cuentas Bancarias 🏦
# Aquí practicaremos la lógica de "acumuladores" y validación estricta de saldos (no permitir
# negativos en extracciones).
# Datos por cuenta:
# ● Titular (String).
# ● Tipo de Cuenta (A = Ahorro, C = Corriente, S = Sueldo).
# ● Saldo (Decimal, puede ser negativo solo si es Cuenta Corriente, validar esto).
# ● Estado (1 = Activa, 0 = Bloqueada).
# Menú de opciones:
# 1. Abrir Cuenta: Pedir datos. El saldo inicial debe ser positivo.
# 2. Ver Cuentas: Listar todas.
# 3. Total de Dinero en el Banco: Sumar los saldos de todas las cuentas
# (independientemente del tipo).
# 4. Cuenta con Mayor Deuda: Buscar y mostrar la cuenta con el saldo más negativo (o
# menor saldo).
# 5. Listar Cuentas Bloqueadas: Mostrar solo las que tienen Estado = 0.
# 6. Realizar Depósito: Seleccionar una cuenta y sumar dinero al saldo (reutilizar lógica de
# búsqueda).
# 7. Salir

titular = []
cuentas = []
saldos = []
estados = []

def menu():
    print("""Menú:
    1. Agregar una cuenta
    2. Ver cuentas
    3. Dinero total
    4. Cuenta con mayor deuda
    5. Cuentas bloqueadas
    6. Deposito
    7. Salir\n""")

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

def agregar_cuenta():
    #Titular(String).
    letras_validas = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    while True:
        nombre = input("Ingrese el nombre del titular: ").lower()
        if nombre == "":
            print("Debe ingresar un nombre.")
            continue

        es_valido = True
        for letra in nombre:
            if letra not  in letras_validas:
                es_valido = False
                break

        if es_valido:
            titular.append(nombre)
            break
        else:
            print("No se permiten números, ni símbolos negativos.")
            continue

    #Tipo de Cuenta (A = Ahorro, C = Corriente, S = Sueldo).
    tipo = ["A","C","S"]
    while True:
        cuenta = input("Ingrese la cuenta del titular A(Ahorro), C(Corriente), S(Sueldo): ").upper()
        if cuenta == "":
            print("Seleccione la cuenta indicada.")
            continue

        es_valido = True
        for letra in cuenta:
            if letra not in tipo:
                es_valido = False
                break

        if es_valido:
            if cuenta == "A":
                cuenta_completa = "Ahorro"
            elif cuenta == "C":
                cuenta_completa = "Corriente"
            else:
                cuenta_completa = "Sueldo"
            cuentas.append(cuenta_completa)
            break
        if not es_valido:
            print("No existe la cuenta.")
            continue

    #Saldo (Decimal, puede ser negativo solo si es Cuenta Corriente, validar esto).
    while True:
        saldo = validar_numero("Ingrese el saldo del titular: ", 2)
        if saldo < 0:
            if cuenta == "C":
                saldos.append(saldo)
                break
            else:
                print("El saldo negativo solo se ingresa en la cuenta corriente.")
                continue
        else:
            saldos.append(saldo)
            break

    #Estado (1 = Activa, 0 = Bloqueada).
    while True:
        estado = validar_numero("Ingrese el estado del titular 0(Bloqueada), 1(Activa): ", 1)
        if estado == 0:
            print("Cuenta Bloqueada.\n")
            estado = "Bloqueada"
            estados.append(estado)
            break
        if estado == 1:
            print("Cuenta Activa.\n")
            estado = "Activa"
            estados.append(estado)
            break
        else:
            print("No existe tal estado.")
            continue

    print("\n---*** Se registró la cuenta ***---\n")

def mostrar_cuentas():
    for i in range(len(cuentas)):
        print(f"{i +1}. Titular: {titular[i]}, Cuenta: {cuentas[i]}, Saldo: ${saldos[i]}, Estado: {estados[i]}")
    print("\n")

def total_saldo():
    total = 0
    for i in range(len(saldos)):
        total += saldos[i]
    print(f"El total de todos los saldos es: ${total}\n")

def mayor_deuda():
    menor = saldos[0]
    indice = 0
    for i in range(len(saldos)):
        if saldos[i] < menor:
            menor = saldos[i]
            indice = i
    print(f"El titular con mayor deuda es '{titular[indice]}' con un saldo de '${menor}'.\nCuenta: {cuentas[indice]}, Estado: {estados[indice]}")
    print("\n")

def cuenta_bloqueada():
    bloqueo = False
    for i in range(len(estados)):
        if estados[i] == "Bloqueada":
            bloqueo = True
            print(f"El titular con la cuenta '{estados[i]}' es '{titular[i]}' con un saldo de '${saldos[i]}'.")
    print("\n")

    if not bloqueo:
        print("No se há registrado una cuenta bloqueada.\n")

def deposito():
    mostrar_cuentas()
    # Pedimos el índice (el número de la izquierda que mostraste en la lista)
    while True:
        indice_usuario = validar_numero("Ingrese el indice de la cuenta a depositar: ", 1)
        # Ajustamos porque el usuario ve 1, pero las listas empiezan en 0
        indice = indice_usuario - 1
        if 0 <= indice < len(cuentas):  # Validamos que el índice exista
            monto = validar_numero("Ingrese monto: ", 2)
            if monto > 0:
                saldos[indice] += monto
                print(f"Se depositó en la cuenta de '{cuentas[indice]}' de '{titular[indice]}'.\n")
                break
            else:
                print("El monto debe ser positivo.")
                continue
        else:
            print("Error.La cuenta no existe.")
            continue

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_cuenta()
        elif opcion == 2:
            if cuentas:
                mostrar_cuentas()
            else:
                print("Lista de cuentas vacías. Ingrese sus cuentas bancarias.\n")
        elif opcion == 3:
            if cuentas:
                total_saldo()
            else:
                print("Lista de cuentas vacías. Ingrese sus cuentas bancarias.\n")
        elif opcion == 4:
            if cuentas:
                mayor_deuda()
            else:
                print("Lista de cuentas vacías. Ingrese sus cuentas bancarias.\n")
        elif opcion == 5:
            if cuentas:
                cuenta_bloqueada()
            else:
                print("Lista de cuentas vacías. Ingrese sus cuentas bancarias.\n")
        elif opcion == 6:
            if cuentas:
                deposito()
            else:
                print("Lista de cuentas vacías. Ingrese sus cuentas bancarias.\n")
        elif opcion == 7:
            print("Saliendo del programa.\n")
            break
        else:
            print("La opción es entre (1-7).\n")
            continue
    except ValueError:
        print("Opción invalida. Ingrese un valor numérico.\n")
        continue




