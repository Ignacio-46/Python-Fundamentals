#SENTENCIAS (IF/ELIF/ELSE)
#IF
edad = 30
if edad >= 18: #SE EJECUTA SI LA DECISION ES VERDADERA
    print(f"Eres mayor de edad tiene: {edad} años\n")
#ATRAS DEL PRINT FIGURA UN TABULADOR(ESPACIO)

#ELSE
edad = 10
if edad >= 18: #SE EJECUTA SI LA DECISION ES VERDADERA
    print(f"Eres mayor de edad tiene: {edad} años")
else: #SE EJECUTA SI LA DECISION ES FALSA O SI NO CUMPLE CON EL IF
    print(f"Eres menor de edad, tiene: {edad} años\n")

#ELIF
edad = 16
if edad >= 18: #SE EJECUTA SI LA DECISION ES VERDADERA
    print(f"Eres mayor de edad tiene: {edad} años")
elif 13 < edad < 18:
    print(f"Eres un adolescente, tiene: {edad} años\n") #SE EJECUTA SI ESTA "DENTRO DEL RANGO", ES VERDADERO
else: #SE EJECUTA SI LA DECISION ES FALSA O SI NO CUMPLE CON EL IF O ELIF
    print(f"Eres menor de edad, tiene: {edad} años\n")

#EJERCICIO SI UN NUMERO ES POSITIVO, NEGATIVO O CERO
numero = int(input("ingrese el numero: "))
if numero > 0:
    print(f"el numero es positivo: {numero}\n")
elif numero < 0:
    print(f"el numero es negativo: {numero}☻\n")
else:
    print(f"el numero es cero: {numero}\n")

#SE PUEDE APLICAR EL DIAGRAMA DE FLUJO PARA VER LA TOMA DE DESICIONES

#EJEMPLO DEL OPERADOR TERNARIO
print("*** Operador ternario ***")

edad = int(input("ingrese su edad: "))

es_adulto = "si" if edad >= 18 else "no"
print(f"Es adulto usted?: {es_adulto}")

#SOLO SIRVE SI EL CODIGO ES COMPACTO, ES DECIR MAS SENCILLO QUE SE PUEDA
#ESCRIBIR EN UNA SOLA LINEA. PORQUE SI EL CODIGO ES COMPLEJO, TE CONVIENE
#HACER EL IF/ELIF/ELSE.

