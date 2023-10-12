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

    def put(self, key, value):
        key_value = KeyValue(key, value)
        hash_index = self.hash(key)
        if self.items[hash_index] == None:
            self.items[hash_index] = key_value
        else:
            while self.items[hash_index] != None:
                hash_index += 1
                if self.items[hash_index] != None:
                    continue
                if hash_index >= self.size:
                    hash_index = 0
                self.items[hash_index] = key_value
                break

    def get(self, key):
        hash_index = self.hash(key)
        return self.items[hash_index].value

    def hash(self, key):
        return key % self.size
    
    def print(self):
        for item in self.items:
            print(item)

hash_table = HashTable(10)
hash_table.put(44, "Jorge")
hash_table.put(88, "Juan")
hash_table.put(55, "Maria")
hash_table.put(14, "Roy")
# hash_table.print()

# Ejercicio 4

dict = {"Ed":17 , "Roy": 23, "Edgar":27, "Juan":19, "Jean":18}

maximum = -999999
minimum = 999999
key_max = None
key_min = None
for persona in dict:
    if dict[persona] > maximum:
        maximum = dict[persona]
        key_max = persona
    if dict[persona] < minimum:
        minimum = dict[persona]
        key_min = persona
print(key_max)
print(key_min)