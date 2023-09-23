class Node():
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        # self.anterior = None # Lista doblemente enlazada
    
class ListaEnlazada():
    def __init__(self) -> None:
        self.cabeza = None
        self.cola = None

    def insertar(self, valor):
        pass

    def eliminar(self, valor):
        pass

    def indice(self, valor):
        pass

    def elemento(self, indice):
        pass

    def print_lista_enlazada(self):
        actual = self.cabeza
        while actual != None:
            print(actual.valor, end=" ")
            actual = actual.siguiente

    def busqueda(self, valor):
        actual = self.cabeza
        while actual != None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

lista_enlazada = ListaEnlazada()

nodo_1 = Node(3)
nodo_2 = Node(4)
nodo_3 = Node(6)
nodo_4 = Node(8)
nodo_5 = Node(1)

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_2.anterior = nodo_1 # lista doblemente enlazada
nodo_3.siguiente = nodo_4
nodo_4.siguiente = nodo_5

lista_enlazada.cabeza = nodo_1
lista_enlazada.cola = nodo_5
print(lista_enlazada.busqueda(8))
print(lista_enlazada.busqueda(99))

# lista_enlazada.cola.siguiente = lista_enlazada.cabeza # lista circular

lista_enlazada.print_lista_enlazada()
