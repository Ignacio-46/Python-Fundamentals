from collections import deque

print("---*** Archivo con Pila y Cola ***---\n")
cola = deque()
pila = []
mi_archivo = "clientes.txt"

# Paso 0: crear archivo (solo para probar)
with open(mi_archivo, "w", encoding="utf8") as archivo:
    archivo.write("Ana\nLuis\nPedro\nSofia\nCarlos\n")

# Paso 1: leer archivo
with open(mi_archivo, "r", encoding="utf8") as archivo:
    for linea in archivo:
        nombre = linea.strip()
        cola.append(nombre)

# Paso 2: cargar cola
print(f"Cola cargadas: {list(cola)}")

# Paso 3: pasar de cola a pila
while cola:
     pila.append(cola.popleft())
print(f"Pila: {pila}")

# Paso 4: sacar de pila e imprimir
print("Invertido:")
while pila:
     print(pila.pop())

print("\n---*** Pilas y Cola con Clase, Objeto y Archivo ***---\n")

from collections import deque
# Clase
class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        return self.nombre

class SistemaClientes:

    def __init__(self, entrada, salida):
        self.archivo_entrada = entrada
        self.archivo_salida = salida
        self.cola = deque()
        self.pila = []

    def leer_clientes(self): # Leer archivo
        with open(self.archivo_entrada, "r", encoding="utf8") as r:
             for linea in r:
                 cliente = Cliente(linea.strip())
                 self.cola.append(cliente)

    def mostrar_cola(self): # Recorre la lista cola
        for cliente in self.cola:
            print(cliente.mostrar())

    def pasar_a_pila(self): # Pasar de cola a pila
        while self.cola:
           self.pila.append(self.cola.popleft())

    def guardar_resultado(self): # Guardar en archivo
        with open(self.archivo_salida, "w", encoding="utf8") as w:
            while self.pila:
                cliente = self.pila.pop()
                w.write(f"{cliente.mostrar()}\n")  # Escribe en archivo

# MAIN
if __name__ == "__main__":
   entrada = "clientes.txt"
   salida = "resultado.txt"

   sistema = SistemaClientes(entrada, salida)

   sistema.leer_clientes()
   sistema.mostrar_cola()
   sistema.pasar_a_pila()
   sistema.guardar_resultado()
