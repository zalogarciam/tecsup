class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
                else:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left

    def insert_(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.insert_(root.right, data)
        else:
            root.left = self.insert_(root.left, data)
        return root
    
    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
            
bst = BinarySearchTree()
bst.root = Node(10)
bst.insert_(bst.root, 5)
bst.insert_(bst.root, 13)
bst.insert_(bst.root, 2)
bst.insert_(bst.root, 9)
bst.insert_(bst.root, 11)
bst.insert_(bst.root, 16)
bst.insert_(bst.root, 12)
bst.in_order(bst.root)