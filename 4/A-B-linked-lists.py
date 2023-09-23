# Crear un Nodo para la lista enlazada

class Nodo():
    def __init__(self, dato) -> None:
        self.data = dato
        self.next = None
        self.previous = None #  Lista doblemente enlazada

class ListaEnlazada():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        # Logica para insertar el elemento

    def eliminar(self, valor):
        pass

    def busqueda(self, valor):
        current = self.head
        while current != None:
            if current.data == valor:
                return True 
            current = current.next
        return False

lista_enlazada = ListaEnlazada()
nodo_1 = Nodo(3)
nodo_2 = Nodo(5)
nodo_3 = Nodo(7)
nodo_4 = Nodo(10) 
# head                    # tail
# (3) --> (5) --> (7) --> (10) --> None
lista_enlazada.head = nodo_1
nodo_1.next = nodo_2
nodo_2.next = nodo_3
nodo_3.next = nodo_4

#  Lista doblemente enlazada
# nodo_4.previous = nodo_3
# nodo_3.previous = nodo_2
# nodo_2.previous = nodo_1

lista_enlazada.tail = nodo_4

nodo_4.next = nodo_1 # opc1
lista_enlazada.tail.next = lista_enlazada.head # opc2
print(lista_enlazada.busqueda(7))