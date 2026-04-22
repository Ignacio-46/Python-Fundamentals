#Encapsulamiento Aritmetica
print("---*** Encapsulamiento Aritmetica ***---\n")

class Aritmetica:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def sumar(self):
        suma = self._num1 + self._num2
        return suma

    def restar(self):
        resta = self._num1 - self._num2
        return resta

    def multiplicar(self):
        multiplicacion = self._num1 * self._num2
        return multiplicacion

    def dividir(self):
        if self._num2 != 0:
            division = self._num1 / self._num2
            return division
        return "Error no se puede dividir por cero"

    def get_num1(self):
        return self._num1
    def set_num1(self, num1):
        self._num1 = num1

    def get_num2(self):
        return self._num2
    def set_num2(self, num2):
        self._num2 = num2

    def mostrar_operaciones(self):
        print(f'''La operaciones aritmeticas:
        La suma: {self.sumar()}
        La resta: {self.restar()}
        La multiplicacion: {self.multiplicar()}
        La division: {self.dividir()}''')

if __name__ == "__main__":
    print("Primer objeto:")
    aritmetica1 = Aritmetica(3,9)
    aritmetica1.mostrar_operaciones()
    print("\nSegundo objeto:")
    aritmetica2 = Aritmetica(2,4)
    aritmetica2.set_num1(9)
    aritmetica2.set_num2(3)
    aritmetica2.mostrar_operaciones()
    #Esta forma es de mostrar por separado cuando llamas a los metodos
    aritmetica3 = Aritmetica(4,5)
    print(f'''\nTercer objeto:
        Las operaciones aritmeticas:
        Suma: {aritmetica3.sumar()}
        Resta: {aritmetica3.restar()}
        Multiplicación: {aritmetica3.multiplicar()}
        División: {aritmetica3.dividir()}''')

# Sistema de Empleados
print("\n---*** Sistema de Empleados ***---")

class Empleados:

    contador_empleados = 0

    def __init__(self, nombre, departamento ):
        self.nombre = nombre
        self.departamento = departamento
        Empleados.contador_empleados += 1
        self.id = Empleados.contador_empleados

    @classmethod
    def total_empleados(cls):
        return cls.contador_empleados

class Empresa:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleados(nombre, departamento)
        self.empleados.append(empleado)

    def numero_empleados_departamento(self, departamento):
        contador_empleados_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_departamento += 1

        return contador_empleados_departamento

    def total_empleados_empresa(self):
        print(f"Total de empleados de la empresa: {self.nombre}")
        for empleado in self.empleados:
            print(f'''ID: {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}''')

if __name__ == "__main__":

    #Se crea una empresa
    empresa1 = Empresa("La Finca S.A.")

    #Se contrata empleados
    empresa1.contratar_empleado("Nacho", "IT")
    empresa1.contratar_empleado("Mati", "IT")
    empresa1.contratar_empleado("Nahuelito", "Ingeniería")
    empresa1.contratar_empleado("Santi", "Ventas")
    #Se obtiene el total de empleados
    print(f"Total de empleados: {Empleados.total_empleados()}")

    #Se obtiene el total de empleados por departamento
    print(f"Empleados de IT: {empresa1.numero_empleados_departamento('IT')}")

    #Se imprime todos los empleados de la empresa
    empresa1.total_empleados_empresa()












