# Gestión de inventario de productos
# Escribe un programa que gestione un inventario de productos.
# Cada producto en la lista debe tener un nombre.
# Una categoría (Alimentos, Higiene, Electrodomésticos o Bazar).
# Un precio (número positivo decimal).
# Una cantidad de stock (número natural o puede ser 0).

# El programa debe mostrar un menú con las siguientes opciones:
# 1.Agregar un nuevo producto al inventario con su nombre, categoría, precio y cantidad de stock.
#  a)Solicitar nombre de producto = string
#  b)Solicitar categoría = Debe ser un carácter según la siguiente tabla:
#    A = Alimentos.
#    H = Higiene.
#    E = Electrodomesticos.
#    B = Bazar.
#  c)Solicitar precio = float (No deben ser números negativos)
#  d)Solicitar cantidad de stock = int (No deben ser números negativos)
# 2.Mostrar la lista de productos, incluyendo nombres, categorías, precios y cantidad de stock.
# 3.Calcular el promedio de precios de una categoría específica.
# 4.Encontrar  y mostrar el producto más caro (Se debe mostrar todos los datos del producto más caro).
# 5.Listar productos con poco stock (Los que tienen menos de 5 inclusive.
# Se debe mostrar todos los datos del producto con menos stock).
# 6.Agregar stock de un producto determinado.
# (Se puede reutilizar la lógica de Mostrar los productos del punto 2
# para listar los productos así el usuario puede ingresar el número y aumentar su stock)
# 7.Salir del programa.

productos = []
precios = []
categorias = []
stock = []

def menu():
    print("Menú:")
    eleccion = ("1. Agregar los productos\n2. Mostrar los productos\n3. Promedio de una categoria especifica\n"
                "4. El producto mas caro\n5. Los productos con poco stock\n"
                "6. Agregar stock del producto determinado\n7. Salir del programa\n")
    print(f"{eleccion}")

def agregar_productos():
    while True:
        nombre = input("Ingrese el nombre del producto: ").lower().strip()
        if nombre == "":
            print("Nombre vacío. Ingrese el nombre.\n")
            continue
        else:
            productos.append(nombre)
            break
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                print("No se permiten números negativo.\n")
                continue
            else:
                precios.append(precio)
                break
        except ValueError:
            print("Ingrese solo valor numérico.\n")
            continue
    categorias_validas = ["A", "H", "E", "B"]
    while True:
        print("Elija la categoria A(Alimentos), H(Higiene), E(Electrodoméstico), B(Bazar)")
        seccion = input("Ingrese la categoria: ").upper()
        if seccion in categorias_validas:
            categorias.append(seccion)
            break
        else:
            print("No existe tal categoría. Ingrese solo A, H, E, o B.\n")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de stock: "))
            if cantidad < 0:
                print("No se permiten números negativo.\n")
                continue
            else:
                stock.append(cantidad)
                break
        except ValueError:
                print("Ingrese solo valor numérico.\n")
                continue
    print("---*** Se agregó a la lista de productos ***---\n")

def mostrar_productos():
    for i in range(len(productos)):
        print(f"{i + 1}. Producto: {productos[i]}, Precio: ${precios[i]}, Categoría: {categorias[i]}, Stock: {stock[i]} disponible.")
    print("\n")

def promedio_categoria_especifica():
    categorias_validas = ["A", "H", "E", "B"]
    while True:
        elegir = input("Ingrese la categoría (A/H/E/B): ").upper()
        try:
            valor = float(elegir)
            print(f"Error, no se permiten números: '{valor:.0f}'.\n")
            continue
        except ValueError:
            pass

        if len(elegir) != 1:
            print("Error: no se permite letras con números.\n")
            continue
        if elegir not in categorias_validas:
            print("No existe la categoría.\n")
            continue

        suma = 0
        cantidad = 0
        for i in range(len(categorias)):
            if categorias[i] == elegir:
                suma += precios[i]
                cantidad += 1

        if cantidad == 0:
            print("Categoría existe pero no tiene productos.\n")
            continue

        promedio = suma/cantidad
        print(f"El promedio del precio de la categoría '{elegir}' es: ${promedio:.2f}\n")
        break

def producto_mas_caro():
    caro = precios[0]
    mayor = 0
    for i in range(len(precios)):
        if precios[i] > caro:
            caro = precios[i]
            mayor = i
    print(f"El producto mas caro: {productos[mayor]}, Precio: ${precios[mayor]}, Categoría: {categorias[mayor]}, Stock: {stock[mayor]} disponible.\n")

def producto_poco_stock():
    poco = 5
    encontrado = False
    for i in range(len(stock)):
        if stock[i] <= poco:
            print(f"El producto con poco stock es: {productos[i]}, Precio: ${precios[i]}, Categoría: {categorias[i]}, con '{stock[i]}' disponible.\n")
            encontrado = True
    if not encontrado:
        print("No hay productos con stock mínimos de 5.\n")

def agregar_stock_producto(productos):
    mostrar_productos()
    cambio = 0
    while True:
        decidir = input("Elija el producto para cambiar su stock: ").lower()
        try:
            valor = float(decidir)
            print(f"Error: No se permiten números: {valor:.0f}.\n")
            continue
        except ValueError:
            pass

        if decidir not in productos:
            print("No existe tal producto.\n")
            continue
        break

    for i in range(len(productos)):
        if decidir == productos[i]:
            while True:
                try:
                    stock_nuevo = int(input(f"Ingrese el nuevo stock de {decidir}: "))
                    if stock_nuevo < 0:
                        print("No se permiten números negativo.\n")
                        continue
                    else:
                        cambio = i
                        stock[i] += stock_nuevo
                        break
                except ValueError:
                    print("Ingrese solo valor numérico.\n")
                    continue

    print(f"Stock nuevo de '{productos[cambio]}' fue modificado.\n")

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
                agregar_productos()
        elif opcion == 2:
            if productos:
                mostrar_productos()
            else:
                print("La lista esta vacía. Agregue sus productos.\n")
        elif opcion == 3:
            if productos:
                promedio_categoria_especifica()
            else:
                print("La lista esta vacía. Agregue sus productos.\n")
        elif opcion == 4:
             if productos:
                producto_mas_caro()
             else:
                print("La lista esta vacía. Agregue sus productos.\n")
        elif opcion == 5:
            if productos:
                producto_poco_stock()
            else:
                print("La lista esta vacía. Agregue sus productos.\n")
        elif opcion == 6:
            if productos:
                agregar_stock_producto(productos)
            else:
                print("La lista esta vacía. Agregue sus productos.\n")
        elif opcion == 7:
            print("Fin del programa.\n")
            break
        else:
            print(f"La opción es entre (1-7): {opcion}.\n")
            continue
    except ValueError:
            print("Opción invalida. Ingrese un valor numérico.\n")
            continue
