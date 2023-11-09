class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.children = {}
        self.eow = False # Fin de palabra

    def remove_child(self, char):
        self.children.pop(char)

class Trie():
    def __init__(self) -> None:
        self.root = Node("ROOT")
        self.count = 0

    def insert(self, string):
        current = self.root
        for char in string:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.eow = True
        self.count += 1

    def traverse(self):
        self.traverse_(self.root)

    #post order
    def traverse_(self, node):
        for item in node.children.values():
            self.traverse_(item)
        print(node.data)

    def pprint(self):
        self.pprint_(self.root, "")

    def pprint_(self, node, prefix):
        if node is None: return
        if node.eow:
            print(prefix + "|--", node.data, '(eow)')
        else:
            print(prefix + "|--", node.data)
        prefix = prefix + "|    "
        for child in node.children:
            self.pprint_(node.children[child], prefix)

    # def traverse_(self, node):
    #     print(node.data)
    #     for item in node.children.values():
    #         self.traverse_(item)

    def search(self, word):
        current = self.root
        if word is None: return False
        for char in word:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        return current.eow

    def remove(self, word):
        if word is None: return
        self.remove_(self.root, word, 0)

    def remove_(self, node, word, index):
        if index == len(word):
            node.eow = False
            return
        char = word[index] # c , a , r , e ...
        child = node.children.get(char, None)
        self.remove_(child, word, index + 1)
        if len(child.children) == 0 and not child.eow:
            node.children.pop(char)

    def count_trie(self):
        return self.count

    def count_words(self):
        return self.count_words_(self.root)

    def count_words_(self, node):
        count = 0 
        if node.eow: count +=1
        for item in node.children.values():
            count += self.count_words_(item)
        return count

trie = Trie()
trie.insert('cat')
trie.insert('car')
trie.insert('care')
trie.insert('careful')
trie.remove('careful')
print(trie.count_words())
trie.pprint()