#FUNCIONES
#LAS FUNCIONES SON BLOQUES DE CODIGOS QUE REALIZAN UNA DETERMINADA TAREA
#EJ. DE UNA FUNCION
print("*** funciones en python ***")

def saludos(): #SE LE PONE NOMBRE DE LA FUNCION

    print("Saludos desde Python!!") #CUERPO DE LA FUNCION, SE PUEDE REALIZAR CUALQUIER TIPO DE EJERCICIO

saludos() #SE LLAMA A LA FUNCION
saludos() #SE LO PUEDE LLAMAR VARIAS VECES
saludos()

def saludar(mensaje): #DENTRO DEL PARENTESIS SE INDENTIFICA COMO PARAMETRO
             #EL PARAMETRO SE PUEDE PONER LA VARIABLE LAS VECES QUE QUIERAS EJ. SALUDAR(MENSAJE, PARAMTR1, PARAMTR2,ECT.)
    print(f"{mensaje}") #TRASMITE EL MENSAJE

saludar("\nHOLA A TODOS!!")

#SUMAR EN FUNCION (CREAR UN ARCHIVO LLAMADO funciones Y COLOCA ESTO)
def sumar(a, b):
    resultado = a + b #SE REALIZA LA OPERACION DE LA SUMA DENTRO DE LA VARIABLE
    return resultado #EL RETURN HACE RETORNAR LA VARIABLE YA DEFINIDA DENTRO DE LA FUNCION

#NO COLOCAR ESTO
resultado_final = sumar(8, 5) #SUMAR ES LA FUNCION YA DEFINIDA
print(f"\nEl resultado de la suma es: {resultado_final}")

#MODULO DE LA FUNCION
#REALIZA UN IMPORTE DE LA FUNCION DE UN ARCHIVO HACIA OTRO
#import modulo_funcion_sumar #ES UN ARCHIVO DONDE TIENE UNA FUNCION Y LO ESTA IMPORTANDO HACIA OTRO ARCHIVO
#from modulo_funcion_sumar import sumar (FORMA MAS RECOMENDADA)
#   NOMBRE DEL ARCHIVO  |  IMPORTANDO LA FUNCION

#CREA OTRO ARCHIVO LLAMADA sumar Y COLOCA ESTO
#from funciones import sumar(NO OLVIDES DE COLOCAR ESTO, EL IMPORT)
print(__name__)
if __name__ == "__main__": #SE PONE ESTA CONDICION PARA QUE NO SE MEZCLEN LA INFORMACION ENTRE LOS ARCHIVOS
    resultado_final = sumar(9, 15) #DENTRO DEL PARENTESIS SE COLOCA LOS NUMEROS Y REALIZA LA SUMA AUTOMATICAMENTE
    print(f"El resultado de la suma es: {resultado_final}")
#RESULTADO_FINAL ES LA VARIABLE QUE CONTIENE LA FUNCION SUMAR

print("\n*** argumentos por nombres ***")

def persona(nombre,apellido = "",edad = 0): #SI EL APELLIDO Y LA EDAD SE LE SACA ESOS VALORES, FIGURA ERROR
    print(f"nombre = {nombre} apellido = {apellido} edad = {edad}")

#SE LLAMA A LA FUNCION PERSONA
#ESTE SOLO SE UTILIZA COLOCANDO LOS VALORES
persona("Ignacio","Roldan",33)
#ESTE SE UTILIZA COLOCANDO LOS ARGUMENTOS CON SUS VALORES
persona(nombre = "Ignacio", apellido = "Roldan", edad = 33)
#SE INTERCAMBIA LOS ARGUMENTO PERO NO SE MODIFICA NADA EN SU FUNCION, ES DECIR, SIGUE IGUAL
persona(edad = 33, apellido = "Roldan", nombre = "Ignacio")
#ARGUMENTOS POR DEFAULT
#EN ESTE SOLO FIGURA EL VALOR DEL NOMBRE
persona(nombre = "Ignacio")
#ACA APARECE EL VALOR DEL NOMBRE Y EL VALOR DEL APELLIDO
persona(nombre = "Ignacio", apellido = "Roldan")
#SE INTERCAMBIA DE LUGAR PERO NO CAMBIA SU FUNCION
persona(apellido = "Roldan", nombre = "Ignacio")

print("\n*** regresar los valores en una tupla desde una funcion ***")

def persona_mayuscula(nombre,apellido,edad):
    print(f"esta funcion regresa varias valores (tupla)")
    return nombre.upper(), apellido.upper(), edad #UPPER() HACE QUE LA CADENA SE PONGA EN MAYUSCULA

#PROGRAMA PRINCIPAL (UNPACKING)
nombre,apellido,edad = persona_mayuscula("ignacio", "roldan", 33) #TRASMITE EL ARGUMENTO EN VARIABLES INDEPENDIENTES
print(f"El resultado de la persona: nombre = {nombre} apellido = {apellido} edad = {edad}")

print("\n*** Coordenadas ***")
def coordenadas():
    x,y,z = 10,20,30
    return x,y,z

resultado = coordenadas()
print(resultado) #ES UNA TUPLA

#UNPACKING DE LA TUPLA
x1,y1,z1 = coordenadas()
print(f"coordenada de x: {x1} coordenada y: {y1} coordenada: {z1}")
#LAS VARIABLES SE VUELVEN INDEPENDIENTE


