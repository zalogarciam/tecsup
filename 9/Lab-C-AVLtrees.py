class AVLNode():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
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
        # root.height = self.set_height(root)
        # return self.balance(root)
        return root
    
    def in_order(self, root, level = 1):
        if root is not None:
            self.in_order(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order(root.right, level + 1)

    def rotate_left(self, root):
        pass

    def rotate_right(self, root):
        pass

avl_tree = AVLTree()
avl_tree.insert_(12)
avl_tree.insert_(3)
avl_tree.insert_(9)
avl_tree.insert_(4)
avl_tree.insert_(6)
avl_tree.insert_(2)
avl_tree.in_order(avl_tree.root)
