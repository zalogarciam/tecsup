# Stacks/Pilas
# Arrays            Time        Space
# Push              O(1)        O(1)  --> self.items[self.index]  
# Pop               O(1)        O(1)  --> self.items[0]
# Peek/Top          O(1)        O(1)  --> self.items[0]
# Size              O(1)        O(1)  --> self.index --> contador

# Linked Lists      Time        Space
# Push              O(1)        O(1) --> self.head = cima de la pila
# Pop               O(1)        O(1) --> self.head = cima de la pila
# Peek/Top          O(1)        O(1) --> self.head = cima de la pila
# Size              O(1)        O(1) --> self.count --> contador

# class Array


# Supoganmos que tenemos una pila implementada en base a un arreglo simple
# como el que se muestra a continuacion. ¿Cuál es el resultado de esas
# operaciones?
# class Stack(Array):
#     def __init__(self, capacity) -> None:
#         super().__init__()
#         self.items = [None] * capacity
#         self.capacity = capacity
#         self.count = 0
#     def push(self, value):
#         if self.count >= self.capacity:
#             raise Exception("Stack Overflow")
#         self.items[self.count] = value
#         self.count += 1
#     def print(self):
#         print(self.items)
# stack = Stack(5)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.print()

# Tenemos una pila implementada a base de una lista enlazada. Se realizan
# las siguientes operaciones:
# push('A')
# push('C')
# push('X')
# pop()
# pop()
# peek()
# push('G')
# pop()
# pop()
# is_empty()
# ¿Cuál es el resultado de la ultima operacion?


# Tenemos una pila implementada a base de una lista enlazada. Se realizan
# las siguientes operaciones:
# push(200)
# push(300)
# push(100)
# push(101)
# push(99)
# pop()
# push(94)
# pop()
# pop()
# size()
# ¿Cuál es el resultado de la ultima operacion?


# Tenemos una cola implementada a base de una lista enlazada. Se realizan
# las siguientes operaciones:
# enqueue('Juan')
# enqueue('Ricardo')
# dequeue()
# dequeue()
# enqueue('Jose')
# enqueue('Mary')
# enqueue('Eli')
# enqueue('Jesus')
# dequeue()
# dequeue()
# enqueue('Omar')
# front()
# ¿Cuál es el resultado de la ultima operacion?




# Tenemos una cola de prioridad y se realiza las siguientes operaciones:
# Recuerda que en este caso, el que tiene un numero mas bajo, tiene mayor 
# prioridad; y que si dos elementos tienen la misma prioridad, se 
# considera el principio FIFO
from queue import PriorityQueue
q = PriorityQueue()

q.put((1, 'Jeff'))
q.put((1, 'Paulo'))
q.put((0, 'David'))
print(q.get())
q.put((2, 'Mike'))
print(q.get())
print(q.get())
q.put((3, 'Brittany'))
q.put((2, 'Thomas'))
q.put((3, 'Rayan'))
print(q.get())

# ¿Cuál es el resultado de la ultima operacion?

