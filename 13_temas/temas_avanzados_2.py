print("---*** Ordenamiento en Python ***---")
#Sorted(): Ordena cualquier iterable (listas, tuplas, cadena, etc.). Y devuelve la lista con los elementos ordenados
#Sintaxis: sorted(iterable, key= None, reverse= False)
                 #lista, función lambda, parametro

empleados = ["Nacho", "Santi", "Mati", "Nahuelito"]
#Ordenar la lista
empleados_ordenados= sorted(empleados)
print(f"Empleados ordenados: '{empleados_ordenados}'")
#Ordena en orden descendente, es decir al revés
empleados_ordenados= sorted(empleados, reverse=True) #Esto hace que vaya al revés
print(f"Empleados ordenados descendente: {empleados_ordenados}")

#Ordenar un diccionario (una llave)
dict_empleados = [{"Nombre" : "Nacho", "Salario" : 5000},
                  {"Nombre": "Santi", "Salario": 7000},
                  {"Nombre": "Nahuelito", "Salario": 6000},
                  {"Nombre": "Mati", "Salario": 3000}]

empleador_ordenado_salario = sorted(dict_empleados, key=lambda x: x["Salario"]) #La función key es una función lambda
print(f"Empleados ordenado por salario: '{empleador_ordenado_salario}'")

empleador_ordenado_salario = sorted(dict_empleados, key=lambda x: x["Salario"], reverse=True) #de forma inversa o descendente
print(f"Empleados ordenado por salario: '{empleador_ordenado_salario}'")

#Los Generadores: Crea iteraciones sencillamente, genera secuencias de valores de forma eficiente
# y nose necesita guarda todos lo valores en la memoria

#Yield(): Cuando se utiliza expresiones generadoras se utiliza yield. Cuando se llama una función generadora, este
#devuelve un objeto generador que puede ser iterado para obtener valores generados

print(f"\n---*** Generadores ***---")

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

var_generador = generador(5) #Se crea un Generador

for valor in var_generador:  #Iteramos sobre el generador
    print(valor)

#Las expresiones generadoras crean valores sobre la marcha parecido a compresión de listas pero se utilizan paréntesis
print(f"\n---*** Expresiones Generadoras ***---")

generador = (x**2 for x in range(10) if x % 2 == 0) #sintaxis: variable = (Expresión, Iteración, Condición)
for cuadrado_pares in generador:
    print(cuadrado_pares)

#Los decoradores modifican la funcionalidad de una funcion o metodo pero sin modificar su código.
#Permite envolver una función en otra función para agregarle funcionalidad adicional antes o después de que se llame su función original
#son de funciones de orden superior, es decir toma una función como argumento y devuelve otra función. Se declara usando "@"
print(f"\n---*** Decoradores ***---")

def decorador(funcion):
    def wrapper(*args, **kwargs): #Envuelve la función con los argumentos
        print("Antes de llamar la función saludar")
        resultados = funcion(*args, **kwargs)
        print("Después de llamar la función saludar")
        return resultados
    return wrapper

@decorador  #Decora en la variable 'resúltado'
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Nacho")

#Función sum() y next()
#sum(): suma los elementos iterable de las listas
print(f"\n---*** Funcion sum y next ***---")

lista = [1,2,3,4,5]

resultado = sum(lista) #suma de todo los elementos
print(f"Resultado de la suma es: {resultado}")
resultado = sum(lista,20) #Se puede proponer un valor inicial
print(f"Resultado de la suma con valor inicial de 20: {resultado}")

#next(): Obtiene el siguiente elemento del iterador
iterador = iter(lista) #iter: Es el objeto que quiere obtener el siguiente elemento
#Obtenemos el proximo elemento del iterador usando la funcion 'next()'
print(f"El siguiente elemento iterable es: {next(iterador)}") #1
print(f"El siguiente elemento iterable es: {next(iterador)}") #2
print(f"El siguiente elemento iterable es: {next(iterador)}") #3
print(f"El siguiente elemento iterable es: {next(iterador)}") #4
print(f"El siguiente elemento iterable es: {next(iterador)}") #5
#print(f"El siguiente elemento iterable es: {next(iterador)}") Si se realiza más iteraciones superando los elementos de la lista te tira error

#Excepciones: Son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de ejecución del código
#cuando se genera una excepción se utiliza 'try', 'except', 'else' y 'finally'.
print("\n---*** Manejo de Excepciones ***---")

def dividir(nominador, denominador):
    try: #El bloque try ejecuta si hay una excepción
        if denominador == 0:
            raise Exception("El denominador es igual a 0") #raiser arroja o lanza nuestras propias excepciones
        resultados = nominador / denominador
        print(f"La division es: {resultados}")
    except Exception as e:                    # Exception ejecuta todos los mensajes genéricos
        print(f"Ocurrio un error: {e}.")
    else:                                     #El else ejecuta el mensaje todo lo contrario del Exception
        print(f"No ocurrio ningún error.")
    finally:
        print("Terminamos de procesar la excepción.\n") #Finally ejecuta el mensaje con o sin Exception
   #except ZeroDivisionError: identifica el error de que no se puede dividir por cero
   #     print("No se puede dividir por cero")
   #except TypeError: Te muestra el error si es de tipo una cadena o string
   #     print("El valor tiene que ser numérico")

#Ejemplo de uso:
dividir(10, 5)
dividir(10, 0)
dividir(10, "0")