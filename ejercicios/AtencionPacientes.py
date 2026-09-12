# Ejercicio: Sistema de Atención de Pacientes
# Desarrollar un programa que gestione un sistema de atención de pacientes utilizando:
# Clases y objetos, Métodos, Archivos, Cola (FIFO), Pila (LIFO)
# Descripción del sistema:
# El sistema debe simular una clínica donde los pacientes llegan y se agregan a una cola de espera,
# los pacientes atendidos pasan a una pila de historial y toda la información se guarda y se lee desde archivos
# El programa debe mostrar un menú con las siguientes opciones:
# 1. Registrar paciente. Ingresar:
#    Nombre completo
#    Especialidad:'C' → Cardiología, 'T' → Traumatología, 'P' → Pediatría,
#    Tiempo estimado (entero > 0)
#    El paciente se agrega a la cola
#    también se guarda en un archivo
# 2. Mostrar cola de espera: Mostrar todos los pacientes en orden de llegada
# 3. Atender paciente: Sacar el primer paciente de la cola Y pasarlo a la pila de atendidos, mostrar quién fue atendido
# 4. Mostrar historial (pila): Mostrar los pacientes atendidos (último atendido primero)
# 5. Buscar pacientes por especialidad: Mostrar todos los pacientes (en cola o historial) de una especialidad
# 6. Calcular tiempo total de atención: Sumar el tiempo de todos los pacientes en la cola
# 7. Paciente con mayor tiempo de atención (Sin usar max())
# 8. Guardar historial en archivo: Guardar los pacientes atendidos en un archivo
# 9. Cargar pacientes desde archivo: Leer pacientes desde archivo y cargarlos en la cola
# 10. Salir del programa
# Objetivo Construir un sistema que: reciba datos, los procese, los guarde, los recupere y use estructuras correctas
from collections import deque

class Pacientes:

    contador_pacientes = 0

    def __init__(self, nombre, especialidad, tiempo_espera):
        self.nombre = nombre
        self.especialidad = especialidad
        self.tiempo_espera = tiempo_espera
        Pacientes.contador_pacientes += 1
        self.id_pacientes = Pacientes.contador_pacientes

    def __str__(self):
        return f'''{self.id_pacientes}. Paciente: {self.nombre} - Especialidad: {self.especialidad} - Tiempo: {self.tiempo_espera} minutos.'''

class SistemaPacientes:

    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida
        self.cola = deque()
        self.pila = []

    def validacion_numero(self,mensaje,tipo):
        while True:
            try:
                if tipo == 1:
                    numero_int = int(input(mensaje))
                    if numero_int <= 0:
                        print("Error. Debe Ingresar un numero entero positivo.")
                    else:
                        return numero_int
                if tipo == 2:
                    numero_float = float(input(mensaje))
                    return numero_float
            except ValueError:
                print("Error. Debe Ingresar un número entero.")
                continue

    def validacion_nombre(self,mensaje):
        letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

        while True:
            nombre = input(mensaje).title().strip()
            if nombre == "":
                print("Error. Debe Ingresar una nombre.")
                continue

            for letra in nombre:
                if letra not in letras:
                    print("Error. Solo se permite letras y espacios")
                    break

            else:
                return nombre

    def validacion_especialidad(self,mensaje):
        letras = "CTP"

        while True:
            categoria = input(mensaje).upper().strip()
            if categoria == "":
                print("Error. Debe Ingresar una especialidad.")
                continue

            for letra in categoria:
                if letra not in letras:
                    print("Error. Solo ingrese la especialidad especificada.")
                    break

            else:
                if categoria == "C":
                    return "Cardiología"
                elif categoria == "T":
                    return "Traumatología"
                else:
                    return "Pediatría"

    def registrar_pacientes(self): #1
        nombre = self.validacion_nombre("Ingrese el nombre del Paciente: ")
        especialidad = self.validacion_especialidad("Ingrese la Especialidad 'C'(Cardiología),'T'(Traumatología),'P'(Pediatría): ")
        tiempo_espera = self.validacion_numero("Tiempo de atención: ", 1)
        paciente = Pacientes(nombre, especialidad, tiempo_espera)
        self.cola.append(paciente)
        print("\n---*** Se registró el paciente ***---\n")
        try:
            with open(self.entrada, "a", encoding="utf8") as archivo:
                archivo.write(f'''{paciente.nombre} - {paciente.especialidad} - {paciente.tiempo_espera}\n''')
        except Exception as e:
            print(f"Error al guardar el archivo: {e}.")

    def mostrar_cola(self): #2
        if not self.cola:
            print("---*** No se ha registrado nigún Paciente ***---\n")
        else:
            print("---*** Lista de Pacientes Registrados ***---\n")
            for linea in self.cola:
                print(linea)

    def atender_paciente(self): #3
        if not self.cola:
            print("---*** No se ha registrado nigún Paciente ***---\n")
        else:
            print("---*** Lista de Pacientes Atendidos ***---\n")
            self.pila.append(self.cola.popleft())

            for pila in self.pila:
                print(f'''{pila.id_pacientes}. Paciente: {pila.nombre} - Especialidad: {pila.especialidad} - Tiempo: {pila.tiempo_espera} minutos.''')

    def mostrar_pacientes_atendidos(self): #4
        if not self.pila:
            print("---*** No se ha registrado nigún Paciente ***---\n")
        else:
            print("---*** Historial de Pacientes Atendidos ***---\n")

            for i in range(len(self.pila)-1,-1,-1):
                print(f'''{self.pila[i].id_pacientes}. Paciente: {self.pila[i].nombre} - Especialidad: {self.pila[i].especialidad} - Tiempo: {self.pila[i].tiempo_espera} minutos.''')

    def buscar_paciente(self):  # 5
        buscar = self.validacion_especialidad("Ingrese la Especialidad 'C'(Cardiología),'T'(Traumatología),'P'(Pediatría): ")
        encontrado = False

        print(f"---*** Pacientes de {buscar} en Espera ***---")
        for cola in self.cola:
            if cola.especialidad == buscar:
                print(f"Paciente: {cola.nombre} - Tiempo: {cola.tiempo_espera} minutos")
                encontrado = True

        print(f"\n---*** Pacientes de {buscar} en Atendidos (Historial) ***---")
        for pila in self.pila:
            if pila.especialidad == buscar:
                print(f"Atendido: {pila.nombre} - Tiempo: {pila.tiempo_espera} min")
                encontrado = True

        if not encontrado:
            print(f"No se ha registrado ningún paciente con la especialidad '{buscar}'.\n")

    def tiempo_total_atencion(self): #6
        if not self.cola:
            print("---*** No se ha registrado ningún Paciente ***---\n")
        else:
            total = 0
            for i in range(len(self.cola)):
                total += self.cola[i].tiempo_espera

            print(f"El tiempo total registrado de los pacientes es: {total} minutos.\n")

    def mayor_tiempo_atencion(self): #7
        if not self.cola:
            print("---*** No se ha registrado ningún Paciente ***---\n")
        else:
            pos = 0
            mayor_tiempo = self.cola[0].tiempo_espera
            for i in range(len(self.cola)):
                if self.cola[i].tiempo_espera > mayor_tiempo:
                    mayor_tiempo = self.cola[i].tiempo_espera
                    pos = i

            print(f"El Paciente con mayor tiempo de atención es: {self.cola[pos].nombre} con {mayor_tiempo} minutos.\n")

    def guardar_historial(self): #8
        if not self.pila:
            print("---*** No se ha registrado ningún Paciente ***---\n")
        else:
            try:
                with open(self.salida, "w", encoding="utf8") as archivo:
                    for paciente in self.pila:
                        archivo.write(f'''{paciente.nombre} - {paciente.especialidad} - {paciente.tiempo_espera}\n''')

                print("---*** Pacientes archivados correctamente ***---\n")
                for i in range(len(self.pila) - 1, -1, -1): print(
                    f'''{self.pila[i].id_pacientes}. Paciente: {self.pila[i].nombre} - Especialidad: {self.pila[i].especialidad} - Tiempo: {self.pila[i].tiempo_espera} minutos.''')

            except Exception as e:
                print(f"Error al guardar el archivo: {e}.")

    def cargar_pacientes_archivo(self):  # 9
        print("---*** Pacientes Archivados ***---\n")
        try:
            with open(self.salida, "r", encoding="utf8") as archivo:
                hay_dato = False
                for linea in archivo:
                    nombre, especialidad, tiempo_espera = linea.strip().split("-")
                    print(f"{nombre.strip()} - {especialidad.strip()} - {tiempo_espera.strip()}\n")

                    paciente = Pacientes(nombre.strip(), especialidad.strip(), int(tiempo_espera.strip()))
                    self.cola.append(paciente)
                    hay_dato = True

                if not hay_dato:
                    print("---*** No se ha registrado ningún Paciente ***---")

        except FileNotFoundError:
            print("---*** No hay pacientes cargados aún ***---\n")

class AtencionPacientes:

    def __init__(self):
        self.pacientes = SistemaPacientes("RegistroPaciente.txt","HistorialPaciente.txt")

    def iniciar_pacientes(self):
        salir = False
        while not salir:
            opcion = self.mostrar_menu()
            salir = self.ejecutar_opciones(opcion)

    def mostrar_menu(self):
        while True:
            print('''
            ********************************************************
            **----***** Sistema de Atención de Pacientes *****----**
            **|                                                  |**
            **|     1. Registrar los Pacientes                   |**
            **|     2. Mostrar los Pacientes                     |**
            **|     3. Atención de los Pacientes                 |**
            **|     4. Historial de Pacientes atendidos          |**
            **|     5. Buscar Pacientes por Especialidad         |**
            **|     6. Tiempo total de atención                  |**
            **|     7. Paciente con mayor tiempo de atención     |**
            **|     8. Historial archivada de los Pacientes      |**
            **|     9. Cargar pacientes desde archivo            |**
            **|     10. Salir del Programa                       |**
            **|                                                  |**                                              
            **----------------------------------------------------**
            ********************************************************\n''')

            try:
                return int(input("Seleccione una opción del menú: "))
            except ValueError:
                print("Ingrese la opción del (1-10)\n")

    def ejecutar_opciones(self,opcion):
        if opcion == 1:
            self.pacientes.registrar_pacientes()
        elif opcion == 2:
            self.pacientes.mostrar_cola()
        elif opcion == 3:
            self.pacientes.atender_paciente()
        elif opcion == 4:
            self.pacientes.mostrar_pacientes_atendidos()
        elif opcion == 5:
            self.pacientes.buscar_paciente()
        elif opcion == 6:
            self.pacientes.tiempo_total_atencion()
        elif opcion == 7:
            self.pacientes.mayor_tiempo_atencion()
        elif opcion == 8:
            self.pacientes.guardar_historial()
        elif opcion == 9:
            self.pacientes.cargar_pacientes_archivo()
        elif opcion == 10:
            print("---*** Fin del Programa ***---")
            return True
        else:
            print(f"Opción no valida: {opcion}\n")

        return False

if __name__ == "__main__":
    atendidos = AtencionPacientes()
    atendidos.iniciar_pacientes()