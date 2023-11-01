class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class Tree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        pass

tree = Tree()
root_node = Node(8)
tree.root = root_node
tree.root.left = Node(3)
tree.root.right = Node(10)
