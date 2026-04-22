print("*** Funciones Recursivas ***\n")

#LA FUNCION RECURSIVA TIENE COMO BASE 2 REGLAS
#LA PRIMERA ES LA FUNCION QUE SE LLAMA ASI MISMA
#LA SEGUNDA ES LA FUNCION QUE SE LLAMA ASI MISMA PERO DEBE AVANZAR A UN CASO BASE
#SINO CAE EN UN CICLO INFINITO

#EJEMPLO:
print("*** Imprimi del 1 al 5 de forma Recursiva ***")

def recursiva(numero):
    #CASO BASE
    if numero == 1:
        print(numero, end = " ")
    #CASO RECURSIVA
    else:
        print(f"{numero}", end = " ") #DE ESTA FORMA VUELVE A LA INVERSA
        recursiva(numero - 1)
        #print(numero, end = " ") #DE FORMA VA HACIA ADELANTE (NORMAL)

recursiva(5)
print("\n")

print("*** Factorial del numero 5 ***")

def factorial(numero):
    #CASO FACTORIAL DE 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f"El resultado factorial parcial del {numero} es 1")
        return 1
    else: #CASO FACTORIAL RECURSIVA
        factor = numero * factorial(numero - 1)
        print(f"El resultado factorial parcial del {numero} es: {factor}")
        return factor

numero = 5 #MODIFICAR CUALQUIER NUMERO
resultado = factorial(numero)
print(f"El factorial del {numero} es: {resultado}")

print("\n")

print("*** Potencia en funciones Recursivas ***")

def potencia(base, exponente):
    #CASO BASE
    if exponente == 0:
        return 1
    else: #CASO POTENCIA RECURSIVA
        return base * potencia(base, exponente - 1)

print(f"El 2 elevado a la 3 es: {potencia(2, 3)}")
print(f"El 5 elevado a la 0 es: {potencia(5, 0)}")
print(f"El 4 elevado a la 5 es: {potencia(4, 5)}")
