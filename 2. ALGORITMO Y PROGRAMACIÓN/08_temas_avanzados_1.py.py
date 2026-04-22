from functools import reduce

#Compresion de listas
print("---*** Compresión de lista ***---")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Sin usar compresión de listas
#Filtrar números pares y genera una nueva lista con estos valores
numeros = range(1,11)
#sin usar una compresión de listas
numeros_pares = []
#Itermos cada elemento de una lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f"Iteramos numeros pares de 1 a 10: {numeros_pares}")

#Usando una compresión de listas
#sintaxis: nueva_listas = [expresión for elemento in iterable if condición]
#Usando compresión de listas
numeros_pares =  [numero for numero in numeros if numero % 2 == 0] #Se usa corchetes
#           [expresión for elemento in iterable if condición]
print(f"Iteramos numeros pares de 1 a 10: {numeros_pares}")

#[numero+1 for numero in numeros if numero % 2 == 0 ]
#[numero**2 for numero in numeros if numero % 2 == 0 ]
# en la expresión "numero" se puede sumar o elevar al cuadrado

#Funcion ZIP
#La función de zip itera la lista de varios elementos
print("\n---*** Función ZIP ***---")
nombres = ["Nacho","Santi","Mati","Nahuelito"]
edades = [34, 21, 32,  37]
ciudades = ["9 de julio", "Las Heras", "San jose", "Altube"]

personas = zip(nombres, edades, ciudades)
print(f"{personas}\n") #si se imprime solo te pone el zip (object) y no te muestra los datos
# se tiene que iterar con for y te devuelve las lista en forma de tuplas
for persona in personas:
    print(persona)

#Manejo de cadenas
print("\n---*** Manejo de cadenas ***---")

#split(): es dividir una cadena
palabra = "Hola Mundo"
palabras = palabra.split()
print(f"{palabras}")

#find(): Busca la posición(número) de la cadena
cadena = "Hola Mundo"
cadenas = palabra.find("Mundo") #devuelve el valor número 5 (es la posición)
print(f"Posición de la cadena: {cadenas}")

#replace(): Reemplaza la cadena vieja por una nueva
saludar = "Hola Mundo"
saludo = saludar.replace("Mundo", "Amigo")
print(f"Nueva cadena reemplazada: {saludo}")

#Multiplicacion de cadenas "*"
multiplicar = "Hola "
multiplica = multiplicar * 3
print(f"El resultado de la multiplicación: {multiplica}")

#strip(): Eliminas los espacio al principio y al final de la cadena
espacio = "   Hola Mundo   "
espacios = espacio.strip()
print(f"Elimina los espacios al principio y al final de la cadena: '{espacios}'")
#También elimina puntos y símbolos

#Funciones Lambda
#Son funciones pequeñas y temporales que se define en una sola línea
#lambda argumento: expresión

print("\n---*** Funciones Lambda ***---")

#Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f"El cuadrado sin lambda es: {cuadrado(5)}")

#Función cuadrado con lambda
cuadrado = lambda x : x ** 2
print(f"El cuadrado con lambda es: {cuadrado(2)}")
print(f"El cuadrado con lambda es: {cuadrado(4)}")

#Usando map():
#lista de numeros
numeros = [1, 2, 3, 4, 5]

#Aplicar una función lambda para obtener los numeros al cuadrado de cada número
cuadrado = list(map(lambda x : x ** 2, numeros))
print(f"Resultado de map y lambda: {cuadrado}")

#Usando filter()
pares = list(filter(lambda x : x % 2 == 0, numeros))
print(f"Resultado de usar filter para filtrar numeros pares: {pares}")

#reduce y map
#utilizamos la misma lista de numeros = [1,2,3,4,5]
suma_acumulativa = reduce(lambda x, y: x + y, numeros)
print(f"Suma acumulativa aplicando reduce: {suma_acumulativa}")


