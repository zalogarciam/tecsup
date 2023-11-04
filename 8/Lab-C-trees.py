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

    def delete(self, root, value):
        # No root
        if not root:
            return root
        
        if root.data > value:
            root.left = self.delete(root.left, value)
        elif root.data < value:
            root.right = self.delete(root.right, value)
        else: # Element found
            # Leaf Node
            if root.left is None and root.right is None:
                return None
            # One child
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            
            # Two children
            min_value = self.min(root.right)
            root.data = min_value
            root.right = self.delete(root.right, min_value)
        return root
    
    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
    
    def in_order_level(self, root, level= 0):
        if root != None:
            self.in_order_level(root.left, level + 1)
            print((level * 4 * "-") + str(root.data))
            self.in_order_level(root.right, level + 1)

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

    def get_nodes_at_distance(self, root, k):
        list = []
        self.print_nodes(root, k , list)
        return list
    
    def print_nodes(self, root, k , list):
        if root is None: return
        if k == 0:
            list.append(root.data)
            return
        self.print_nodes(root.left, k-1, list)
        self.print_nodes(root.right, k-1, list)

    def get_nodes(self, root, list):
        if root is None: return
        if root.left is None and root.right is None:
            list.append(root.data)
        self.get_nodes(root.left, list)
        self.get_nodes(root.right, list)

    def sum_nodes(self, root):
        # Case Base
        if root is None: return 0

        # Leaf Node
        if root.left is None and root.right is None:
            return 1
        
        # Recursive calls
        return self.sum_nodes(root.left) + self.sum_nodes(root.right)

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
# bst.delete(bst.root, 11)
bst.in_order_level(bst.root)
print(bst.sum_nodes(bst.root))
# list = []
# bst.get_nodes(bst.root, list)
# print(list)
# print(bst.get_nodes_at_distance(bst.root, 2))
# print(bst.search(bst.root, 12))
# print(bst.search(bst.root, 0))
# print(bst.height(bst.root))
# print(bst.min(bst.root))
# print(bst.max(bst.root))
# bst.in_order(bst.root)
# bst.get_ancestors(bst.root, 2)

# def swap(word, index):
#     if index == len(word): return
#     print(word[index])
#     swap(word, index + 1)

# swap("ABCD", 0)


