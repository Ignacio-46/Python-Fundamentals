#EJERCICIO: Sistema de Bibliotecas

class Libros:

     def __init__(self, titulo, autor, genero):
         self._titulo = titulo
         self._autor = autor
         self._genero = genero

     @property
     def titulo(self):
         return self._titulo

     @property
     def autor(self):
         return self._autor

     @property
     def genero(self):
         return self._genero

class Biblioteca:

     def __init__(self, nombre):
            self._nombre = nombre
            self._libros = []

     def agregar_libros(self, libro):
         self._libros.append(libro)

     def buscar_libro_autor(self, autor):
         for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libros(libro)

     def buscar_libro_genero(self, genero):
            for libro in self._libros:
                if libro.genero.lower() == genero.lower():
                    self.mostrar_libros(libro)

     def mostrar_libros(self, libro):
         print(f'''Libro --> Titulo: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}''')

     def mostrar_todos_libros(self):
         print(f"El sistema de bibliotecas: {self._nombre}")
         for libro in self._libros:
             self.mostrar_libros(libro)

     @property
     def nombre(self):
         return self._nombre
     @property
     def libros(self):
         return self._libros

if __name__ == "__main__":
    biblioteca1 = Biblioteca('Unpaz')
    print(f"---*** Bienvenidos a la Biblioteca: {biblioteca1.nombre} ***---")

    #Definicion de libros
    libro1 = Libros("Cien años de soledad", "Gabriel G. Marquez", "Ficción")
    libro2 = Libros("La Rayuela", "Julio Cortázar", "Novela")
    libro3 = Libros("El principito", "Saint Exupery", "Fantasia")

    #Agrega los libros en la biblioteca
    biblioteca1.agregar_libros(libro1)
    biblioteca1.agregar_libros(libro2)
    biblioteca1.agregar_libros(libro3)

    #Buscar libros por autor
    autor = "Gabriel G. Marquez"
    print(f"\nLibros del autor: {autor}")
    biblioteca1.buscar_libro_autor(autor)

    #Buscar libros por género
    genero = "Novela"
    print(f"\nLibros por género: {genero}")
    biblioteca1.buscar_libro_genero(genero)

    #Mostrar todos los libros registrados
    print("\n")
    biblioteca1.mostrar_todos_libros()



