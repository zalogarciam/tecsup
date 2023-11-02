class Heap():
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, value):
        self.items.append(value)
        self.size += 1
        self.bubble_up(self)

    def bubble_up(self):
        pass

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def parent(self, index): # Get index parent
        return (index - 1) // 2

    def left_child(self, index): # return left child value
        return self.items[self.left_child_index(index)]

    def right_child(self, index): # return right child value
        return self.items[self.right_child_index(index)]

    def left_child_index(self, index): # return left index
        return index * 2 + 1

    def right_child_index(self, index): # return right index
        return index * 2 + 2
    
    def has_left_child(self, index): 
        return self.left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.right_child_index(index) < self.size

    # Return larger child between left and right
    def larger_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)
        
        left = self.left_child(index)
        right = self.right_child(index)
        if left >= right:
            return self.left_child_index(index)
        else:
            return self.right_child_index(index)