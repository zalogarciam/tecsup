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
        root.height = self.set_height(root)
        return self.balance(root)
    
    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def height(self, node):
        if node is None:
            return -1
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def set_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def in_order(self, root, level = 1):
        if root is not None:
            self.in_order(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order(root.right, level + 1)

    def left_heavy(self, node):
        return self.balance_factor(node) > 1

    def right_heavy(self, node):
        return self.balance_factor(node) < -1

    def balance_factor(self, node):
        if node is None: return 0
        else: return self.height(node.left) - self.height(node.right)

    def balance(self, root):
        if self.left_heavy(root):
            if self.balance_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        elif self.right_heavy(root):
            if self.balance_factor(root.right) > 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root
    
tree = AVLTree()
tree.insert_(12)

tree.insert_(3)
tree.insert_(9)
tree.insert_(4)
tree.insert_(6)
tree.insert_(2)
tree.in_order(tree.root)