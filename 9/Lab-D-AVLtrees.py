class AVLNode():
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.height = None

class AVLTree():
    def __init__(self) -> None:
        self.root = None

    def insert_(self, value):
        self.root = self.insert(self.root, value)

    def insert(self, root, value):
        if root is None:
            return AVLNode(value)
        if value > root.data:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        root.height = self.set_height(root)
        return self.balance(root)
    
    def rotate_left(self, root):
        pass

    def rotate_right(self, root):
        pass    