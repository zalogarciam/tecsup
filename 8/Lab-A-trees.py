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

    def delete(self, root, value):
        if root is None:
            return
        if value > root.data:
            root.right = self.delete(root.right, value)
        elif value < root.data:
            root.left = self.delete(root.left, value)
        else:
            # Leaf Node?
            if root.left is None and root.right is None:
                return None
            
            # One child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Two chidren
            min_value = self.min(root.right)
            root.data = min_value
            root.right = self.delete(root.right, min_value)
        
        return root

    def min(self, root):
        if root.left is None: return root.data
        return self.min(root.left)
    
    def search(self, root, value):
        if root is None:
            return False
        if value == root.data:
            return True
        elif value > root.data:
            return self.search(root.right, value)
        else:
            return self.search(root.left, value)

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
bst.root = Node(4)

bst.insert_(bst.root, 2)
bst.insert_(bst.root, 6)
bst.insert_(bst.root, 1)
bst.insert_(bst.root, 3)
bst.insert_(bst.root, 5)
bst.insert_(bst.root, 0)
bst.delete(bst.root, 4)
print(bst.search(bst.root, 0))
print(bst.search(bst.root, 4))
bst.in_order(bst.root)

# bst_root = Node(10)
# bst_root.left = Node(7)
# bst_root.right = Node(15)
# bst.root = bst_root