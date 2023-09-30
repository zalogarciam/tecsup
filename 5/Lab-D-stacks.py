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

    def length(self):
        return self.count

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
        pop_item = None
        if self.head == None:
            raise Exception("Lista enlazada esta vacia")
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while current != None:
                if current.next == self.tail:
                    pop_item = current.next.data
                    break
                current = current.next
            current.next = None
            self.tail = current
        self.count -= 1
        return pop_item

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

class Stack(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def push(self, value):
        self.insert_end(value)

    def pop(self):
        return self.delete_last()

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def peek(self):
        return self.tail.data

    def print_stack(self):
        self.print_linked_list()

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(7)
stack.print_stack()
print(stack.pop())
stack.print_stack()
print(stack.is_empty())
print(stack.size())
print(stack.peek())
