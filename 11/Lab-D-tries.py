class TrieNode():
    def __init__(self, data) -> None:
        self.data = data
        self.children = {} # a b c d ... z
        self.eow = False

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode("ROOT")

    def insert(self, word): # interact
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.eow = True

    def pre_order(self):
        self.pre_order_(self.root)

    def pre_order_(self, node): # ROOT - CHILDREN
        print(node.data)
        for char in node.children.values():
            self.pre_order_(char)

    def post_order(self):
        self.post_order_(self.root)

    def post_order_(self, node): # CHILDREN - ROOT
        for char in node.children.values():
            self.post_order_(char)
        print(node.data)

    def print(self):
        self.print_(self.root, "")
    
    def print_(self, node, prefix):
        if node.eow:
            print(prefix + '|--', node.data, '(eow)')
        else:
            print(prefix + '|--', node.data)
        prefix = prefix + "|  "
        for char in node.children:
            self.print_(node.children[char], prefix)

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
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

    def remove(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if current.eow:
            current.eow = False
            for child in current.children.values():
                self.remove(child.data)
            return True
        if current.children:
            current.children = {}
            return True
        current.data = None
        return True
    
    def count_words(self):
    pass

trie = Trie()
trie.insert("INTERACT")
trie.insert("INTERNATIONAL")
trie.insert("INTERNET")
# print(trie.search("INTERACT"))
# print(trie.search("INTERN"))
trie.delete("INTERNATIONAL")
# trie.pre_order()
trie.print()
# trie.post_order()
