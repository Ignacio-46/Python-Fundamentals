#CICLOS (WHILE / FOR)

#CICLO WHILE
#UNA ESTRUCTURA DE CONTROL QUE REPITE INSTRUCCIONES HASTA QUE CUMPLA LA CONDICION VERDADERA
print("*** CICLO WHILE ***\n")
contador = 1 #ES UNA VARIABLE QUE SIRVE PARA SUMAR LOS ELEMENTOS, NUMEROS, ETC.
while contador <= 3: #SI COMPLE O SI ES VERDADERA LA CONDICION
    print(contador,"\n") #IMPRIME
    contador += 1 #SE ELEMINA EL 1 Y PASA SER 2 Y VUELVE A EVALUAR LA CONDICION
#EJEMPLO DE EJERCICIO WHILE
condicion = 1
while condicion <= 5:
    print(condicion, end = " ")#EL PARAMETRO END HACE QUE LOS NUMEROS CORRAN EN UNA SOLA LINEA
    condicion += 1 #condicion = condicion + 1 - ES LO MISMO Y FUNCIONA IGUAL QUE LA CONDICION += 1

#VALIDACION CAMPO DE FORMULARIO CON WHILE
usuario = None
while not usuario:
    usuario = input("\n\nIngrese el nombre de usuario: ")
print(f"El nombre del usuario es: {usuario}\n")

#CICLO FOR
#ITERA UNA SECUENCIA DE VALORES, COMO UNA LISTA O CADENAS Y EJECUTA UN BLOQUE DE CODIGO
#POR CADA ELEMENTO DE LA SECUENCIA
print("*** CICLO FOR ***\n")
cadena = "hola mundo"
for letra in cadena: #SE ITERA LOS CARACTERES DE CADENA EN LA VARIABLE LETRA
    print(letra, end = " ")

print("\n\nse corre una lista de frutas:")
frutas = ["pera", "manzana", "mandarina"] #ES UNA LISTA
for fruta in frutas: # SE VUELVE A ITERAR EL CONTENIDO DE FRUTAS EN LA VARIABLE FRUTA
    print(fruta, end = " ")

#FUNCION RANGE EN FOR:
#*** LA FUNCION RANGE ***
#LA FUNCION RANGE ES UN PARAMETRO, QUE SIRVE PARA CUANTAS VECES VAS ITERAR
#EJEMPLO: RANGE(0,5,1)
# RANGE(INICIO,FIN,INCREMENTO)
#INICIO = 0 (OPCIONAL, TAMBIEN SE PUEDE PONER DESDE 1 O EL NUMERO DONDE QUIERAS ARRANCAR)
#FIN = 5 - 1 = 4 (ES DECIR ARRANCA DESDE CERO, POR ENDE, FIGURA 0,1,2,3,4)
#INCREMENTO = 1 (OPCIONAL, TAMBIEN SE PUEDE PONER EL NUMERO QUE QUIERAS INCREMENTAR)

print("\n")
print("funcion range:")
for i in range(5): #SI COLOCAS UN NUMERO SE TIENE EN CUENTA EL FIN
    print(i, end = " ")
print("\n")
for i in range(0,10,2): #EL INCREMENTO SE CUENTA DE 2 EN 2
    print(i, end = " ")
print("\n")
for i in range(10, 20 + 1): #EL (20 + 1) ES EL INCREMENTO = 1 (VALOR POR DEFAULT Y ES OPCIONAL)
    print(i, end = " ")     #TAMBIEN DIRECTAMENTE ES VEZ DE COLOCAR (20 + 1), SE COLOCA 21, AMBOS SON VALIDOS.
print("\n")

#REPITICION DE MENSAJE
mensaje = input("Ingrese el mensaje: ")
iterar = int(input("Cuantas veces queres repetir: "))
for i in range(iterar): #LA i (INDICE) SIEMPRE ARRANCA DESDE CERO
    print(f"{i+1} - {mensaje}\n") #PARA QUE EMPIECE DESDE EL 1 SE COLOCA: "{i+1}"
#SI NO QUERES USAR i SE PONE UN GUIO BAJO (_) EN SU LUGAR Y NO TE MUESTRA
#EL INDICE O LA CANTIDAD DE REPITICIONES. EJ.: "for _ in range (iterar):"
#                                                      print(mensaje)

#DIBUJO DE UN TRIANGULO
print("*** triangulo simetrico ***")
numero = int(input("Proporciona un numero de filas: "))
for fila in range(1,numero + 1):
    espacio = " " * (numero - fila)
    asterisco = "*" * (2 * fila - 1)
    print(f"{espacio}{asterisco}")

#BREAK Y CONTINUE
print("\n*** break ***")
for numero in range(1, 10):
    if numero % 2 == 0:
        print(numero)
        break #HACE CORTAR LA ITERACION

print("*** continue ***")
for numero in range(1, 10):
    if numero % 2 == 1: #NUMERO IMPAR
        continue #HACE CONTINUAR LA ITERACION
    print(numero) #NUMERO PAR

#EJEMPLO DE UN EJERCICIO(LA CANTIDAD DE VOCALES)
cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print(contador)