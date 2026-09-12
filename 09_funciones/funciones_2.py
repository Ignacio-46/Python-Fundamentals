print("\n*** Alcanze de Variables ***")

#PUEDE SER GLOBAL O LOCAL DEPENDIENDO DE DONDE SE DECLARE
#GLOBAL: ALCANZA A LO LARGO DE TODO EL PROGRAMA
#LOCAL: DISPONIBLE DENTRO DE UN BLOQUE O DE UNA FUNCION DECLARADA

contador_global = 0 #SE DEFINE LA VARIABLE GLOBAL

def alcanze():

    contador_local = 0 #SE DEFINE LA VARIABLE LOCAL

    global contador_global #PARA USAR LA VARIABLE GLOBAL SE TIENE QUE USAR "GLOBAL"

    contador_global += 1 #SE REALIZA EL CONTEO
    contador_local += 1

    print(f"\ncontador local: {contador_local}") # SE IMPRIME EL CONTEO
    print(f"contador global: {contador_global}")

alcanze()
alcanze() #A MEDIDA QUE SE LLAMA MAS FUNCIONES, SE SUMA EL CONTEO
alcanze()

print(f"\nEl contador global es: {contador_global}") #QUEDA FIJO EL NUMERO TOTAL DEL CONTEO

print("\n*** Argumentos de Variables ***")
#LOS ARGUMENTOS SE DEFINEN COMO UN TUPLA
def comics(superheroe, nombre, *args): #LOS ARGUMENTOS SIEMPRE VAN AL FINAL DE LOS PARAMETROS Y LLEVA UN *
    print(f"Super heroe: {superheroe} nombre: {nombre} poder: {args}") #NO ES NECESARIO USAR EL * PARA DECLARAR
    for comic in args:
        print(f"Superpoder: {comic}")

comics("Spiderman", "Peter Parker","Insticto Aracnido","Teleraña")
comics("Batman", "Bruce","Combate","Boomeran murcielago","Batimovil")
comics("Mujer Maravilla", "no me acuerdo") #AL NO TENER ARGUMENTO TE TIRA SOLAMENTE LA TUPLA VACIA
#LOS ARGUMENTOS NUNCA PUEDEN IR AL PRINCIPIO DEL PARAMETRO DE LA FUNCION PORQUE TE FIGURA ERROR
#EJ.: def comics(*args, superheroe, nombre): #NO FUNCIONA

#*arg - argumentos - tupla
#**kwargs - keyword argumentos (key, value) como diccionario
#LOS **KWARGS SE DEFINEN COMO DICCIONARIO
print("\n*** Argumentos en variables en forma de diccionario ***")
#LOS **KWARGS SIEMPRE VA A FINAL DEL PARAMETRO
def marvel(nombre, *args, **kwargs):
    print(f"Nombre: {nombre} - {args} mas info: {kwargs}") # NO SON NECESARIOS USAR LOS ** PARA DECLARAR

marvel("Flash","velocidad", edad = 20, empresa = "Marvel") # SE DECLARA DE ESTA FORMA
marvel("Mi vecino") # SINO SE USA LOS ARGS Y KWARGS, TE MUESTRA LA TUPLA VACIA Y EL DICCIONARIO VACIO

print("\n*** Sumar Variables con Argumentos ***")

def suma(*args):
    total = 0
    for numeros in args: #SE PUEDE USAR LOS ARGS EN FOR Y PASARLO EN OTRA VARIABLE YA QUE ES TUPLA
        total += numeros #UNA VEZ QUE LOS ARGS PASAN A LA VARIABLE NUMEROS, ESTE SE VUELVE INDEPENDIENTE
    return total

resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(f"La suma total es: {resultado}")

print("\n*** Se imprime la persona usando **kwargs ***")

def persona(**kwargs):
    print(f"Los valores de la persona:")
    for la_persona, valor in kwargs.items(): #AL USAR EL .ITEMS() DEVUELE LA CLAVE Y LOS VALORES
        print(f"{la_persona} - {valor}") # DE FORMA UNPACKING

persona(nombre = "Nacho", edad = 33, trabajo = "Fumigacion", estudio = "Analista de Sistema")
#SE PUEDE PONER CIERTA CANTIDAD DE VALORES QUE QUIERAS

print("\n*** Funcion Par ***")

def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese el numero: "))
print(f"El numero es Par? : {par(numero)}")
