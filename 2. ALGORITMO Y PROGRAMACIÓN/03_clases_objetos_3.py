#Atributos de clase y Atributos de instancia
print("---*** Atributos de clase e instancia de objetos ***---")

class Persona:

    atributo_clase = 0  #Los atributos de clase se define fuera de los metodos y se
    #asocia con la clase y comparte su información.

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
        #Los atributos de instancia se encuentra dentro de los metodos y no comparte su información,
        #ya que se asocia con su objeto ensi mismo cuando se crea el objeto.

if __name__ == '__main__':
    print(f'''El atributo de clase: {Persona.atributo_clase}''')
    #Se modificó el atributo clase
    Persona.atributo_clase = 10
    print(f'''El atributo de clase: {Persona.atributo_clase}''')

    persona1 = Persona(15)
    print(f'''Primer objeto:
    Atributo clase Persona 1: {persona1.atributo_clase} 
    Atributo instancia Persona 1: {persona1.atributo_instancia}''')

    persona2 = Persona(30)
    print(f'''Segundo objeto:
    Atributo clase Persona 2: {persona2.atributo_clase}
    Atributo instancia Persona 2: {persona2.atributo_instancia}''')
    #Para el atributo de instancia se tiene que crear el objeto asi se puede mostrar su valor
    #En cambio, el atributo de clase no es necesario, ya que comparte su información

print(f"\n---*** Utilizar contador ***---")
#Como utilizar un contador
class Persona:

    contador_personas = 0 #Atributo de clase

    def __init__(self, nombre, apellido): #Constructor
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador_personas += 1
        self.id = Persona.contador_personas

    def mostrar_personas(self):
        print(f'''Tercer objeto:
    La persona {Persona.contador_personas}: {self.nombre} {self.apellido}''')

    @staticmethod
    def get_contador_personas_statico(): #Es metodo no necesita referencia pero, si llamar a la clase
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls): #Este metodo si utiliza la referencia "cls" funciona como self
        return cls.contador_personas      #pero no necesita llamar a la clase para usar el contador

if __name__ == '__main__':
    persona1 = Persona("Nacho", "Roldán")
    print(f'''Primer objeto:
    La persona {persona1.id}: {persona1.nombre} {persona1.apellido}''')
    persona2 = Persona("Matias", "Torres")
    print(f'''Segundo objeto:
    La persona {persona2.id}: {persona2.nombre} {persona2.apellido}''')
    persona3 = Persona("Santos", "Mira")
    persona3.mostrar_personas()
    #Se imprime el contador de personas
    print(F"El contador de personas: {Persona.contador_personas}")
    #Se imprime el contador estático
    print(f"El contador de personas (estatico): {Persona.get_contador_personas_statico()}")
    #Se imprime el contador de clase
    print(f"El contador de personas (clase): {Persona.get_contador_personas_clase()}")





