class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if (current.data > value):
                    if current.left is None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    current = current.right

    def in_order(self, root, level = 1):
        if root is not None:
            self.in_order(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order(root.right, level + 1)


bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.in_order(bst.root)

# bst_root = Node(10)
# bst_root.left = Node(7)
# bst_root.right = Node(15)
# bst.root = bst_root