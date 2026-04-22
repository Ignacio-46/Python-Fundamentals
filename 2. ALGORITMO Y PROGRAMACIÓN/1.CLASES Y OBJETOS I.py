#Definicion de una clase
class Persona:

    def inicializar_persona(self, nombre, apellido):#Metodo se considera igual a una función
         #Se crea los Atributos de la clase
         self.nombre = nombre
         self.apellido = apellido

    def mostrar_persona(self):#Metodo
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f"Dir. memoria self: {id(self)}")
        print(f"Dir. memoria hex self: {hex(id(self))}")
        print(f"Dir. memoria: {id(persona1)}")
        print(f"Dir. memoria hex: {hex(id(persona1))}")

#Creacion de objetos
if __name__ == '__main__':
    #Creacion de un primer objeto
    persona1 = Persona() # Se crea un objeto vacio en memoria
    persona1.inicializar_persona(nombre = "Nacho", apellido = "Roldán")
    persona1.mostrar_persona()
    print(f"Dir. memoria: {id(persona1)}")
    print(f"Dir. memoria hex: {hex(id(persona1))}")

#Sintaxis de un constructor
# class IniciarClase:
#     def __init__(self, parametro1, parametro2):
#         self.parametro1 = parametro1
#         self.parametro2 = parametro2

class IniciarPersona:

    #Constructor
    def __init__(self, nombre, apellido): #Se declara los atributos
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self): #Se realiza los Metodos
        print(f'''\nPersona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f"Dir. memoria: {id(persona2)}")
        print(f"Dir. memoria hex: {hex(id(persona2))}")

#Creacion de un objeto
if __name__ == '__main__':
    persona2 = IniciarPersona("Eze","Roldán")
    persona2.mostrar_persona()
    print(f"Dir. memoria: {id(persona2)}")
    print(f"Dir. memoria hex: {hex(id(persona2))}")

#Direccion de memoria
# print(f"Dir. memoria: {id()}")
# print(f"Dir. memoria hex: {hex(id())}")

#Ejercicio Aritmético
class Aritmetico:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        self.suma = num1 + num2
        self.resta = num1 - num2
        self.multiplicacion = num1 * num2
        self.division = num1 / num2

    def mostrar_operacion(self):
        print(f'''\nOperacion Aritmético:
        la suma es: {self.suma}
        la resta es: {self.resta}
        la multiplicacion es: {self.multiplicacion}
        la division es: {self.division}''')

if __name__ == '__main__':
    operar = Aritmetico(1, 2)
    operar.mostrar_operacion()

class Aritmetica:                              #Se define la clase

    def __init__(self, num1, num2):            #Se define el constructor
        self.num1 = num1                       #Se realiza los atributos
        self.num2 = num2

    def suma(self):                            #Se realiza los metodos = funciones
        return self.num1 + self.num2

    def resta(self):                           #Metodo
        return self.num1 - self.num2

    def multiplicacion(self):                  #Metodo
        return self.num1 * self.num2

    def division(self):                        #Metodo
        if self.num2 != 0:
            return self.num1 / self.num2
        return "Error: division por zero"

    def mostrar_operaciones(self):             #Metodo
        print(f'''Operaciones Aritmetica:
        La suma es: {self.suma()}
        La resta es: {self.resta()}
        La multiplicacion es: {self.multiplicacion()}
        La division es: {self.division()}''')

if __name__ == "__main__":                     #Se crea el objeto
    print("\nPrimer objeto: ")
    operar = Aritmetica(2,4)        #Se guarda la clase dentro del objeto o variable
    operar.mostrar_operaciones()               #Se muestra el objeto llamando un metodo
    print("\nSegundo objeto: ")
    operar1 = Aritmetica(3, 9)
    operar1.mostrar_operaciones()



