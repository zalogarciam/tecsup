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
        self.items[hash_index] = key_value

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
hash_table.print()
