class AVLNode():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.height = None
    
class AVLTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, value):
        if root is None:
            return AVLNode(value)
        if value > root.data:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root
    
    def rotate_left():
        pass

    def rotate_right():
        pass

    def in_order(self, root, level = 1):
        if root is not None:
            self.in_order(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order(root.right, level + 1)

tree = AVLTree()
tree.root = AVLNode(12)
tree.insert(tree.root, 3)
tree.insert(tree.root, 9)
tree.insert(tree.root, 4)
tree.insert(tree.root, 6)
tree.insert(tree.root, 2)
tree.in_order(tree.root)