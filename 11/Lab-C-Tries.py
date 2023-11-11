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
    
    # Time Complexity: O(L)
    def search(self, word):
        # "" or None --> False
        if not word:
            return False
        
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.eow
    
    def delete(self, word):
        if word is None: return
        self.delete_(self.root, word, 0)

    def delete_(self, node, word, index):
        if index == len(word):
            node.eow = False
            return
        char = word[index]
        child = node.children.get(char, None)
        self.delete_(child, word, index + 1)
        if len(child.children) == 0 and not child.eow:
            node.children.pop(char)

    def count_words(self):
        return self.count_words_(self.root)
    
    def count_words_(self, node):
        count = 0
        if node.eow: count = count + 1
        for item in node.children.values():
            count += self.count_words_(item)
        return count

trie = Trie()
trie.insert("rebuild")
trie.insert("recover")
trie.insert("rest")
trie.insert("revisit")
trie.insert("car")
trie.insert("home")
trie.delete("revisit")
trie.print()
print(trie.count_words())
# print(trie.search("rest"))
# print(trie.search("res"))