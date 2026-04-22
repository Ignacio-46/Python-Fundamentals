#Ejercicio Máquina de Snacks
import os.path

class Snack:

    contador_snack = 0

    def __init__(self, nombre = "", precio = 0.0):
        self.nombre = nombre
        self.precio = precio
        Snack.contador_snack += 1
        self.id = Snack.contador_snack

    def __str__(self):
       return f'''Id: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}'''

    def escribir_snack(self):
        return f'''{self.id},{self.nombre},{self.precio}\n'''

class ServicioSnacks:

    snack_archivo = "Snacks.txt"

    def __init__(self):
        self.snacks = []
        #Revisar si ya existe el archivo snacks
        #Si ya existe, obtenemos los snacks del archivo
        if os.path.isfile(self.snack_archivo):
            self.snacks = self.obtener_snacks()
        #Si no, cargamos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack("papa", 70),
            Snack("Refresco", 50),
            Snack("Sandwich", 120)
        ]

        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivos(snacks_iniciales)

    def guardar_snacks_archivos(self, snacks):
        try:
            with open(self.snack_archivo, "a") as archivo:
                for snack in snacks:
                    archivo.write(snack.escribir_snack())
        except Exception as e:
            print(f"Error al guardar snacks en el archivo: {e}\n")

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.snack_archivo, "r") as archivo:
                for linea in archivo:
                    #1,"papa",70.0
                    #2,"Refresco",50.0
                    id_snack, nombre, precio = linea.strip().split(",")
                    snack = Snack(nombre, float(precio))
                    snack.id = int(id_snack)
                    Snack.contador_snack = max(Snack.contador_snack, snack.id)
                    snacks.append(snack)
        except Exception as e:
            print(f"Error al leer archivos de snacks: {e}")
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivos([snack])

    def mostrar_snacks(self):
        print("---*** Snacks en el Inventario ***---")
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks

class MaquinaSnacks:

    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snack(self):
        salir = False
        print("---*** Maquina de Snacks ***---\n")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrió un error: {e}")

    def mostrar_menu(self):
        print(f'''\nMenú:
        1. Comprar Snacks
        2. Mostrar Tickets
        3. Agregar un nuevo Snacks al inventario
        4. Inventario Snacks
        5. Salir''')
        try:
            return int(input("\nElige un opción: "))
        except ValueError:
            print("Ingrese un número valido.")
            return 0

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print("Salir")
            return True
        else:
            print(f"Opcion invalida: {opcion}")
        return False

    def comprar_snack(self):
        try:
            id_snack = int(input("Que snack quieres comprar (id)?: "))
        except ValueError:
            print("Ingrese un 'ID' valido.")
            return
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f"Snack encontrado -> {snack}")
        else:
            print(f"Snack '{id}' no encontrado")

    def mostrar_ticket(self):
        if not self.productos:
            print(f"No hay snack en el ticket")
            return
        total = sum(snack.precio for snack in self.productos)
        print("---*** Tickets de venta ***---")
        for producto in self.productos:
            print(f"\t - {producto.nombre} - ${producto.precio:.2f}")
        print(f"\t - Total -> ${total:.2f}")

    def agregar_snack(self):
        nombre = input("Nombre del Snack: ")
        try:
            precio = float(input("Precio del Snack: "))
        except ValueError:
            print("Precio invalido.")
            return
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f"Snack agregado correctamente -> '{nuevo_snack}'.")

#Programa Principal
if __name__ == "__main__":
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snack()
