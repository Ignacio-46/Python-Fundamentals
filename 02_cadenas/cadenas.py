#CADENAS

cadena1 = "hola mundo" #CADENA TIPO STRING

#SE PUEDE GUARDAR UNA VARIABLE DENTRO DE OTRA
cadena2 = cadena1

caracter = cadena1[0] #SE RESCATA EL CARACTER SEGUN SU INDICE. POR EJ.: INDICE:0, LETRA:"H"

#SE IMPRIME USANDO PRINT(SE USA PARA MOSTRAR DATOS EN LA PANTALLA)
print(cadena1)
print(cadena2)
print(f"{caracter}\n")

#VARIABLE
cadena3 = '''se puede escribir el texto 
                en multiples lineas, utilizando
                    la variable cadena3'''#AL USAR TRIPLE COMILLAS SE PUEDE ESCRIBIR VARIAS LINEAS
#SE USA "TAB" (TABULAR) PARA CORRER LOS ESPACIOS
print(f"{cadena3}\n")

#CARACTERES ESPECIALES
print("hola \nmundo") # SALTO DE LINEA
print("Python \t \t \t es genial") #GENERA ESPACIOS, SE LO LLAMA TABULAR
print("estoy \'cansado\' jefe") #PARA USAR SIMPLES COMILLAS
print("anda nomas, \"nadie te detiene\"") #PARA USAR DOBLE COMILLAS
print("nahuelito \\ es un nahuelito\n") #PARA USAR UNA BARRA DIAGONAL

#CONCATENACION
cadena4 = "mama"
cadena5 = "ypapa"
concatenacion = cadena4 + cadena5
concatenacion1 = cadena4 + " " + cadena5 #LA DIFERENCIA ES QUE MUESTRA LOS ESPACIO ENTRE LAS CADENAS
print(concatenacion)
print(concatenacion1)

#concatenacion metodo join
cadena6 = "mama"
cadena7 = "y papa"
concatenacion2 = ''.join([cadena6," ",cadena7]) #ES LO MISMO NADA MAS QUE SE USA EL METODO JOIN
print(f"{concatenacion2}\n")

#FORMATO DE CADENAS "F"
# ESTO SE LO DENOMINA F-STRING
nombre = "santi"
edad = 20
mensaje = f"el nombre es {nombre} y su edad es {edad}" #LA F ES EL FORMATO Y LAS VARIABLES SE ESCRIBEN ENTRE {}
print(mensaje)

#METODO FORMAT "f"
mensaje = "el nombre es {} y su edad es {}".format(nombre, edad)
print(f"{mensaje}\n")

#METODOS DE CADENAS CON UPPER, LOWER Y STRIP
opcion1 = "metal slug 3" #PARA CONVERTIR EN MAYUSCULA
opcion2 = "SUNSET RAIDERS" #PARA CONVERTIR EN MINUSCULA
opcion3 = "     resident evil          " #PARA ELEMINAR LOS ESPACIOS AL INICIO Y AL FINAL
print("",opcion1.upper(),"\n",opcion2.lower(),"\n",opcion3.strip())
print(f"{opcion3}\n")#UN EJEMPLO DE NO USAR EL .STRIP()

#LARGO DE UNA CADENA CON .LEN() (LONGITUD)
frase = "cowboy bebop!!"
print(frase,"tiene",len(frase),"letras\n") #EL METODO LEN() CUENTA LOS CARACTERES, ESPACIOS, Y SIMBOLOS DE UNA FRASE

#SUBCADENA CON SLICING [0:10]
#EJ.: SUBCADENA = CADENA[INICIO : FIN]
palabra = "sonic, the hedgehog"
subcadena = palabra
print(f"quiero la primer subcadena de la palabra:{subcadena[0:5].upper()} y despues la segunda subcadena:{subcadena[11:19].upper()}\n")
#[] AL USAR ENTRE CORCHETES TE INDICA LA CADENA SEGUN SU INDICE, TAMBIEN CUENTA LOS ESPACIOS Y SIMBOLOS
#EJ.: S O N I C PALABRAS
#     0 1 2 3 4 INDICES [0:5]

#BUSCAR SUBCADENAS CON .FIND() (TE MUESTRA LOS INDICES)
SEGA = "sonic"
print(f"MOSTRA EL INDICE DEL SONIC:{SEGA.find("sonic")}\n")
#MARCA EL PRIMER INDICE DE CADA PALABRA

#REEMPLAZAR LAS SUBCADENAS CON .REPLACE()
SEGA = "SONIC THE HEDGEHOG"
print(SEGA)
print(f"ahora se va a llamar:{SEGA.replace("THE HEDGEHOG", "& NUCKLES")}\n")

#SEPARAR CADENAS CON .SPLIT()
super = "super mario"
print(f"el juego de nintendo es:{super.split()}\n") #POR DEFAULT SEPARA CADA ELEMENTO POR ESPACIO EN BLANCO

#MULTIPLICAR CADENAS
akira = "dragon ball z\n"
toriyama = 3
goku = akira * toriyama
print(goku)

#GENERADOR DE EMAIL: GENERE UN EMAIL A PARTIR DE LOS SIGUIENTES DATOS
nombre = "Nacho Roldan"
empresa = "    La Veranada     "
dominio = "com.ar"

#RESULTADO FINAL : EMAIL: IGNA.OCT.36@GMAIL.COM.AR

print(f'''El usuario:{nombre.replace("Nacho","Ignacio").split()}. 
Trabaja en una empresa de fumigacion llamada:{empresa.upper().strip()}
y su email es el siguiente:
{nombre.replace("Nacho Roldan", "igna.")}{nombre[4:5]}{nombre[2:3]}t.{nombre.find("ho")}{len("Roldan")}@gmail.{dominio}''')

#FIN DE CADENAS