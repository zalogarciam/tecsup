class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    def insert_start(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def insert_mid(self, data, position):
        new_node = Node(data)
        current = self.head
        index = 0
        while current != None:
            if index == position:
                previous = current
                next = current.next
                previous.next = new_node
                new_node.next = next
                return
            current = current.next
            index +=1
        self.count += 1

    def delete_first(self):
            if self.head == None:
                raise Exception("Lista enlazada esta vacia")
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                second = self.head.next
                self.head.next = None
                self.head = second
            self.count -= 1

    def delete_last(self):
        if self.head == None:
            raise Exception("Lista enlazada esta vacia")
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while current != None:
                if current.next == self.tail:
                    break
                current = current.next
            current.next = None
            self.tail = current
        self.count -= 1

    def delete_mid(self, data):
        current = self.head
        previous = None
        while current != None:
            if current.next.data == data:
                previous = current
                current = current.next
                break
            current = current.next
        previous.next = current.next
        self.count -= 1

    def print_linked_list(self):
        current = self.head

        while (current != None):
            print(current.data, end="==>")
            current = current.next
        print("None")
lista_enlazada = LinkedList()
lista_enlazada.insert_end(4)
lista_enlazada.insert_end(13)
lista_enlazada.insert_start(7)
lista_enlazada.print_linked_list()