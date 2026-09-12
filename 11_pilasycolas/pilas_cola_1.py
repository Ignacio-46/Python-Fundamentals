# Pila (Stack)
# Una pila funciona como una pila de platos: 'El último que entra es el primero que sale'
# Esto se llama LIFO (Last In, First Out). Ejemplo:
# Agrego: 1 → 2 → 3
# Pila: [1, 2, 3] ← el 3 está arriba
# Saco (pop): sale el 3 primero

print("---*** Pila ***---")
pila = []
pila.append(1) #Push
pila.append(2)
pila.append(3)
pila.pop()  # elimina el 3

# peek: pila[-1] muestra el último
print(f"Último elemento: '{pila[-1]}'")
print(f"Pila completa: {pila}")

print("\n---*** Listas de Pila ***---")
numeros = [1, 2, 3, 4, 5]
pila = []
invertido = []

# Paso 1: meter en la pila
for n in numeros:
    pila.append(n) #meter en pila (mejor con loop)

print(f"Pila completa: '{pila}'")

# Paso 2: sacar de la pila y guardar en invertido
while len(pila) > 0:
    invertido.append(pila.pop()) #sacar correctamente (LIFO real)

print(f"Invertido: {invertido}")

#Validar paréntesis con PILA
print("\n---*** Validar Pila ***---")
texto = "(())()"
pila = []

for c in texto:
    if c == "(":
        pila.append(c)
    elif c == ")":
        if len(pila) == 0:
            print("Incorrecto")
            break
        pila.pop()
else:
    if len(pila) == 0:
        print("Correcto")
    else:
        print("Incorrecto")

# Cola (Queue)
# Una cola funciona como una fila de personas: 'El primero que entra es el primero que sale'
# Esto se llama FIFO (First In, First Out). Ejemplo:
# Agrego: 1 → 2 → 3
# Cola: [1, 2, 3] ← el 1 está primero
# Saco (dequeue):sale el 1 primero

print("\n---*** Cola ***---")

from collections import deque
cola = deque()
cola.append(1) #enqueue
cola.append(2)
cola.append(3)
cola.popleft()  #dequeue: elimina el 1

# front: cola[0] muestra el primero
print(f"Primer elemento:'{cola[0]}'")
print(f"Cola completa: {cola}")

print("\n---*** Listas de Cola ***---")
from collections import deque

clientes = deque(["Ana", "Luis", "Pedro"])
atendidos = []

# Paso 1: llega Sofía
clientes.append("Sofia")
# Paso 2: se atiende 1
atendidos.append(clientes.popleft())
# Paso 3: llega Carlos
clientes.append("Carlos")
# Paso 4: se atienden 2
atendidos.append(clientes.popleft())
atendidos.append(clientes.popleft())

print("Atendidos:", atendidos)
print("Cola final:", list(clientes))
