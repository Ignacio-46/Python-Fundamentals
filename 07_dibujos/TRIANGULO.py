print("\n\n*** dibujo de un triangulo ***")

numero = int(input("ingrese el numero de filas: "))
for filas in range(1,numero + 1):
    espacios = " " * (numero - filas)
    asteristico = "*" * (2 * filas - 1)
    print(f"{espacios}{asteristico}")