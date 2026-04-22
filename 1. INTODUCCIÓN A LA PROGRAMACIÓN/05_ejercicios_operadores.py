#GENERACION DE TICKETS DE VENTAS
producto1 = input("ingrese el producto 1: ")
precio1 = float(input("ingrese su precio: "))
producto2 = input("ingrese el producto 2: ")
precio2 = float(input("ingrese su precio: "))
producto3 = input("ingrese el producto 3: ")
precio3 = float(input("ingrese su precio: "))

suma = precio1 + precio2 + precio3 #SUMA TOTAL DE LOS PRECIOS
impuesto = 0.15 * suma #SE MULTIPLICA SI ES IMPUESTO A LA SUMA TOTAL
descuento = suma * 10 / 100 #SE REALIZA EL DESCUENTO DE LA SUMA(REGLA DE 3 SIMPLES)
suma_descuento = suma - descuento #UNA VEZ A REALIZADA EL DESCUENTO, VOLVES A RESTAR LA SUMA TOTAL CON EL DESCUENTO
compra = suma_descuento + impuesto #SE SUMA DESCUENTO + IMPUESTO PARA EL TOTAL DE LA COMPRA

print("***Tickect de Compra***")
print("-----------------------")
print(f"{producto1.strip().lower()}\t\t{precio1}")
print(f"{producto2.strip().lower()}\t\t{precio2}")
print(f"{producto3.strip().lower()}\t\t\t{precio3}")
print(f"Impuesto(15%)\t{impuesto:.2f}")
print("-----------------------")
print(f"Descuento(10%)\t{descuento:.2f}")
print("-----------------------")
print(f"Total          \t{compra:.2f}\n")

#SISTEMA DE AUTENTICACION
usuario = input("ingrese su usuario: ")
password = input("ingrese su contraseña: ")
usuario = usuario == "nacho"
password = password == "roldan"
print(f"Los datos son:{usuario and password}\n")

#VALOR DENTRO DEL RANGO
valor = int(input("ingrese el valor: "))
valor_min = 0
valor_max = 5
rango = valor >= valor_min and valor <= valor_max
print(f"el valor ingresado es:{valor}\nestá dentro del rango:{rango}\n")

#CALCULO DE AREA Y PERIMETRO DE UN RECTANGULO
base = float(input(f"ingrese la base del rectagulo: "))
altura = float(input(f"ingrese la altura del rectagulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"El area del rectagunlo es:{area:.2f}\nEl perimetro del ractagulo es:{perimetro:.2f}")




