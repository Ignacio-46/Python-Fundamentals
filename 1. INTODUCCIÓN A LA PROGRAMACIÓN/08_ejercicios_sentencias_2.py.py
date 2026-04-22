#EJERCICIO 6: EL MAYOR DE 2 NUMEROS
num = int(input("Ingrese el primer numero entero: "))
num1 = int(input("Ingrese el segundo numero entero: "))

print(f"Los numeros ingresados para comparar:\n\t\t {num} = {num1}")

if num > num1:
    print(f"el primer numero es el mayor: {num}\n")
else:
    print(f"el segundo numero es el mayor: {num1}\n")

#EJERCICIO 7: ESTACION DEL AÑO
mes = int(input(f"ingrese el mes para saber la estacion del año: "))

if mes == 1 or mes == 2 or mes == 12:
    print(f"La estacion del año es Invierno\n")
elif mes == 3 or mes == 4 or mes == 5:
    print(f"La estacion del año es Primavera\n")
elif mes == 6 or mes == 7 or mes == 8:
    print(f"La estacion del año es Verano\n")
elif mes == 9 or mes == 10 or mes == 11:
    print(f"La estacion del año es Otoño\n")
else:
    print(f"Estacion desconocida\n")

#EJERCICIO 8: SISTEMA DE CALIFICACIONES
calificaciones = int(input("ingrese la calificacion entre 0 y 10: "))

if calificaciones >= 9 and calificaciones < 10:
    print(f"La calificacion ingresada {calificaciones} es: A\n")
elif calificaciones >= 8 and calificaciones < 9:
    print(f"La calificacion ingresada {calificaciones} es: B\n")
elif calificaciones >= 7 and calificaciones < 8:
    print(f"La calificacion ingresada {calificaciones} es: C\n")
elif calificaciones >= 6 and calificaciones < 7:
    print(f"La calificacion ingresada {calificaciones} es: D\n")
elif calificaciones >= 0 and calificaciones < 6:
    print(f"La calificacion ingresada {calificaciones} es: F\n")
else:
    print(f"VALOR DESCONOCIDO\n")

#EJERCICIO 9: SISTEMAS DE ENVIO
destino = input("Ingrese el destino del paquete (Nacional/Internacional): ")
peso = float(input("Ingrese el peso del paquete (en kg): "))

costo = 10 * peso
costo1 = 20 * peso

if destino == "Nacional":
    print(f"El destino del envio sera: {destino}\nSu costo es: ${costo:.2f}\n")
elif destino == "Internacional":
    print(f"El destino del envio sera: {destino}\nSu costo es: ${costo1:.2f}\n")
else:
    print("Destino no valido\n")

#EJERCICIO 10: SISTEMA DE AUTENTICACION
print("------*** Sistema de Autenticacion ***------")
usuario = input("Usuario: ")
password = input("Password: ")

usuario = usuario.strip().lower() == "nacho"
password = password.strip().lower() == "roldan"

if usuario and password:
    print("Bienvenido al Sistema\n")
elif password:
    print("Usuario Invalido\n")
elif usuario:
    print("Password Invalido\n")
else:
    print("Usuario y Password Invalidos\n")

print("--------------------------------------------\n")

