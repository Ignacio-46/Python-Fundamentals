#EJERCICIO 1: SUMA ACUMULATIVA
maximo = 5
numero = 1
acumulador = 0
while numero <= maximo:
    print(f"Acumulador + numero -> {acumulador} + {numero}")
    acumulador += numero
    numero += 1
    print(f"suma parcial acumulada : {acumulador}\n")
print(f"La suma acumulada es:{acumulador}\n")

#EJERCICIO 2: SISTEMA DE ADMINISTRACION DE CUENTAS
print("*** Sistema de Administracion de Cuentas ***")
print("          1.Crear tu cuenta")
print("          2.Eleminar tu cuenta")
print("          3.Salir del sistema")
print("--------------------------------------------\n")

inicio = 0
while inicio != 1:
    menu = int(input("Ingrese el valor del menu: "))
    while menu < 1 or menu > 3:
        print("ERROR")
        menu = input("Ingrese el valor del menu: ")

    if menu == 1:
        print("Crear tu cuenta\n")
    if menu == 2:
        print("Eleminar tu cuenta\n")
    if menu == 3:
        print("-------- *** saliste *** -----------\n")
        inicio = 1

#EJERCICIO 3: APLICACION CAJERO AUTOMATICO
print("*** Aplicacion Cajero Autmoatico ***")
print("         1.Consultar Saldo")
print("         2.Retirar Saldo")
print("         3.Depositar Saldo")
print("         4.Salir de sistema")
print("-------------------------------------\n")

inicio = 0     #SIEMPRE DECLARA LAS VARIABLES AFUERA DE TODO
saldo = 1000   #SINO TE PUEDE DAR ERROR

while inicio != 1:
    menu = int(input("Ingrese el valor del menu: "))
    while menu < 1 or menu > 4:
        print("ERROR")
        menu = input("Ingrese el valor del menu: \n")

    if menu == 1:
            print(f"Tu saldo actual es: ${saldo:.2f}\n")

    elif menu == 2:
        retiro = float(input("Ingrese el monto de su Retiro: "))
        if retiro <= saldo:
            saldo -= retiro #saldo = saldo - retiro
            print(f"Tu nuevo saldo es: ${saldo:.2f}\n")
        else:
            print(f"No cuenta con saldo suficiente. Tu saldo actual es de ${saldo:.2f}\n")

    elif menu == 3:
        deposito = float(input("Ingrese el monto de su Deposito: "))
        saldo += deposito #saldo = saldo + deposito
        print(f"Tu Deposito actual es: ${saldo:.2f}\n")

    elif menu == 4:
        print("---*** Terminó tu Transacción ***---\n")
        inicio = 1

#EJERCICIO 4: CALCULADORA DE PYTHON
print('''         *** Calculadora de Python *** 
          ---------------------------
            1.Suma
            2.Resta
            3.Multiplicación
            4.División
            5.Salir de la Calculadora
         -----------------------------\n''')

inicio = 0

while inicio != 1:
    menu = int(input("           Ingrese el valor del menu: "))
    while menu < 1 or menu > 5:
        print("                      ERROR")
        menu = int(input("           Ingrese el valor del menu: "))

    if menu == 1:
            numero1 = float(input("           Ingrese el numero 1: "))
            numero2 = float(input("           Ingrese el numero 2: "))
            suma = numero1 + numero2
            print(f"           La suma de los numeros ingresados son: {suma:.2f}\n")
    elif menu == 2:
            numero1 = float(input("           Ingrese el numero 1: "))
            numero2 = float(input("           Ingrese el numero 2: "))
            resta = numero1 - numero2
            print(f"           La resta de los numeros ingresados son: {resta:.2f}\n")
    elif menu == 3:
            numero1 = float(input("           Ingrese el numero 1: "))
            numero2 = float(input("           Ingrese el numero 2: "))
            multiplica = numero1 * numero2
            print(f"           La multiplicación de los numeros ingresados son: {multiplica:.2f}\n")
    elif menu == 4:
            numero1 = float(input("           Ingrese el numero 1: "))
            numero2 = float(input("           Ingrese el numero 2: "))
            division = numero1 / numero2
            print(f"           La división de los numeros ingresados son: {division:.2f}\n")
    elif menu == 5:
            inicio = 1
            print(f"      *** *** Aprendé a sumar tonto *** ***")
