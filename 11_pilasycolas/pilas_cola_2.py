print("\n---*** Pilas manual con indice ***---")
pila = [1, 2, 3, 4]
print(pila)
pila = pila[:-1]
print(pila)
pila = pila[:-1]
print(pila)
pila = pila[:-1]
print(pila)
pila = pila[:-1]
print(f"{pila}\n")

clientes = ["Ana", "Luis", "Pedro", "Sofia", "Carlos"]
atendidos = []

# sacar el último
for _ in range(3):
    atendidos.append(clientes.pop())
     # “corrés” la pila

print("Atendidos:", atendidos)  #Esta es la forma más fácil
print("Cola final:", clientes)

# pila.pop()
# sacás el último (LIFO)

print("\n---*** Cola manual con índices ***---")

clientes = ["Ana", "Luis", "Pedro"]
atendidos = []

# Paso 1: llega Sofía
clientes.append("Sofia")
# Paso 2: se atiende 1
atendidos.append(clientes.pop(0))
# Paso 3: llega Carlos
clientes.append("Carlos")
# Paso 4: se atienden 2
atendidos.append(clientes.pop(0))
atendidos.append(clientes.pop(0))

print(f"Atendidos: {atendidos}")
print(f"Cola final: {clientes}\n")

clientes = ["Ana", "Luis", "Pedro"]
atendidos = []

# llega Sofía
clientes.append("Sofia")
# atender 1
atendidos.append(clientes[0])
clientes = clientes[1:]  # eliminas el primero
# llega Carlos
clientes.append("Carlos")
# atender 2
atendidos.append(clientes[0])
clientes = clientes[1:]
atendidos.append(clientes[0])
clientes = clientes[1:]

print("Atendidos:", atendidos)
print("Cola final:", clientes)

numeros = [1,2,3,4]
print(f"\n{numeros}")
numeros = numeros[1:]
print(f"{numeros}")
numeros = numeros[1:]
print(f"{numeros}")
numeros = numeros[1:]
print(f"{numeros}")
numeros = numeros[1:]
print(f"{numeros}\n")

clientes = ["Ana", "Luis", "Pedro", "Sofia", "Carlos"]
atendidos = []

# atender los 3 primeros
for _ in range(3):
    atendidos.append(clientes[0])
    clientes = clientes[1:]  # “corrés” la cola

print("Atendidos:", atendidos)  #Esta es la forma más fácil
print("Cola final:", clientes)

# cola.pop(0) o popleft()
# sacás el primero (FIFO)

clientes = ["Ana", "Luis", "Pedro", "Sofia", "Carlos"]
atendidos = []
