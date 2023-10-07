
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def length(self):
        return self.count
    
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
        deleted_item = None
        if self.head == None:
            raise Exception("Lista enlazada esta vacia")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            deleted_item = self.head
            second = self.head.next
            self.head.next = None
            self.head = second
        self.count -= 1
        return deleted_item.data

    def delete_last(self):
        deleted_value = None
        if self.head == None:
            raise Exception("Lista enlazada esta vacia")
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while current != None:
                if current.next == self.tail:
                    deleted_value = current.next.data
                    break
                current = current.next
            current.next = None
            self.tail = current
        self.count -= 1
        return deleted_value
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


class Queue(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, value):
        self.insert_end(value)

    def dequeue(self):
        return self.delete_first()
    
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def front(self):
        return self.head.data
    
    def print_queue(self):
        self.print_linked_list()

# queue = Queue()
# queue.enqueue(3)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(9)
# print(queue.dequeue())
# print(queue.is_empty())
# print(queue.size())
# queue.print_queue()

class ArrayQueue():
    def __init__(self) -> None:
        self.items = [] # array

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def print_queue(self):
        print(self.items)

# queue_stack = ArrayQueue()
# queue_stack.enqueue(3)
# queue_stack.enqueue(5)
# queue_stack.enqueue(6)
# queue_stack.enqueue(7)
# queue_stack.enqueue(9)
# queue_stack.print_queue()
# queue_stack.dequeue()
# queue_stack.print_queue()

# Ejercicio 2

class Client():
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.address = None
        self.age = None

    def __str__(self) -> str:
        return 'Name: '+ self.name + '  Id: ' + str(self.id)

class SuperMarket():
    def __init__(self, name) -> None:
        self.name = name
        self.queue = []

    def register(self, client):
        self.queue.append(client)

    def atender(self):
        self.queue.pop(0)

    def show(self):
        for item in self.queue:
            print(item)

# market = SuperMarket("KOSTO")
# market.register(Client('Maria', 12121212))
# market.register(Client('Gerardo', 13131313))
# market.register(Client('Jesus', 14141414))
# market.register(Client('Mary', 14141414))
# market.show()
# market.atender()
# market.show()

class Processor():
    def __init__(self) -> None:
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)

    def process(self):
        return self.queue.pop(0)
    
    def total_time(self):
        total_time = 0
        for task in self.queue:
            total_time += task.time
        return total_time

class Task():
    def __init__(self, name, time) -> None:
        self.name = name
        self.time = time

# processor = Processor()
# processor.add_task(Task('A', 10))
# processor.add_task(Task('B', 15))
# processor.add_task(Task('C', 20))
# processor.add_task(Task('D', 25))
# processor.process()
# print(processor.total_time())

class Element():
    def __init__(self, name, priority) -> None:
        self.name = name
        self.priority = priority

    def __str__(self) -> str:
        return 'Name: ' + self.name + '  Priority: ' + str(self.priority)

class PriorityQueue():
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, element):
        if len(self.items) == 0:
            self.items.append(element)
        else:
            for i in range(len(self.items)):
                if self.items[i].priority <= element.priority:
                    break
            self.items.insert(i, element)

    def dequeue(self):
        self.items.pop(0)

    def print_priority_queue(self):
        for item in self.items:
            print(item)

priority_queue = PriorityQueue()
priority_queue.enqueue(Element('B', 2))
priority_queue.enqueue(Element('C', 4))
priority_queue.enqueue(Element('A', 4))
priority_queue.enqueue(Element('X', 10))
priority_queue.enqueue(Element('W', 13))

priority_queue.enqueue(Element('Y', 5))

priority_queue.enqueue(Element('F', 4))

priority_queue.print_priority_queue()