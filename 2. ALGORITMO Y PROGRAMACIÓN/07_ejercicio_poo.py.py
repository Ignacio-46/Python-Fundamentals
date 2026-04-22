#EJERCICIO: Aplicación de Mundo PC

class DispositivoEntrada:

    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.id = Raton.contador_ratones

    def __str__(self):
        return f'''Mouse: 
        ID: {self.id}
        Marca: {self.marca}
        Tipo de entrada: {self.tipo_entrada}'''

class Teclado(DispositivoEntrada):

    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado

    def __str__(self):
        return f'''Teclado: 
        ID: {self.id}
        Marca: {self.marca}
        Tipo de entrada: {self.tipo_entrada}'''

class Monitor:

    contador_monitor = 0

    def __init__(self, marca, tamanio, tipo_entrada):
        self.marca = marca
        self.tamanio = tamanio
        self.tipo_entrada = tipo_entrada
        Monitor.contador_monitor += 1
        self.id = Monitor.contador_monitor

    def __str__(self):
        return f'''Monitor: 
        ID: {self.id}
        Marca: {self.marca}
        Tamaño: {self.tamanio}
        Tipo de entrada: {self.tipo_entrada}'''

class Computadora:

    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        Computadora.contador_computadora += 1
        self.id = Computadora.contador_computadora

    def __str__(self):
        return f'''Computadora: 
        {self.nombre}
{self.monitor}\n{self.teclado}\n{self.raton}'''

class Orden:

    contador_ordenes = 0

    def __init__(self):
        self.computadoras = []
        Orden.contador_ordenes += 1
        self.id = Orden.contador_ordenes

    def agregar_computadoras(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computer in self.computadoras:
            computadoras_str += computer.__str__()

        return f'''Orden: 
        N°: {self.id}\n{computadoras_str}'''

print("---*** Aplicacion de Mundo PC ***---")
print("\n---*** Clase Mouse ***---")
raton1 = Raton("Logitech", "USB")
print(raton1)
print("\n---*** Clase Teclado ***---")
teclado1 = Teclado("Sentey", "USB")
print(teclado1)
print("\n---*** Clase Monitor ***---")
monitor1 = Monitor("Thinkvision", "17'", tipo_entrada = "HDMI")
print(monitor1)
print("\n---*** Clase Computadora ***---")
computadora1 = Computadora("PC 1", monitor= monitor1, teclado= teclado1, raton = raton1)
print(computadora1)
print("\n---*** Clase Orden ***---")
orden1 = Orden()
orden1.agregar_computadoras(computadora1)
print(orden1)

