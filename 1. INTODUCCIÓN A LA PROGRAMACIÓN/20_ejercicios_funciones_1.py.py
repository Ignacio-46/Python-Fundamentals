print("*** Sistema de Inventarios (con Funciones) ***\n")

productos = {"1": {"ID": 1, "nombre": "Camisa", "precio": 25.99, "cantidad": 50},
             "2": {"ID": 2, "nombre": "Pantalones", "precio": 39.99, "cantidad": 30},
             "3": {"ID": 3, "nombre": "Zapato", "precio": 49.99, "cantidad": 20}}

def menu():
    opcion = "1.Mostrar inventarios\n2.Agregar nuevo producto\n3.Buscar productos por ID\n4.Salir"
    print(f"-------*** menu ***--------\n{opcion.upper()}")

def los_productos(productos):
    for ID, producto in productos.items():
        print(f"ID: {ID}, Nombres: {producto["nombre"]}, Precio: ${producto["precio"]}, Cantidad: {producto["cantidad"]} (unidades)")
    print("\n")

def agregar(productos):
    print("--- * Ingrese el nuevo producto *---")
    sumar_producto = str(len(productos) + 1)
    productos[sumar_producto]= {
             "ID" : int(input("ID: ")),
             "nombre": input("Nombre: "),
             "precio": float(input("Precio: ")),
             "cantidad": int(input("Cantidad: "))}
    print("Productos agregado al Inventario\n")

def buscar(productos):
    print("\n--- * Buscar Productos por ID *---")
    id = int(input("Ingresa el ID: "))
    buscar = None
    for ID, producto in productos.items():
        if producto.get("ID") == id:
            buscar = producto
            break

    if buscar is not None:
        print("\nInformacion del Producto encontrado:")
        print(f"ID: {buscar.get("ID")}, Nombres: {buscar.get("nombre")}, Precio: ${buscar.get("precio")}, Cantidad: {buscar.get("cantidad")} (unidades)")
    else :
        print("No existe el ID")
    print("\n")

inicio = 0
while inicio != 1:
    menu()
    opciones = int(input("\nIngrese la opcion del menu: "))
    while opciones < 1 or opciones > 4:
        print("ERROR")
        opciones = int(input("\nIngrese la opcion del menu: "))

    if opciones == 1:
        los_productos(productos)

    if opciones == 2:
        agregar(productos)

    if opciones == 3:
        buscar(productos)

    if opciones == 4:
        inicio = 1
        print("Hasta luego!!")

print("\n-----*** Maquina de Snacks ***-----")

snacks = [{"ID": 1, "nombre": "Papas", "precio": 30},
         {"ID": 2, "nombre": "Refresco", "precio": 50},
         {"ID": 3, "nombre": "Sandwich", "precio": 120},]

def menu():
    opcion = "1.mostrar snacks\n2.comprar snack\n3.mostrar sticket\n4.salir"
    print(f"\n{opcion.upper()}")

def mostrar(snacks):
    for snack in snacks:
        print(f"ID: {snack["ID"]} -> {snack["nombre"]} - ${snack["precio"]}")

comprado = []
def compra(snacks):
    id = int(input("Que snack quieres comprar (ID)?: "))
    venta = None
    for snack in snacks:
        if snack["ID"] == id:
            venta = snack

    if venta is not None:
        comprado.append(venta)
        print(f"Snack agregado: {comprado}")
    else:
        print(f"Snack no encontrado con el ID: {id}")

def ticket(snacks):
    ticket = "---*** Ticket de Venta ***---"
    total = 0
    for compras in comprado:
        ticket += f"\n- {compras.get("nombre")} - ${compras.get("precio")}"
        total += compras.get("precio")
    ticket += f"\nTOTAL -> ${total}"
    print(f"\n{ticket}")

inicio = 0
while inicio != 1:
    menu()
    opciones = int(input("\nIngrese la opcion del menu: "))
    while opciones < 1 or opciones > 4:
        print("ERROR")
        opciones = int(input("\nIngrese la opcion del menu: "))

    if opciones == 1:
        mostrar(snacks)

    if opciones == 2:
        compra(snacks)

    if opciones == 3:
        ticket(snacks)

    if opciones == 4:
        inicio = 1
        print("Hasta Luego!!")

