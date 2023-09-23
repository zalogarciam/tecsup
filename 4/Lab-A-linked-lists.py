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
        while current!=None:
            print(current.data, end=" ")
            current = current.next
        print()

    def search(self, data):
        current = self.head
        while current!=None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def concatenate(self, le2):
        le3 = LinkedList()
        current = self.head
        while current!=None:
            le3.insert_end(current.data)
            current = current.next
        
        current2 = le2.head
        while current2!=None:
            le3.insert_end(current2.data)
            current2 = current2.next
        return le3

    def length(self):
        return self.count
    
linked_list = LinkedList()
linked_list.insert_end(2)
linked_list.insert_end(1)
linked_list.insert_end(7)
linked_list.insert_end(9)
linked_list.insert_start(3)
linked_list.insert_end(8)
linked_list.insert_mid(4,2)
linked_list.print_linked_list()
linked_list.delete_first()
linked_list.print_linked_list()
linked_list.delete_last()
linked_list.print_linked_list()
linked_list.delete_mid(4)
linked_list.print_linked_list()
print(linked_list.search(7))

linked_list2 = LinkedList()
linked_list2.insert_end(3)
linked_list2.insert_end(4)
linked_list2.insert_end(0)

linked_list3 = linked_list.concatenate(linked_list2)
linked_list3.print_linked_list()

print(linked_list.length())

