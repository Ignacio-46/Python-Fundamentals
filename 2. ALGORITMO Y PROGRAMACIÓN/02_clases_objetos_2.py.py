#Encapsulamiento en Phyton
#Atributos Público, Protegido y Privado.

class Coche: #Clase

    def __init__(self, marca, modelo, color): #Constructor
        self.marca = marca #Atributo Público se pone con "."
        self._modelo = modelo #Atributo Protegido se pone con "._"
        self.__color = color #Atributo Privado se pone con ".__"

    def conducir(self): #Metodo
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')

if __name__ == '__main__': #Se crea el objeto
    coche1 = Coche("Ford", "'82", "Dorado")
    coche1.conducir()

    #Forma de entender los atributos
    #No se debería acceder los atributos que no sean públicos
    coche1.marca = "Volkswagen" #El atributo público se puede modificar sin nigún problema
    coche1._modelo = "'00" #El atributo protegido se puede modificar, pero no es una buena práctica
    coche1.__color = "Blanco" #El atributo privado no se modifica, ya que python lo ignora por completo
    coche1._Coche__color = "Blanco" #Esta es la forma para acceder el atributo privado, pero no es una buena práctica
    coche1.conducir()
print("\n")

#Metodo Get y Set
#Todos los atributos pasa a ser protegido y se marca con "._"
#El Metodo get nos permite leer información el valor de atributo
#El metodo set nos permite modifica el valor de un atributo

class Auto:
    def __init__(self, marca, modelo, color):
        self._marca = marca #Atributo protegido
        self._modelo = modelo #Atributo protegido
        self._color = color #Atributo protegido

#La mejor forma que quede el atributo es el protegido para usar el metodo get y set,
#pero depende del programador con el proyecto que esté trabajando, pues algunos utilizan el atributo privado.

    def get_marca(self, marca):     #Forma de usar get
        return  self._marca
    @property                       #Define el metodo get de manera más pythonica, funciona igual que el de arriba
    def marca(self):
        return self._marca

    def set_marca(self, marca):     #Forma de usar set
        self._marca = marca
    @marca.setter                   #Define el metodo set de manera más pythonica, funciona igual que el de arriba
    def marca(self, marca):
        self._marca = marca

    def get_modelo(self, modelo):
        return self._modelo
    @property
    def modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    def get_color(self, color):
        return self._color
    @property
    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color
    @color.setter
    def color(self, color):
        self._color = color

    def conduciendo(self):
        print(f'''Conduciendo el auto:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

if __name__ == '__main__':
    auto1 = Auto("Fiat", "'00", "Verde")
    auto1.conduciendo()
    auto1.set_marca("Fiat 600")
    auto1.set_modelo("'69")
    auto1.set_color("Amarillo")
    auto1.conduciendo()
    #Forma de mostrar get y set de manera pythonica con @property y @setter
    #Se declara como atributos públicos, pero en realidad están realizados como protegidos
    auto1.marca = "Peugeot"
    auto1.modelo = "2005"
    auto1.color = " Negro"
    auto1.conduciendo()
    #de manera dinámica con "setatrr" y "__dict__"
    setattr(auto1, "nuevo_atributo", "valor nuevo atributo")
    auto1.nuevo_atributo2 = "valor nuevo atributo 2"
    print("\n",auto1.nuevo_atributo)
    print(f"Nuevo atributo del auto 1: {auto1.nuevo_atributo2}")
    print(f"Atributos del auto 1: {auto1.__dict__}")
    #Segundo objeto
    auto2 = Auto("Alfaromero", "'89", "Rojo")
    auto2.conduciendo()
    print(f"Atributos del auto 2: {auto2.__dict__}")





