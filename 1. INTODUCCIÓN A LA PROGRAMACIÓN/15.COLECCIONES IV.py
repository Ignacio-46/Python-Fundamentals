#FORMA DE COMO TRABAJAR CON SET(CONJUNTO)
#LISTA DE SUSCRIPTORES
print("*** Lista de Suscriptores ***")
suscriptores = set() #DE ESTA FORMA SE ACLARA EL

cantidad = int(input("Cuantos suscriptores desea agregar?: "))
for _ in range(cantidad):
    suscripto = input("Ingrese el suscríptor: ")
    suscriptores.add(suscripto)

print("Lista de suscriptores:")
for i in suscriptores:
    print(f"Se suscribió: {i}")

nuevo = input("Desea agregar un nuevo suscriptor?: ")
suscriptores.add(nuevo)
print(f"Nuevo suscriptor ingresado: {nuevo}")

print("Nueva Lista de suscriptores:")
for i in suscriptores:
    print(f"Suscriptos: {i}")

eleminar = input("Desea eleminar un suscriptor?: ")
suscriptores.remove(eleminar)
print(f"Suscriptor eleminado: {eleminar}")

print("Nueva Lista de suscriptores:")
for i in suscriptores:
    print(f"Suscriptos: {i}")



#FORMAS DE COMO TRABAJAR EN DICCIONARIOS
print(f"\n*** Agenda de Contactos ***")

agenda = {
    "carlos" : {
        "telefono": "55667711",
        "email": "carlos@mail.com",
        "direccion": "Calle principal 123"
    },
    "maria" : {
        "telefono": "99887733",
        "email": "maria@mail.com",
        "direccion": "Av central 456"
    },
    "pedro" : {
        "telefono": "55139078",
        "email": "pedro@mail.com",
        "direccion": "Plaza mayor 789"
    }
}
print(f"Agenda: {agenda}")

#ACCEDER LA INFORMACIÓN DEL CONTACTO
print(f'''\nInformacion de Maria:\nTelefono: {agenda["maria"]["telefono"]}
email: {agenda["maria"]["email"]} 
direccion: {agenda.get("maria").get("direccion")}\n''') #USAR [][] O GET().GET() AMBAS SINTAXIS SON VALIDAS

#AGREGAR UN CONTACTO NUEVO
agenda["Ana"] = {
    "telefono":"55678392",
    "email":"ana@mail.com",
    "direccion":"Av Salvador Diaz 321"
}
print(f"Agenda: {agenda}")

#ELEMINAR UNA LLAVE
agenda.pop("pedro")
#del agenda["pedro"] TAMBIEN SE PUEDE ELEMINAR DE ESTA FORMA
print(f"Agenda: {agenda}\n")

#MOSTRAR LOS CONTACTOS DE LA AGENDA
for nombres, contacto in agenda.items(): #FUNCIONA CUANDO HAY UN DICCIONARIO DENTRO DE OTRO {{ }}
    print(f'''Nombres: {nombres}
telefono : {contacto["telefono"]}
email: {contacto["email"]}
direccion: {contacto["direccion"]}
''')

