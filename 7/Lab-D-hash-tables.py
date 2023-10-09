class KeyValue():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return "Key: " + str(self.key) + " Value: " + self.value

class HashTable():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.count = 0

    # Linear Probing (Sondeo Lineal): 
    def put(self, key, value):
        key_value = KeyValue(key, value)
        hash_value_index = self.hash(key)
        if self.items[hash_value_index] == None: # Si no existe colision
            self.items[hash_value_index] = key_value
        else: # Si existe colision ...
            while self.items[hash_value_index] != None:
                hash_value_index += 1
                if hash_value_index == (self.size - 1):
                    hash_value_index = 0
            self.items[hash_value_index] = key_value

    def get(self, key):
        hash_value_index = self.hash(key)
        key_value = self.items[hash_value_index]
        if key == key_value.key:
            return self.items[hash_value_index]
        else:
            while self.items[hash_value_index].key != key:
                hash_value_index += 1
                if hash_value_index == (self.size - 1):
                    hash_value_index = 0
            return self.items[hash_value_index]

    def remove(self, key):
        hash_value_index = self.hash(key)
        key_value = self.items[hash_value_index]
        if key == key_value.key:
            self.items[hash_value_index] = None
        else:
            while self.items[hash_value_index].key != key:
                hash_value_index += 1
                if hash_value_index == (self.size - 1):
                    hash_value_index = 0
                while self.items[hash_value_index] == None:
                    hash_value_index += 1

            self.items[hash_value_index] = None

    def keys(self): # O(n) donde n es el tamano de la tabla Hash = self.size
        key_list = []
        for item in self.items:
            if item != None:
                key_list.append(item.key)
        return key_list

    def values(self): # O(n) donde n es el tamano de la tabla Hash = self.size
        value_list = []
        for item in self.items:
            if item != None:
                value_list.append(item.value)
        return value_list

    def length(self):
        return self.size

    def print(self):
        for item in self.items:
            print(item)
        print()

    def hash(self, key):
        return key % self.size

hash_table = HashTable(10)
hash_table.put(65, 'A')
hash_table.put(66, 'B')
hash_table.put(67, 'C')
hash_table.put(68, 'D')
hash_table.put(69, 'E')
hash_table.put(70, 'F')
hash_table.put(71, 'G')
# hash_table.print()
hash_table.put(75, 'K')
hash_table.remove(67)
hash_table.remove(75)
# hash_table.print()
# print('65', hash_table.get(65))
# print('70', hash_table.get(70))
# print('75', hash_table.get(75))

# print(hash_table.keys())
# print(hash_table.values())


# Ejercicio 4

words = ['car', 'watch', 'tv', 'day', 'car', 'car', 'watch', 'end', 'car', 'watch']

dictionary = {}

for word in words: # Complejidad O(n) donde n es el numero de palabras 
    if word not in dictionary: dictionary[word] = 1
    else: dictionary[word] += 1
# print(dictionary)
        
# def elimiduplica(n):
#     # eleunicos = {}  
#     resultado = []
#     for elemento in n:
#         if elemento not in resultado:
#             resultado.append(elemento)
#             # eleunicos[elemento] = True
#     return resultado
# arreglo = [1, 1,45,12,78,12, 45,12]
# resultado = elimiduplica(arreglo)
# print(resultado)

# def delDuplicate(numbers):
#     uniqueNumbers = {}
#     result = []
#     for i in numbers:
#         if i not in uniqueNumbers:
#             uniqueNumbers[i] = True
#             result.append(i)
#     return result
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# result = delDuplicate(numbers)
# print(result)

# Ejercicio 5

array =  [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
dictionary = {}

for item in array:
    if item not in dictionary: 
        dictionary[item] = True
# print(list(dictionary.keys()))

array = [1, 2, 2, 3, 3, 3, 4]
dictionary = {}

for number in array: # O(n)
    if number not in dictionary:
        dictionary[number] = 1
    else:
        dictionary[number] += 1

max = -1
result = 0
for key in dictionary: # O(n)
    if dictionary[key] >  max:
        max = dictionary[key]
        result = key

# print('Max: ', result)
# print(dictionary)

array =  [1, 7, 5, 9, 2, 12, 3] 
K=2
dictionary = {}

for number in array:
    dictionary[number] = True

# print(dictionary)
count = 0
for num in dictionary:
    if (num + K) in dictionary:
        count += 1
print(count)