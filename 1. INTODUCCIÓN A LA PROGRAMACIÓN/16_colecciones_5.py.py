#COMBINACION DE LISTA Y DICCIONARIO
personas = [
      {
            "nombre" : "Regina",
            "apellido" : "Flores",
            "edad" : 21
      },
      {
            "nombre" : "Alejandro",
            "apellido" : "Reyes",
            "edad" : 32
      },
]

print(f"Personas:{personas}")

#ACCEDO A BUSCAR INFO DE LA PRIMERA PERSONA
print(f'''\nNombre: {personas[0].get("nombre")}
Apellido: {personas[0].get("apellido")}
edad: {personas[0].get("edad")}
''')

#RECORRER LOS ELEMENTOS DE LA LISTA
for contador, persona in enumerate(personas):
    print(f"{contador}-{persona}")

print("\n")

for contador, persona in enumerate(personas): #SE USA CUANDO SE TRABAJA CON LISTA Y DICCIONARIO [{}]
    print(f"{contador}-Nombre: {persona.get("nombre")} Apellido: {persona.get("apellido")} edad: {persona.get("edad")}")

#FORMA DE COMO TRABAJAR UNA LISTA CON EL DICCIONARIO
print("\n*** Sistema de Inventarios ***")

inventario = [] #SE CREA LISTA VACIA

cuantos = int(input("Cuantos productos desea agregar al inventario?: "))
for i in range(cuantos):
    print(f"Proporciona los valores del producto {i + 1}")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    productos = {"id": i, "nombre": nombre, "precio": precio, "cantidad": cantidad} #SE CREA UN DICCIONARIO
    inventario.append(productos)
print(f"Inventario: {inventario}")

#for i, producto in enumerate(inventario): MUESTRA MAS DATALLADO E INDEPENDIENTE LOS PRODUCTOS
#    print(f"{i}-Nombre: {producto.get("nombre")} Precio: {producto.get("precio")} Cantidad: {producto.get("cantidad")}")

id = int(input("\nIngresa el ID del producto a buscar: "))
encontrado = None
for producto in inventario:
    if producto.get("id") == id: #COMPARA EL ID CON EL NUMERO INGRESA EL USUARIO
        encontrado = producto
        break

if encontrado is not None:
    print("Producto encontrado") # SI EL ID ES CORRECTO TE MUESTRA LOS DATOS DEL PRODUCTO ELEGIDO
    print(f'''id:{encontrado.get("id")} 
    Nombre: {encontrado.get("nombre")}  
    Precio: ${encontrado.get("precio")} 
    Cantidad: {encontrado.get("cantidad")}''')
else:
    print(f"No se encontró el producto con el id: {id}") #SI EL ID ES INCORRECTO TE MENCIONA QUE NO SE ENCUENTRA

print("\n--- Inventario Detallado ---")
for id, lista in enumerate(inventario): #MUESTRA LOS DATOS INGRESADO DE LOS PRODUCTOS
    print(f'''id:{id} 
Nombre: {lista.get("nombre")} 
Precio: ${lista.get("precio")} 
Cantidad: {lista.get("cantidad")}''')

print("\n*** Compresion de lista ***")

numero = range(10+1) #
print(f"{numero}") #SE IMPRIME EL PARAMETRO, NO ES UNA LISTA

pares = [x for x in numero if x % 2 == 0] #RECORRER UNA LISTA DENTRO DE UNA VARIABLE USANDO UNA CONDICION
print(f"{pares}")

numeros = [0,1,2,3,4,5,6,7,8,9,10]
cuadrado = [x**2 for x in numeros]
print(f"{cuadrado}")

nombres = ["Nacho","Mati","Santi","Nahuelito"]
saludos = [f"Hola {nombre}" for nombre in nombres]
print(f"{saludos}")

