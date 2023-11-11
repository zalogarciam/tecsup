class TrieNode():
    def __init__(self, data) -> None:
        self.data = data
        self.children = {} # a, b, c ... z
        self.eow = False # End Of Word

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("ROOT")

    # Time Complexity: O(x) --> x = length of word
    def insert(self, word):
        current = self.root
        for char in word: # home, read
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.eow = True

    def pre_order(self):
        self.pre_order_(self.root)

    # ROOT, CHILDREN
    def pre_order_(self, node):
        print(node.data)
        # CHILDREN
        for char in node.children.values():
            self.pre_order_(char)

    # CHILDREN, ROOT
    def post_order(self):
        self.post_order_(self.root)

    def post_order_(self, node):
        # CHILDREN
        for char in node.children.values():
            self.post_order_(char)
        print(node.data)

    def print(self):
        self.print_(self.root, "")

    def print_(self, node, prefix):
        if node.eow:
            print(prefix + "|--", node.data, '(eow)')
        else:
            print(prefix + "|--", node.data)
        prefix = prefix + "|   "
        for char in node.children.values():
            self.print_(char, prefix)
    
        
trie = Trie()
trie.insert("rebuild")
trie.insert("recover")
trie.insert("rest")
trie.insert("revisit")
trie.insert("car")
trie.insert("home")
trie.insert("read")
trie.print()