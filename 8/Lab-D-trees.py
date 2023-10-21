class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

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

    def insert_(self, data, root):
        if root is None:
            return Node(data)
        else:
            if data > root.data:
                root.right = self.insert_(data, root.right)
            else:
                root.left = self.insert_(data, root.left)
        return root
    
    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

bst = BinarySearchTree()
bst.root = Node(8)
bst.insert_(4, bst.root)
bst.insert_(15, bst.root)
bst.insert_(1, bst.root)
bst.insert_(6, bst.root)
bst.insert_(13, bst.root)
bst.insert_(18, bst.root)
bst.insert_(14, bst.root)
bst.in_order(bst.root)