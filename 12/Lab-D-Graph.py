class Node:
    def __init__(self, label) -> None:
        self.label = label

class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)
            self.adjacency_list[label] = []

    def remove_node(self, label):
        node = self.nodes[label]
        for key in self.adjacency_list:
            if node in self.adjacency_list[key]:
                self.adjacency_list[key].remove(node)
        del self.adjacency_list[label]
        del self.nodes[label]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(self.nodes[destination])
    
    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(self.nodes[destination])

    def pprint(self):
        for node in self.adjacency_list:
            print(node, end="==>")
            for conn in self.adjacency_list[node]:
                print(conn.label, end=', ')
            print()

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
graph.add_node('H')
graph.add_edge('A', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'B')
graph.add_edge('B', 'F')
graph.add_edge('F', 'E')
graph.add_edge('F', 'G')
graph.add_edge('F', 'H')
graph.add_edge('H', 'B')
graph.add_edge('G', 'E')
graph.add_edge('G', 'H')
graph.add_edge('E', 'A')
graph.pprint()