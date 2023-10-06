stack = []

stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.append(6)
print(stack)
stack.append(9) # Inserta en la siguiente stack[self.count] = NUEVO_VALOR O(1)
print(stack)
print(stack.pop())  # Elimina stack[len(stack) - 1] O(1)
print(stack)

# Lista enlazada --> self.head ... self.tail

# Pila

# Listas enlazadas
            # Tiempo    #       Espacio
# Push -->          O(1)           O(1)
# Pop -->           O(1)            O(1)
# Size -->          O(1)           O(1)
# Top/Peek -->      O(1)           O(1)

# Arreglos              Tiempo      Espacio
# Push -->              O(1)        O(1)
# Pop -->               O(1)        O(1)       
# Size -->              O(1)        O(1)
# Top/Peek -->          O(1)        O(1)

queue = []
queue.append((1, 1))
queue.append((0, 0))
queue.append((2, 2))
queue.append((3, 3))
print(queue)
