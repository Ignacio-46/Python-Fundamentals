# COLECCIONES SE BASA UNA ESTRUCTURA DE DATOS ORGANIZADOS POR VARIOS METODOS:
#LISTA
#TUPLAS
#SET(CONJUNTOS)
#DICCIONARIO

#LISTAS
#LAS LISTA SON ESTRUCTURAS DE DATOS ORGANIZADOS
#LAS LISTA PUEDEN SER NUMEROS ENTEROS O FLOAT, CADENAS, LISTAS DENTRO DE OTRA LISTA(sublista)
#SON REPRESENTADOS CON CORCHETES []

#MANEJO DE LISTAS
numero = [1,2,3,4,5]
frutas = ["manzana","pera","mandarina"]
tipos = [1,"sopa",3.0,[4,5]]

mi_lista = [1,2,3,4,5]                          #INDICE =  0  1  2  3  4 SIEMPRE ARRANCA DESDE CERO
print(f"{mi_lista} -> lista original")           #NUMERO = [1, 2, 3, 4, 5]
print(f"la longitud de la lista: {len(mi_lista)}") #LA FUNCION LEN() MIRA A LO LARGO DE LA CADENA
print(f"saca el valor por indice:{mi_lista[4]}") #CORRE EL INDICE DE IZQ A DER
print(f"sacamos el ultimo indice:{mi_lista[-1]}") #CORRE EL INDICE DE DER A IZQ

#MODIDICAR LOS ELEMENTOS EN LA LISTA
mi_lista[1] = 10 #SE MODIFICA UN ELEMENTO SIEMPRE Y CUANDO INDIQUE SU INDICE ENTRE CORCHETE
print(f"{mi_lista} -> lista modificada en el indice 1")

#AGREGAR ELEMENTOS A LA LISTA
mi_lista.append(6) #SE USA .APPEND() PARA AGREGAR UN ELEMENTO AL FINAL DE LA LISTA
print(f"{mi_lista} -> se agregó el elemento 6")

mi_lista.insert(2,15) #.INSERT() AGREGA ELEMENTO  SIEMPRE Y CUANDO INDIQUE SU INDICE Y SU VALOR
print(f"{mi_lista} -> se agregó un elemento en el indice 2")

#REMOVER LOS ELEMENTOS DE LA LISTA
mi_lista.remove(5)
print(f"{mi_lista} -> se eleminó el valor 5") #REMUEVE EL VALOR DE LA LISTA

mi_lista.pop(1)
print(f"{mi_lista} -> se eleminó el elemento del indice 1") #ELEMINA INDICANDO SU INDICE

del mi_lista[2]
print(f"{mi_lista} -> se eleminó el indice 2") #ELEMINA INDICANDO EL INDICE TAMBIEN SOLO USANDO "DEL"

#SUBLISTAS
sublista = mi_lista[1:3]
print(f"{sublista} -> se generó una sublista [1:3]") #GENERA UNA SUBLISTA SEGUN SU INDICE, EL ULTIMO NO INCLUYE

#ITERAR UNA LISTA
print("\n*** iterar lista ***")
nombres = ["nacho", "mati", "santi", "nahuelito\n"]
for i in nombres: #TAMBIEN SE PUEDE PONER for nombre in nombres
    print(f"{i}") #(ES DECIR, "nombres" LE ESTA AGREGANDO ELEMENTOS A "nombre(OTRA LISTA NUEVA)")

tipo_lista = [1,3.0,True,"UnPaz"]
for i in tipo_lista: #EL CICLO FOR PUEDE ITERAR CUALQUIER VALOR DEL ELEMENTO
    print(f"{i}") #PUEDE SER ELEMENTOS DE TIPO NUMERO ENTERO O FLOTANTE, UN VALOR BOOLEANO O UNA CADENA

#TUPLAS
#LAS TUPLA SON SIMILARES A LA LISTA PERO QUE SU ESTRUCTURA DE DATOS
#NO PUEDE MODIFICAR, AGREGAR, ELEMINAR Y NI AGRANDAR SU TAMAÑO A LOS ELEMENTOS DE SU LISTA
#QUEDAN FIJO Y NO CAMBIA CON EL TIEMPO
#SON REPRESENTACON PARENTESIS () Y SEPERADOS POR UNA COMA ,

#MANEJO DE TUPLAS
mi_tupla = (1,2,3,4,5)
cadena_tupla = "manzana","pera","mandarina"
tipos_tupla = 1,"sopa",3.0,(4,5)
#LAS TUPLAS PUEDEN SER NUMEROS ENTEROS O FLOAT, CADENAS, TUPLAS DENTRO DE OTRA(subtuplas)
#SE INDENTIFICA CON PARENTESIS Y COMAS

#NO SE PUEDE MODIFICAR UNA TUPLA EJ.
#mi_tupla[0] = 10 #NO SE PUEDE MODIFICAR EN SU INDICE
#mi_tupla.append(6) #NO SE PUEDE AGREGAR UN ELEMENTO

print(f"\n{mi_tupla}")

for i in mi_tupla:
    print(i, end = " ")

#SE CREA TUPLAS EN CORDENADAS
cordenadas = (3,5)
print(f"\nLa cordenada en eje x:{cordenadas[0]}")
print(f"La cordenada en eje y:{cordenadas[1]}")

#TUPLA DE UN ELEMENTO
un_elemento = 10, #LA COMA NO ES OPCIONAL, SI O SI DEBE IR PARA QUE EL ELEMENTO SE IDENTIFIQUE COMO TUPLA
print(f"La Tupla de un elemento es: {un_elemento}")

#TUPLA ANIDADA
anidada = (1,(2,3),(4,5)) #SON SUBTUPLAS
print(f"La Tupla anidada del indice 1 es: {anidada[1]}") #TE MUESTA LA SUBTUPLA SEGUN SU INDICE INDICADO
print(f"La Tupla anidada del indice 2 es: {anidada[2]}")




