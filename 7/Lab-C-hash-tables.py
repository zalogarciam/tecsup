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

    def search(self, data):
        current = self.head
        while current!=None:
            if current.data == data:
                return current.data
            current = current.next
        return None
    
    def print_linked_list(self):
        current = self.head
        while current!=None:
            print(current.data, end=" ")
            current = current.next
        print()

    def to_array(self):
        array = []
        current = self.head
        while current!=None:
            array.append(current.data)
            current = current.next
        return array

class KeyValue():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return 'Key: ' + str(self.key) + ' Value:' + self.value

class HashTable():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size

    def put(self, key, value):
        # key_value = KeyValue(key, value)
        hash_index = self.hash(key)
        if self.items[hash_index] is None:
            self.items[hash_index] = LinkedList()
        self.items[hash_index].insert_end(value)

    def get(self, key):
        hash_index = self.hash(key)
        linked_list = self.items[hash_index]
        if linked_list.length() == 1:
            return self.items[hash_index].head.data
        else:
            result = linked_list.search(chr(key))
            return result

    def remove(self, key):
        hash_index = self.hash(key)
        linked_list = self.items[hash_index]
        if linked_list.length() == 1:
            linked_list.delete_first()
            self.items[hash_index] = None
        else:
            linked_list.delete_mid(chr(key))
    
    def hash(self, key):
        return key % self.size
    
    def print(self):
        for item in self.items:
            if item is not None:
                item.print_linked_list()

    def keys(self):
        keys = []
        for item in self.items:
            if item != None:
                array = item.to_array()
                for i in array:
                    keys.append(ord(i))
        return keys

    def values(self):
        values = []
        for item in self.items:
            if item != None:
                values.extend(item.to_array())
        return values

hash_table = HashTable(10)
hash_table.put(97, 'a')
hash_table.put(98, 'b')
hash_table.put(99, 'c')
hash_table.put(100, 'd')
hash_table.put(101, 'e')
hash_table.put(102, 'f')
hash_table.put(107, 'k')
hash_table.put(117, 'u')
# print('GET', hash_table.get(98))
# print('GET', hash_table.get(107))
hash_table.remove(107)
# hash_table.print()
print(hash_table.keys())
print(hash_table.values())
# Tablas Hash

# dictionary = {}

# dictionary[97] = 'a'
# dictionary[98] = 'b'
# dictionary[99] = 'c'

# # print(dictionary)

# words= ['car', 'delete', 'zip', 'delete', 'delete', 'car']
# car: 2
# delete: 3
# zip : 1
# text = "car delete zip delete delete car"
# words = text.split(' ')
# # print(words)
# dictionary = {}
# for word in words:  #O(n) donde n es el numero de palabras del text
#     if word not in dictionary:
#         dictionary[word] = 1
#     else:
#         dictionary[word] += 1
# print(dictionary)

# array = [1,4,4,4,2,3,2,2,3]
# # 1,2,3,4
# dictionary = {}

# for number in array: #O(n) donde n es el numero de elementos del arreglo.
#     if number not in dictionary:
#         dictionary[number] = number
    
# print(list(dictionary.keys()))
# print(list(dictionary.values()))

# Puente de la Vega

# array = [1, 2, 2, 2,2,2,2,2, 3, 3, 3, 4]
# dictionary = {}
# for number in array:
#     if number not in dictionary:
#         dictionary[number] = 1
#     else:
#         dictionary[number] += 1
# print(dictionary)
# num_com = max(dictionary, key=dictionary.get)
# print(num_com)


input = {1:True, 7:True, 5:True, 9:True, 2:True, 12:True, 3:True}
k = 2
count = 0
for i in input: # O(n^2)
    for j in input:
        if (i - j) == k:
            count += 1
print(count)

count = 0
for number in input:
    if number + k in input:
        count += 1
