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

    def insert_(self, root, value):
        if root is None:
            return Node(value)
        if value > root.data:
            root.right = self.insert_(root.right, value)
        else:
            root.left = self.insert_(root.left, value)
        return root

    def in_order(self, root, level = 1):
        if root is not None:
            self.in_order(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order(root.right, level + 1)

    def pre_order(self, root, level = 1):
        if root is not None:
            print(str(root.data))
            self.pre_order(root.left, level + 1)
            self.pre_order(root.right, level + 1)

    def post_order(self, root, level = 1):
        if root is not None:
            self.post_order(root.left, level + 1)
            self.post_order(root.right, level + 1)
            print(str(root.data))

bst = BinarySearchTree()
tmp = bst.insert_(bst.root, 4)
tmp = bst.insert_(tmp, 2)
tmp = bst.insert_(tmp, 6)
tmp = bst.insert_(tmp, 1)
tmp = bst.insert_(tmp, 3)
tmp = bst.insert_(tmp, 5)
tmp = bst.insert_(tmp, 4.5)
bst.post_order(tmp)

# bst_root = Node(10)
# bst_root.left = Node(7)
# bst_root.right = Node(15)
# bst.root = bst_root