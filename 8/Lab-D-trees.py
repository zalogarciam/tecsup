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

    def pre_order(self, root):
        if root != None:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root != None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)

    def in_order_level(self, root, level= 0):
        if root != None:
            self.in_order_level(root.left, level + 1)
            print((level * 4 * "-") + str(root.data))
            self.in_order_level(root.right, level + 1)

    def search(self, data, root):
        if root is None:
            return False
        else:
            if data == root.data:
                return True
            elif data > root.data:
                return self.search(data, root.right)
            elif data < root.data:
                return self.search(data, root.left)
        
    def height(self, root):
        if root is None: return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def min(self, root):
        if root.left is None: 
            return root.data
        return self.min(root.left)
    
    def max(self, root):
        if root.right is None: 
            return root.data
        return self.max(root.right)
    
bst = BinarySearchTree()
bst.root = Node(8)
bst.insert_(4, bst.root)
bst.insert_(15, bst.root)
bst.insert_(1, bst.root)
bst.insert_(6, bst.root)
bst.insert_(13, bst.root)
bst.insert_(18, bst.root)
bst.insert_(14, bst.root)
print(bst.search(14, bst.root))
print(bst.search(0, bst.root))
bst.post_order(bst.root)
print(bst.height(bst.root))
print(bst.min(bst.root))
print(bst.max(bst.root))