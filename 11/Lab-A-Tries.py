class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.children = {}
        self.eow = False # Fin de palabra

    def remove_child(self, char):
        self.children.pop(char)

class Trie():
    def __init__(self) -> None:
        self.root = Node("NULL")

    def insert(self, string):
        current = self.root
        for char in string:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.eow = True

    def traverse(self):
        self.traverse_(self.root)

    def traverse_(self, node):
        pass