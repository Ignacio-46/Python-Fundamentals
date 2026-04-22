import os

class Pelicula:

    contador_pelicula = 0

    def __init__(self, nombre, id_pelicula = None):
        self.nombre = nombre

        if id_pelicula is None:
            self.id_pelicula = Pelicula.contador_pelicula
            Pelicula.contador_pelicula += 1
        else:
            self.id_pelicula = int(id_pelicula)
            Pelicula.contador_pelicula = max(Pelicula.contador_pelicula, self.id_pelicula + 1)

class ServiciosPeliculas:

    def __init__(self):
        self.peliculas_archivo = "Películas.txt"
        self.cargar_peliculas()

    def cargar_peliculas(self):
        try:
            with open(self.peliculas_archivo, "r", encoding="utf8") as archivo:
                for lineas in archivo:
                    id_pelicula, _ = lineas.strip().split(" -> ")
                    Pelicula.contador_pelicula = max(Pelicula.contador_pelicula, int(id_pelicula) + 1)
        except FileNotFoundError:
            pass

    def agregar_peliculas(self):
        nombre_pelicula = input("Ingrese el nombre del película: ")
        nuevo_pelicula = Pelicula(nombre_pelicula)
        try:
            with open(self.peliculas_archivo, "a", encoding="utf8") as archivo:
                    archivo.write(f"{nuevo_pelicula.id_pelicula} -> {nuevo_pelicula.nombre}\n")
            print(f'''---*** Sé cargó correctamente la pelicula al catalogo ***---\n''')
        except Exception as e:
            print(f"Error al guardar el archivo -> {e}")

    def listar_peliculas(self):
        try:
            with open(self.peliculas_archivo, "r", encoding="utf8") as archivo:
                print(f'''---*** Peliculas ***---\n''')
                for lineas in archivo:
                    id_pelicula, nombre = lineas.strip().split(" -> ")
                    print(f"{id_pelicula} -> {nombre}")
            print("\n")
        except FileNotFoundError:
            print(f"No hay peliculas cargadas aún\n")
        except Exception as e:
            print(f"Error al leer el archivo -> {e}\n")

    def eliminar_pelicula(self):
        try:
            os.remove(self.peliculas_archivo)   #os.remove(el nombre del archivo que deseamos eliminar)
            Pelicula.contador_pelicula = 0
            print(f"Archivo eliminado: {self.peliculas_archivo}\n")
        except FileNotFoundError:
            print(f"Archivo no existente: {self.peliculas_archivo}\n")

class CatalogoPeliculas:

    def __init__(self):
        self.pelis = ServiciosPeliculas()

    def agregar_peliculas(self):
        self.pelis.agregar_peliculas()

    def listar_peliculas(self):
        self.pelis.listar_peliculas()

    def eliminar_pelicula(self):
        self.pelis.eliminar_pelicula()

    def iniciar_menu(self):
        salir = False
        print(f'''---*** App catalogos de Peliculas ***---\n''')
        while not salir:
            opcion = self.mostrar_menu()
            salir = self.ejecutar_opciones(opcion)

    def mostrar_menu(self):
        while True:
            print('''Menú:
            1. Agregar Películas
            2. Listar Películas
            3. Eliminar Películas
            4. Salir''')
            try:
                return int(input("\nElija una opción: "))
            except ValueError:
                print(f"Ingrese la opción del (1-4)\n")

    def ejecutar_opciones(self,opcion):
        if opcion == 1:
            self.agregar_peliculas()
        elif opcion == 2:
            self.listar_peliculas()
        elif opcion == 3:
            self.eliminar_pelicula()
        elif opcion == 4:
            print("---*** Saliendo del Programa ***---")
            return True
        else:
            print(f"Opción invalida: {opcion}\n")
        return False

#Programa Principal
if __name__ == "__main__":
    peliculas = CatalogoPeliculas()
    peliculas.iniciar_menu()

