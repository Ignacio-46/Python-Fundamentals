#EJERCICIO 5: VALIDACION DE CONTRASEÑA
inicio = 0
while inicio != 1:
    password = input("ingrese su password: ")
    contraseña = "roldan"
    if password == contraseña:
        print(f"Password valido: {password}")
        break
    elif len(password) <= 6:
        print(f"Su contraseña tiene que tener al menos 6 caracteres")
    else:
        print(f"ERROR. Vuelva ingresar su contraseña")

#EJERCICIO 6: JUEGO DE ADIVINANZA
adivinanza = input('''      **** ADIVINANZA ****
   Elige un numero del 1 a 50!!
    si \'GANÁS\' eres el mejor
    pero pero pero pero pero
    si perdes recibiras una 
     \'PATADA EN EL CULO\'
       LISTO!!? presioná:
      ------       ------
      | si |   o   | no |
      ------       ------\n''')
adivinanza = adivinanza.strip().lower() == "si"
import random
secreto = random.randint(1, 50)
intentos = 9
intentos1 = 1

inicio = 0
while inicio != 1:
    if adivinanza:
       print("OK")
    else:
       print("ANDATE A LA MIERDA BIGOTE!!\n")
       break
    numero = int(input("Elegi un numero dale de 1 a 50: "))
    while numero <= 0 or numero >= 51:
            numero = int(input("Sos boludo de 1 a 50...DIJE!!: "))

    if numero == secreto:
        print(f"\nFelicidades GANASTE!!\n"
              f"LO HICISTE EN {intentos1} INTENTOS\n"
              f"TE QUEDABA {intentos} INTENTOS\n"
              f"EL NUMERO SECRETO ERA: {secreto}\n")
        break

    if numero >= 1 or numero >= 51:
        intentos1 += 1
        intentos -= 1
        if intentos > 0:
            print(f"FALLASTE!!. Te queda {intentos} intentos.")
            if numero <= secreto:
                print(f"Fijate capaz el numero sea mayor al {numero}\n")
            if numero >= secreto:
                print(f"Fijate capaz el numero sea menor al {numero}\n")

    if intentos == 0:
        print("AAAAAYYY QUE LASTIMA!! SOS RE TRUCHO JAJAJAJ!!\n")
        inicio = 1

