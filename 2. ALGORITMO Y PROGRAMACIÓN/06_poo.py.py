#Herencia en Python

class Animal:   #Esto se lo considera clase padre
    def comer(self):
        print("como muchas veces al dia") #Metodo o Función

    def dormir(self):
        print("duermo muchas horas al dia") #Los metodos de clase padre pueden ir a las subclases o clase hijas

class Perro(Animal): #Esto se lo considera clase hija (Heredado de la clase padre)
    def hacer_sonido(self):
        print("Puedo ladrar") #Los metodos de clase hija no pueden ir a la clase padre

class Gato(Animal):
    #Sobreescritura del metodo dormir
    def dormir(self):
        print("Suelo dormir 15 horas al dia")

#Programa Principal
print("---*** Ejemplo de Herencia en Python ***---")
print("\n'Clase padre, soy un Animal'")
animal1 = Animal() # Se crea objeto
animal1.comer() #Aparece los metodos de clase padre
animal1.dormir()

print("\n'Clase hija, soy un perro'")
perro1 = Perro() # Se crea objeto
perro1.comer()  #Heredado de clase padre
perro1.dormir() #Heredado de clase padre
perro1.hacer_sonido() #Aparece metodo de la clase hija

#Sobreescritura de un metodo
print("\n---*** Sobreescritura clase Gato ***---")
print("\n'Clase hija, soy un gato'")
gato1 = Gato() # Se crea objeto
gato1.comer()
gato1.dormir() #Se puede sobreescribir el metodo en la clase hija

#Polimorfismo en Python
#Es el multiple comportamiento de metodos según tipo de datos con lo cual estamos trabajando

class Animales:

    def hacer_sonido(self):
        print("Hace sonidos")

class ElPerro(Animales):
    def hacer_sonido(self):
        print("Guau guau!!")

class ElGato(Animales):
    def hacer_sonido(self):
        print("Miaaaaaaauu!!")

print("\n---*** Ejemplo de Polimorfismo en Python ***---")
print("\n'Clase padre Animal'")
animal1 = Animales()
animal1.hacer_sonido()

print("\nClase hija Perro:")
perro1 = ElPerro()
perro1.hacer_sonido()

print("\nClase hija Gato:")
gato1 = ElGato()
gato1.hacer_sonido() #Polimorfismo utiliza la sobreescritura de los metodos de todas las clases, se lo considera también como interfaces

#Duck typing
#Si una clase se parece de tal manera y se comporta de tal manera, entonces esa es la manera
#Ejemplo: Si se parece un pato y se comporta como un pato, entonces es un pato. Esto se lo define asi como Duck typing

#Funcion polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

print("\n---*** Ejemplo de Duck typing en Python ***---")
print("\nClase Padre Animal:")
animal1 = Animales()
hacer_sonido_animal(animal1)

print("\nClase hija Perro:")
perro1 = ElPerro()
hacer_sonido_animal(perro1)

print("\nClase hija Gato:")
gato1 = ElGato()
hacer_sonido_animal(gato1)

print("\n---*** Clase Object ***---")

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #Sobreescribir el metodo __str__
    def __str__(self):
        return f'''\nPersona:
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Dir. mem.: {super.__str__(self)}'''

persona1 = Persona("Ignacio", "Roldán")
print(persona1) #El metodo __str__ se llama automáticamente desde print
#print(persona1.__str__()) Esto es lo mismo pero es opcional

