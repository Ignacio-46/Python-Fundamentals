#EJERCICIO 1: SISTEMA DE DESCUENTOS
compra = float(input("cual es el monto de tu compra?: "))
tienda = input("Eres miembro de la tienda(si/no): ")

descuento = compra * 10/ 100
descuento1 = compra * 5/ 100
descuento2 = compra * 3 / 100
total = compra - descuento
total1 = compra - descuento1
total2 = compra - descuento2
tienda = tienda.strip().lower() == "si"

if compra > 1000 and tienda:
    print(f"Felicidades tienes un descuento del 10%!!\nTu compra fue por: ${compra:.2f}")
    print(f"Tu descuento es: {descuento:.2f}")
    print(f"Total de tu compra es: {total:.2f}\n")
elif compra < 1000 and tienda:
    print(f"tienes un descuento del 5!!\nTu compra fue por: ${compra:.2f}")
    print(f"Tu descuento es: {descuento1:.2f}")
    print(f"Total de tu compra es: {total1:.2f}\n")
elif compra > 1000:
    print(f"tienes un descuento del 3%!!\nTu compra fue por: ${compra:.2f}")
    print(f"Tu descuento es: {descuento2:.2f}")
    print(f"Total de tu compra es: {total2:.2f}\n")
else:
    print(f"No eres miembro, te invito a que lo seas!!\nTu compra fue por: ${compra:.2f}\n")

#EJERCICIO 2: SISTEMA BANCARIO
sistema = input("desea continuar dentro del sistema (si/no): ")
if not sistema == "si":
    print(f"continuamos dentro del sistema\n")
else:
    print("salimos del sistema\n")

#EJERCICIO 3: LA CASA DE LOS ESPEJOS
casa = input("Le tiene miedo a la oscuridad?: ")
edad = int(input("Cuantos años tiene?: "))

if not edad <= 10 and casa == "no":
    print(f"puedes ingresar a la casa\n")
else:
    print("Te puede dar miedo\n")

#EJERCICIO 4: APLICACIÓN DE SALUD Y FITNESS
nombre = input("ingrese su nombre: ")
pasos = int(input("ingrese los pasos caminados en el dia: "))

meta = 10000
calorias = 0.04
quema = pasos * calorias
alcanzó = pasos >= meta
alcanzó = "si" if alcanzó else "no"
print(f"Nombre: {nombre}: Meta: {meta}. Realizo: {pasos} pasos. Supero la meta: {alcanzó}. Calorias: {quema:.2f} kc\n")

#EJERCICIO 5: SISTEMA DE RESERVACION DEL HOTEL
print("---------------------------------------")
print("*** Sistema de Reservacion de Hotel ***")
print("---------------------------------------")
nombre = input("Cual es su nombre?: ")
dias = int(input("Cuantos dias deseaba hospedarse?: "))
vista = input("Quiere un cuarto con vista al mar (si/no)?: ")

mar = 190.50
no_mar = 150.50
estadia = mar * dias
estadia1 = no_mar * dias

print("------- Ticket Reserva de Hotel -------")

vista = vista.strip().lower() == "si"
estadia = estadia if vista else estadia1
vista = "si" if vista else "no"

print(f"Nombre: {nombre}")
print(f"Estadia: {dias} dias")
print(f"Costo: ${estadia:.2f}")
print(f"Con vista al mar: {vista}")

print("---------------------------------------")