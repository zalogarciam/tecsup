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
    
    def search(self, root, data):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data > root.data:
            return self.search(root.right, data)
        elif data < root.data:
            return self.search(root.left, data)

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

    def height(self, root):
        if root is None: return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def min(self, root):
        if root.left is None: return root.data
        return self.min(root.left)
    
    def max(self, root):
        if root.right is None: return root.data
        return self.max(root.right)

    # def get_ancestors(self, root, target):
    #     if root is None:
    #         return False
    #     if root.data == target:
    #         return True
        
    #     left = self.get_ancestors(root.left, target)
    #     right = self.get_ancestors(root.right, target)
    #     if left or right:
    #         print(root.data)
    #         return True
    #     return False


bst = BinarySearchTree()
bst.root = Node(10)
bst.insert_(bst.root, 5)
bst.insert_(bst.root, 13)
bst.insert_(bst.root, 2)
bst.insert_(bst.root, 9)
bst.insert_(bst.root, 11)
bst.insert_(bst.root, 16)
bst.insert_(bst.root, 12)
# print(bst.search(bst.root, 12))
# print(bst.search(bst.root, 0))
# print(bst.height(bst.root))
# print(bst.min(bst.root))
# print(bst.max(bst.root))
# bst.in_order(bst.root)
# bst.get_ancestors(bst.root, 2)

def swap(word, index):
    if index == len(word): return
    print(word[index])
    swap(word, index + 1)

swap("ABCD", 0)


