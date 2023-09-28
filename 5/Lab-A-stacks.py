stack = []

stack.append(1)
stack.append(3)
stack.append(5)
stack.append(7)
stack.append(0)

pop_item = stack.pop()
# print(pop_item)
# print(stack)

# Stack Implementation

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


class Stack(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def push(self, value):
        self.insert_start(value)

    def pop(self):
        return self.delete_first()
    
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def print_stack(self):
        self.print_linked_list()

# stack = Stack()
# stack.push(1)
# stack.push(3)
# stack.push(5)
# stack.push(7)
# stack.push(0)
# print(stack.pop())
# print(stack.is_empty())
# print(stack.size())
# stack.print_stack()


class ArrayStack():
    def __init__(self) -> None:
        self.items = [] # array

    def push(self, value):
        self.items.append(value)
        # insert at the beginning

    def pop(self):
        # return self.items[0]
        # return self.items[len(self.items) - 1]
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)

# array_stack = ArrayStack()
# array_stack.push(1)
# array_stack.push(3)
# array_stack.push(5)
# array_stack.push(7)
# array_stack.push(0)
# array_stack.print_stack()
# array_stack.pop()
# array_stack.print_stack()

# Ejercicio 2

# word = "METRO"
# stack = []
# for character in word:
#     stack.append(character)

# for i in range(len(word)):
#     print(stack.pop())


# Ejercicio 3

def parenthesis_comparison(parenthesis):
    stack = []
    if parenthesis[0] == ")": return False
    for char in parenthesis:
        if char == "(":
            stack.append(char)
        if char == ")":
            stack.pop()
    if len(stack) == 0:
        return True
    else: return False

# print(parenthesis_comparison("(())"))
# print(parenthesis_comparison("((()()))"))
# print(parenthesis_comparison("((()()"))
# print(parenthesis_comparison("((())"))
# print(parenthesis_comparison(")("))


# Ejercicio 4

expression = ["2", "3", "1", "*", "+", "9", "-"]

stack = []
for item in expression:
    if item.isdigit():
        stack.append(item)
    else:
        element1 = stack.pop()
        element2 = stack.pop()
        result = eval(element2 + item + element1)
        stack.append(str(result))
print(stack)