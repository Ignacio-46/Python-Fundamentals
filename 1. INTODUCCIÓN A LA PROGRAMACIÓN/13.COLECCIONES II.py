#LOS SETS (CONJUNTOS)
#SON COLECCIONES DE DATOS NO ORDENADOS EN LOS ELEMENTOS
#Y NO TIENE EN CUENTA LOS ELEMENTO DUPLICADOS
#SON REPRESENTADOS CON LLAVES {}

#MENEJOS DE SETS
set = {"elemento1", "elemento2", "elemento3"}
seta = {1,2,3,4,5}
setab = {2,3.0,True,"NACHO"}
numeros = {1,2,2,3,3,4,5} #NO TIENE EN CUENTA LOS ELEMENTOS DUPLICADOS
print(numeros) #ACA UN EJEMPLO

#CREAR UN CONJUNTO
set = {1,2,3,4,5}
print(f"{set} - conjunto original")

#AGREGAR ELEMENTOS CON ADD()
set.add(6)
set.add(7)
set.add(3) # NO TIENE EN CUENTA LOS ELEMENTOS DUPLICADOS CUANDO SE AGREGA
print(f"{set}")

#REMOVER UN ELEMENTO
set.remove(4)
print(f"{set}")

#LONGITUD DE LOS ELEMENTOS
len(set)
print(f"La longitud de set es: {len(set)}")

#COMPRAR LOS SETS SI EXISTEN O NO
print(f"Existe dentro de set el elemento 4?: {4 in set} ")
print(f"Existe dentro de set el elemento 1?: {1 in set} ")

#ITERAR LOS ELEMENTOS
for elemento in set:
    print(elemento, end = " ")

print("\n")

#OPERACION DE CONJUNTOS
a = {1,2,3,4}
b = {3,4,5,6}
print(f"a: {a}")
print(f"b: {b}")

#UNION DE CONJUNTOS
union = a | b
print(f"La union entre a | b : {union}") #NO TIENE ENCUENTA LOS ELEMNTO DUPLICADOS CUANDO SE HACEN LA UNION

#INTERSECCION DE CONJUNTOS
interseccion = a & b
print(f"La interseccion entre a & b : {interseccion}")

#DIFERENCIA DE CONJUNTOS
diferencia = a - b
diferencia1 = b - a
print(f"La diferencia entre a - b : {diferencia}")
print(f"La diferencia entre b - a : {diferencia1}")

#DICCIONARIOS
#SON COLECCIONES DE DATOS DE FORMA ORDENADA QUE SE GUARDAN EN LLAVE : VALOR
#TIENE UN CONJUNTOS DE VALORES CON UN CONJUNTO DE CLAVES QUE SIRVEN COMO INDICE UNICOS

#MANEJO DE DICCIONARIOS
diccionario = {"clave1":"valor 1","clave2":"valor 2","clave3": "valor 3"}

print(f"El diccionario tiene:{diccionario}") #MUESTRA EL DICCIONARIO CON LAS CLAVES Y SUS VALORES
print(f"Clave 1:{diccionario["clave1"]}") #ASI SE LO LLAMA Y SE MUESTRA LAS CLAVES CON SU VALORES DE FORMA INDEPENDIENTE
print(f"Clave 2:{diccionario.get("clave2")}") #EL METODO GET() RECUPERA CLAVE CON SU VALOR DENTRO DEL DICCIONARIO
print(f"Clave 3:{diccionario.get("clave3")}\n")

#FORMAS Y METODOS DEL DICCIONARIO
persona = {"nombre":"Ignacio","edad":"33 años","ciudad":"Bs. As."}
print(f"Persona: {persona}")

#LLAMAR LAS CLAVES CON SUS VALORES
print(f'''Nombre: {persona["nombre"]}
edad: {persona["edad"]}
ciudad: {persona.get("ciudad")}\n''')

#MODIFICAR EL VALOR DEL CLAVE
persona["edad"] = 34
persona["nombre"] = "Ramón"
print(f"Nombre: {persona["nombre"]} Edad: {persona["edad"]}")

#AGREGAR CLAVES CON SUS VALORES
persona["profesion"] = "Fumigador"
persona["estudio"] = "Analista de Sistema"
print(f"Persona: {persona}")

#ELEMINAR CLAVES CON SUS VALORES
del persona["edad"] #USANDO DEL
persona.pop("ciudad") #USANDO .POP()
print(f"Persona: {persona}\n")

#ITERAR LOS DICCIONARIOS

#ITERAR LOS ELEMENTOS (RECUPERA CLAVE Y SU VALOR)
for clave, valor in persona.items(): #LO DEVUELVE COMO TUPLA Y HACE QUE LOS ELEMENTOS SE VUELVA INDEPENDIENTE
    print(f"{clave}: {valor}") #USANDO DE FORMA UNPACKING(TUPLAS)

print("\n")

#RECUPERAR CLAVE SOLAMENTE
for clave in persona.keys():
    print(f"-{clave}")

print("\n")

#RECUPERA VALOR SOLAMENTE
for valor in persona.values():
    print(f"-{valor}")

