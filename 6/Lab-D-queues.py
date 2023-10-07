

from datetime import date


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
            deleted_item = self.head
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

    def size(self):
        return self.count
    
    def front(self):
        return self.head.data
    
    def is_empty(self):
        return self.count == 0
    
# queue = Queue()
# queue.enqueue(7)
# queue.enqueue(1)
# queue.enqueue(0)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.print_linked_list()
# print(queue.dequeue())
# print(queue.size())
# print(queue.is_empty())
# print(queue.front())
# queue.print_linked_list()

class QueueArray():
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        # del, remove, pop
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0

    def print(self):
        print(self.items)

# queue = QueueArray()
# queue.enqueue(7)
# queue.enqueue(1)
# queue.enqueue(0)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.print()
# print(queue.dequeue())
# print(queue.size())
# print(queue.is_empty())
# print(queue.front())
# queue.print()


class SocialNetwork():
    def __init__(self, name) -> None:
        self.name = name

class User():
    def __init__(self, name) -> None:
        self.name = name
        self.email = None
        self.phone = None
        self.queue = []

    def send_message(self, content, to):
        msg = Message(content)
        to.queue.append(msg)

    def receive_message(self):
        msg = self.queue.pop(0)
        print(msg)

    # def enqueue_message(self):
    #     pass

class Message():
    def __init__(self, content) -> None:
        self.content = content
        self.date = date.today()

    def __str__(self) -> str:
        return self.content + " (Message sent at " + str(self.date) + ")"

# facebook = SocialNetwork("Facebook")
# gerardo = User("Gerardo")
# mary = User("Mary")
# gerardo.send_message("Hello...", mary)
# gerardo.send_message("How are you...", mary)
# gerardo.send_message("Why ...", mary)
# gerardo.send_message("Hey...", mary)
# gerardo.send_message(".....", mary)
# gerardo.send_message("Bye ...", mary)
# mary.receive_message()
# mary.receive_message()
# mary.receive_message()
# mary.receive_message()

class Element():
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority

    def __str__(self) -> str:
        return "Value: " + str(self.value) + " Priority: " + str(self.priority)

class PriorityQueue():
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, element):
        if len(self.items) == 0:
            self.items.append(element)
        else:
            for i in range(len(self.items)):
                if element.priority >= self.items[i].priority:
                    break
            self.items.insert(i, element)

    def print(self):
        for item in self.items:
            print(item)

# priority_queue = PriorityQueue()
# priority_queue.enqueue(Element(3, 1))
# priority_queue.enqueue(Element(1, 3))
# priority_queue.enqueue(Element(8, 3))
# priority_queue.enqueue(Element(9, 7))
# priority_queue.enqueue(Element(5, 5))
# priority_queue.print()