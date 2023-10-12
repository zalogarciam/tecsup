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

    def insert_start(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count +=1

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count +=1

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
        self.count+=1

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
        self.count -=1

    def longitud(self):
        return self.count

    def print_linked_list(self):
        current = self.head
        while current != None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

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
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(1)
# queue.enqueue(3)
# queue.enqueue(8)
# queue.print_linked_list()
# queue.dequeue()
# print(queue.size())
# print(queue.front())
# print(queue.is_empty())

class ArrayQueue():
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
    


class Clinic():
    def __init__(self, name) -> None:
        self.name = name
        self.web = None
        self.address = None
        self.queue = []

    def add(self, appointment):
        self.queue.append(appointment)

    def attended(self):
        self.queue.pop(0)

    def show(self):
        for appointment in self.queue:
            print(appointment)

    def calculate_average(self):
        sum = 0
        for appointment in self.queue:
            sum = appointment.difference
        return sum // len(self.queue)

class Patient():
    def __init__(self, name) -> None:
        self.name = name
        self.id = None
        self.address = None
        self.age = None

class Appointment():
    def __init__(self, patient, date, room) -> None:
        self.patient = patient
        self.date = date
        self.start_date = None
        self.end_date = None
        self.difference = self.end_date - self.start_date
        self.room = room

    def __str__(self) -> str:
        result = ""
        result += "Patient: " + self.patient.name + "\n"
        result += "Date: " + self.date + "\n"
        result += "Room: " + self.room + "\n"
        return result
       
# clinica = Clinic("Espiritu Santo")
# appointment1 = Appointment(Patient('Raul'), "10/7/2023", "A101")
# appointment2 = Appointment(Patient('Jessica'), "10/20/2023", "A102")
# appointment3 = Appointment(Patient('Jorge'), "10/12/2023", "A101")
# clinica.add(appointment1)
# clinica.add(appointment2)
# clinica.add(appointment3)
# clinica.show()
# clinica.attended()
# clinica.show()
# clinica.attended()
# clinica.show()


class Element():
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority

    def __str__(self) -> str:
        return "Value: " + self.value + " Priority: " + str(self.priority)

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

    def show(self):
        for element in self.items:
            print(element)

priority_queue = PriorityQueue()
priority_queue.enqueue(Element("A", 1))
priority_queue.enqueue(Element("C", 3))
priority_queue.enqueue(Element("X", 3))
priority_queue.enqueue(Element("F", 10))
priority_queue.enqueue(Element("G", 5))

# priority_queue.show()

class Event():
    def __init__(self, name) -> None:
        self.name = name
        self.queue = []
    
    def add(self, participant):
        self.queue.append(participant)

    def remove(self):
        self.queue.pop(0)

    def show(self):
        print("PARTICIPANTS")
        for participant in self.queue:
            print(participant)

class Participant():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

event = Event("Fito Paez")
event.add(Participant('Marco'))
event.add(Participant('Jesus'))
event.add(Participant('Mary'))
event.add(Participant('Jess'))
event.add(Participant('Pedro'))
event.show()
event.remove()
event.show()