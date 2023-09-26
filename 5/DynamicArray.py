class DynamicArray():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.index = 0

    def insert(self, value):
        if self.index == self.size: # Array is full
            # Duplicate array size
            new_array = [None] *  (self.size * 2)
            for i in range(self.size):
                new_array[i] = self.items[i]
            self.items = new_array
            self.size = self.size * 2
        self.items[self.index] = value
        self.index += 1

    def print_dynamic_array(self):
        for item in self.items:
            print("[", item, "]", end=" ")

dynamic_array = DynamicArray(6)
dynamic_array.insert(3)
dynamic_array.insert(4)
dynamic_array.insert(1)
dynamic_array.insert(0)
dynamic_array.insert(7)
dynamic_array.insert(8)
dynamic_array.insert(10)
dynamic_array.insert(6)
dynamic_array.insert(5)
dynamic_array.insert(8)
dynamic_array.insert(11)
dynamic_array.insert(15)
dynamic_array.insert(20)
dynamic_array.print_dynamic_array()