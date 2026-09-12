#FORMAS DE TRABAJAR CON LISTAS
#EJERCICIO 1: LISTA DE REPRODUCCION
print("*** Lista de Reproducción ***")

canciones = [] #LISTA VACIA
cantidad = int(input("Cuantas canciones desea agregar?: "))
for i in range(cantidad):
    cancion = input(f"Agregue su cancion favorita {i + 1}: ").strip().lower() # {i+1} ES PARA CUANTO SE VA AGREGANDO CADA ELEMENTO
    canciones.append(cancion)
    canciones.sort() #SE PUEDE PONER .SORT(REVERSE = True), ESTO HACE QUE LOS TEMAS SE ORDENA DE FORMA INVERSA
print(f"Mi lista de Canciones:\n{canciones}\n")
#SE ITERA LA CANCIONES DE ARRIBA A ABAJO, YA ORDENADA DE FORMA ALFABETICA
contador = 0
print("Mi lista de Canciones:")
for i in canciones:
    contador += 1 #SE UTILIZA EL CONTADOR PARA QUE VAYA DE FORMA ORDENA LOS NUMEROS Y SE VA CONTANDO
    print(f"{contador} - {i}\n")



#EJERCICIO 2: PROMEDIO DE CALIFICACIONES
print("*** promedio de Calificaciones ***")

calificacion = []
calificaciones = int(input("Proporciona el nro. de Calificaciones: "))

for i in range(calificaciones):
    proporcion = float(input(f"Calificacion[{i + 1}]: "))
    calificacion.append(proporcion)
print(f"Las Calificaciones proporcionadas:{calificacion}")

suma = 0
for i in range(calificaciones):
    suma += calificacion[i] #TAMBIEN SE PUEDE USAR SUM ES UNA FUNCION DE PYTHON Y REALIZA LA SUMA TOTAL
promedio = suma/calificaciones
print(f"Promedio de las Calificaciones: {promedio:.2f}\n")



#FORMA DE COMO TRABAJAR CON TUPLA
#UNPACKING (DESEMPAQUETADO DE TUPLAS)
print("*** Unpacking ***")

productos = ("P001", "camisa", 20.000)
id,discripcion,precio = productos
print(f"La Tupla completa:{productos}")
print(f"id: {id}, descripcion: {discripcion}, precio: {precio:.3f}")



#COMBINACION DE TUPLAS Y LISTAS
print("\n*** Unpacking 2 ***")
productos = [("P001", "camisa", 30.00),
             ("P002", "remera", 20.00), # SON TUPLAS DENTRO DE UNA LISTA
             ("P003", "sueter", 40.00)] #LAS TUPLAS NO MODIFICAN SUS ELEMENTOS

for producto in productos:
    print(f"{producto}") # SE IMPPRIME LAS TUPLAS

total = 0
for producto in productos: #LAS TUPLAS CONTENIDAS EN "PRODUCTO", PASAN A ESTAR EN DISTINTAS VARIABLES
    id,discripcion,precio = producto #ACA ES DONDE LOS ELEMENTOS SE VUELVE INDEPENDIENTE Y YA NO SON TUPLAS
    print(f"id: {id}, descripcion: {discripcion}, precio: ${precio:.2f}") #UNPACKING
    total += precio #SE PUEDE CALCULAR DENTRO DEL FOR
print(f"el precio total: ${total}")



