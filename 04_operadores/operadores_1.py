#OPERACION ARIMETICA

#TAMBIEN SIRVE PARA RESTA, MULTIPLICACION Y DIVISION
a = 10
b = 3
suma = a + b
print(f"la suma:{suma}")

#ASI SE SACA EL MUDULO(%), DIVISION PARTE ENTERA(//), Y POTENCIA (**)
division_entera = a // b
modulo = a % b
potencia = a ** b
print(f"la division entera:{division_entera}\nel modulo:{modulo}\npotencia:{potencia}\n")


#ASIGNACION MULTIPLE
a,b,c = 5, 10, 15
print(f"{a}, {b}, {c}")
#ASIGNACION ENCADENADA
x = y = z = 10
print(f"{x}, {y}, {z}\n")

#INTERCAMBIO DE VALORES
c,d = 10, 5
c,d = d,c
print(f"{c, d}")
print(f"{d, c}\n") #SE PONE ENTRE PARENTESIS

#RECIBI MULTIPLES VALORES DEL USUARIO
nombre, apellido = input("ingrese su nombre y apellido: ").split(",") #INGRESA NOMBRE, APELLIDO
print(f"{nombre.strip()}, {apellido.strip()}\n")
#ESTO HACE QUE LE PIDA AL USUARIO QUE INGRESE LOS DATOS CON UNA COMA

#OPERADOR COMPUESTO (+= / -= / *= / /= / %= / //= / **=)
a = 10
b = 15
a += b # a = a + b ES LO MISMO
print(f"la suma entre a y b es: {a}\n")
#FUNCIONA CON LA RESTA, MULTIPLICACION, DIVISION, MODULO, POTENCIA

#OPERADOR DE COMPARACION (RELACIONES)
# (== / != / > >= / < <=)
a,b = 15,10 #CAMBIA DE NUMERO PARA COMPARAR
print(f"a es igual a b:{a == b}")
print(f"a es distinto de b:{a != b}")
print(f"a es mayor que b:{a > b}")
print(f"a es mayor e igual a b:{a >= b}")
print(f"a es menor que b:{a < b}")
print(f"a es menor e igual a b:{a <= b}\n")

#OPERADORES LOGICOS(AND / OR / NOT)

#OPERADOR AND (AMBOS VALORES TIENEN QUE SER VERDADERO)
# SI ES FALSE AND FALSE SEGUIRA SIENDO FALSE
condicion1 = False # TRUE / FALSE / TRUE
condicion2 = False #TRUE / TRUE ( FALSE
resultado = condicion1 and condicion2
print(f"ambas condiciones presenta:{resultado}\n")
#EJERCICIO CON EL OPERADOR AND
#SISTEMA CON DESCUENTO VIP
compras = int(input("cuanto productos ha comprado en el dia?: "))
miembro = input("cuenta con la membresia de la tienda?: ")
tienda = compras >= 10 and miembro == "si"
print(f'''tiene el descuento VIP: {tienda}\n''')

#OPERADOR OR (ES VERDADERO SI CUALQUIERA DE LOS DOS ES VERDADERO)
#SI ES FALSE OR FALSE SEGURIRA SIENDO FALSE
condicion1 = True # TRUE / FALSE / TRUE
condicion2 = False #TRUE / TRUE ( FALSE
resultado = condicion1 or condicion2
print(f"ambas condiciones presenta:{resultado}\n")

#EJERCICIO CON EL OPERADOR OR
#SISTEMA PRÉSTAMO DE LIBROS
lugar = int(input("A cuanto km vive de la biblioteca?: "))
crendencial = input("Tiene crendencial?: ")
biblioteca = lugar <= 3 or crendencial == "si"
print(f'''Prestamo de libro: {biblioteca}\n''')

#OPERADOR NOT(NEGACION)
condicion1 = True #NOT = FALSE
condicion2 = False #NOT = TRUE
resultado = not(condicion1)
resultado1 = not(condicion2)
print(f"La condicion 1 presenta: {resultado}\nLa condicion 2 presenta: {resultado1}\n")

