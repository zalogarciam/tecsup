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
# stack.print_stack()
# print(stack.pop())
# stack.print_stack()
# print(stack.is_empty())
# print(stack.size())
# print(stack.peek())

class ArrayStack():
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def print_stack(self):
        print(self.items)

array_stack = ArrayStack()
array_stack.push(3)
array_stack.push(5)
array_stack.push(2)
array_stack.push(7)
# array_stack.print_stack()
array_stack.pop()
# array_stack.print_stack()
# print(array_stack.size())
# print(array_stack.is_empty())
# print(array_stack.peek())

# Ejercicio 2

word= "EXTINTOR"

stack = []

for character in word:
    stack.append(character)

reverted_word = ''
while len(stack) >= 1:
    reverted_word += stack.pop()

# print(reverted_word )



# Ejercicio 4

input = ['2', '3', '1', '*', '+', '9', '-']

stack = []
for element in input:
    if element.isdigit(): 
        stack.append(element)
    else:
        elem1 = stack.pop()
        elem2 = stack.pop()
        result = eval(elem2 + element + elem1)
        stack.append(str(result))
# print(stack)


# Ejercicio 3

def parenthesis(input):
    stack = []
    if input[0] == ")": return False
    for parenthesis in input:
        if parenthesis == "(":
            stack.append(parenthesis)
        else:
            stack.pop()
    return len(stack) == 0

# print(parenthesis("(())"))
# print(parenthesis("(()())"))
# print(parenthesis("(()"))
# print(parenthesis(")()"))


def decimal_to_binary(number):
    stack = []
    result = ""
    while number >= 0:
        res = number % 2 
        stack.append(res)
        number = number // 2
        if number == 0 or number == 1:
            stack.append(number)
            break
    
    while len(stack) > 0:
        result += str(stack.pop())
    return result

print(decimal_to_binary(345))

