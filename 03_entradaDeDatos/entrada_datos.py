#CONVERSION DE DATOS

#LA CONVERSION TIPO ENTERO
numero = "10"
booleano = int(numero)
print(f"la conversion de numero es:{booleano}")

#LA CONVERSION TIPO FLOAT
numero1 = "3.14"
booleano = float(numero1)
print(f"la conversion de numero1 es:{booleano}")

#LA CONVERSION TIPO NUMERO A CADENA
numero2 = 1200
booleano = str(numero2)
print(f"la conversion de numero2 es:{booleano}")

#LA CONVERSION TIPO BOOLEANO
numero3 = 0
numero4 = 5
booleano = bool(numero3)
booleano1 = bool(numero4)
print(f"la coversion de numero3 es:{booleano}\nla conversion de numero4 es:{booleano1}")

#LA CONVERSION CADENA VACIA Y CON VALOR
numero5 = ""
numero6 = "numero 6 tiene valor"
booleano = bool(numero5)
booleano1 = bool(numero6)
print(f"el valor de booleano es:{booleano}")
print(f"el valor de booleano1 es:{booleano1}")

#LA CONVERSION TIPO NONE
numero5 = None
booleano = bool(numero5)
print(f"la conversion tipo none es:{booleano}\n")

#CONCATENACION DE CADENA
numero7 = "20"
numero8 = "30"
concatenar = numero7 + numero8
print(f"la  concatenacion de los numeros es:{concatenar}") #ES UNA CONCATENACION NO UNA SUMA ARIMETICA
#CONVERTIR DE CADENA A TIPO INT
numero9 = "20"
numero10 = "30"
suma = int(numero9)
suma1 = int(numero10)
resultado = suma + suma1
print(f"el resultado es:{resultado}\n") # AL CONVERTÍR LAS CADENAS A TIPO INT SE REALIZA LA OPERACION ARIMETICA

#ENTRADA DE DATOS CON INPUT
nombre = input("decime tu nombre:")
edad = input("decime tu edad:")
print(f"tu nombre es:{nombre} y tu edad es:{edad}")
#CONVERTIR LA CADENA DE ENTRADA A TIPO INT
edad1 = int(input(f"decime tu edad de nuevo:")) #CUANDO USA INT(INPUT("")) CONVIERTE LA CADENA EN VALOR NUMERICO
print(f"tu edad es:{edad1} y en 10 años tendras:{edad1 + 10} años\n")

#EJEMPLO DE COMO CONVERTIR DATOS
nombre = input("ingrese su nombre:")
edad2 = int(input("ingrese su edad:"))
salario = float(input("ingrese su salario:"))
jefe = input("es jefe de departamento:")
#COVERTIMOS LA VARIABLE JEFE EN TIPO BOOLEANO VERDADERO
jefe = jefe.lower() == "si"
print(f"su nombre es:{nombre}, su edad es:{edad2}, su salario es:${salario:.2f} mil y es jefe del departamento:{jefe}\n")
#{salario:.2f} NOS DARÁ DOS NÚMEROS DECÍMALES

#EJERCICIO DE RECETA DE COCINA
print("*** RECETA DE COCINA ***")

nombre = input("ingrese el plato:")
ingredientes = input("ingrese los ingredientes:")
preparacion = int(input("ingrese los minutos:"))
dificultad = input("su dificultad:")

print(f"nombre del plato:{nombre}")
print(f"los ingredientes son:{ingredientes}")
print(f"se tardará {preparacion} minutos")
print(f"la dificultad es:{dificultad}\n")

#GENERAR VALORES ALEATORIO
#VALORES ALEATORIO CON LA FUNCION RANDINT
#IMPORT RAMDON
from random import randint
#GENERA UN NUMERO ALEATORIO DE 1 A 10
randin = randint(1, 10)
print(f"el numero aleatorio entre 1 y 10:{randin}")
#simulacion de dados
dado = randint(1, 6)
print(f"lanza el dado:{dado}\n")

#EJERCICIO GENERADOR UNICO DE ID
from random import randint
nombre1 = input("ingresa tu nombre: ")
apellido = input("ingrese su apellido. ")
año = int(input("ingrese su año de nacimiento: "))
randin1 = randint(1,9999)

#año = anio.strip()[2:4]  no me funciona

print(f'''Hola {nombre1},
        tu numero de indentificacion (ID) generado por el sistema es:
        {nombre1.strip().upper()[0:2]}{apellido.strip().upper()[0:2]}{año}{randin1}
        Felicidades!!!\n''')

#EJERCICIO NUEVO GENERADOR DE EMAIL
nombre = input("ingrese su nombre:")
apellido = input(("ingrese su apellido:"))
empresa = input("ingrese el nombre de la empresa:")
extension = ".com.ar"
arroba = "@"
nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ", ".")
extension = extension.strip().lower().replace(" ","")
email = f"{nombre}.{apellido}{arroba}{empresa}{extension}"
print(f"{email}")

