print("-----*** Calculadora con Funciones ***-----")

def menu():
    opcion = "1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Impuesto\n6. Temperatura\n7. Salir"
    print(f"\n{opcion.upper()}")

def suma():
    valor1 = float(input("Dame el valor 1: "))
    valor2 = float(input("Dame el valor 2: "))
    sumar = valor1 + valor2
    print(f"El resultado de la suma es: {sumar}")

def resta():
    valor1 = float(input("Dame el valor 1: "))
    valor2 = float(input("Dame el valor 2: "))
    restar = valor1 - valor2
    print(f"El resultado de la suma es: {restar}")

def multiplicacion():
    valor1 = float(input("Dame el valor 1: "))
    valor2 = float(input("Dame el valor 2: "))
    multiplicar = valor1 * valor2
    print(f"El resultado de la suma es: {multiplicar}")

def division():
    valor1 = float(input("Dame el valor 1: "))
    valor2 = float(input("Dame el valor 2: "))
    dividir = valor1 / valor2
    print(f"El resultado de la suma es: {dividir}")

def impuesto():
    sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
    monto_impuesto = int(input("Proporcione el monto del impuesto: "))
    total = sin_impuesto + sin_impuesto * (monto_impuesto/100)
    print(f"Pago con impuesto: {total}")

def temperatura():
    celsius = float(input("\nIngrese los grados de Celsius para Fahrenheit (°C): "))
    fahrenheit = float(input("Ingrese los grados de Fahrenheit para Celsius (°F): "))
    F = (celsius * 9/5) + 32
    C = (fahrenheit - 32) * 5/9
    print(f"\nEl resultado de Celsius a Fahrenheit es: {F}°F")
    print(f"El resultado de Fahrenheit a Celsius es: {C}°C")

ini = 0
while ini != 1:
    menu()
    opciones = int(input("\nIngrese la opción del menu: "))
    while opciones < 1 or opciones > 7:
        print("ERROR")
        opciones = int(input("\nIngrese la opción del menu: "))

    if opciones == 1:
        suma()

    elif opciones == 2:
        resta()

    elif opciones == 3:
        multiplicacion()

    elif opciones == 4:
        division()

    elif opciones == 5:
        impuesto()

    elif opciones == 6:
        temperatura()

    elif opciones == 7:
        ini = 1
        print("Saliste de Calculadora.. HASTA PRONTO!!\n")

def validar_numero(mensaje,tipo):
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