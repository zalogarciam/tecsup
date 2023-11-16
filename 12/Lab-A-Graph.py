class Node:
    def __init__(self, label) -> None:
        self.label = label

class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        self.nodes[label] = Node(label)
        self.adjacency_list[label] = []

    def remove_node(self, label):
        if label is not self.nodes: return
        node = self.nodes[label]

        # Delete nodes that are attached
        for key in self.adjacency_list[node]:
            self.adjacency_list[key].remove(node)
        
        del self.adjacency_list[label]
        del self.nodes[label]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(self.nodes[destination])

    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(self.nodes[destination])

    def print(self):
        print('Nodes')
        for node in self.nodes:
            print(node)
        print('Connections')
        for item in self.adjacency_list:
            print(item, '==>', end="")
            for edge in self.adjacency_list[item]:
                print(edge.label, end=", ")
            print()

    def bfs(self, label):
        queue = [label]
        visited = []
        while len(queue) > 0:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.append(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor.label not in visited:
                    queue.append(neighbor.label)
        return visited

    def dfs(self, label):
        stack = [label]
        visited = []
        while len(stack) > 0:
            current = stack.pop()
            if current in visited:
                continue
            visited.append(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor.label not in visited:
                    stack.append(neighbor.label)
        return visited

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')

graph.add_edge('A', 'B')
graph.add_edge('B', 'A')
graph.add_edge('A', 'C')
graph.add_edge('C', 'A')
graph.add_edge('A', 'D')
graph.add_edge('D', 'A')
graph.add_edge('A', 'E')
graph.add_edge('E', 'A')
graph.add_edge('D', 'E')
graph.add_edge('E', 'D')
graph.add_edge('D', 'F')
graph.add_edge('F', 'D')
graph.add_edge('G', 'F')
graph.add_edge('F', 'G')

print(graph.bfs('A'))
print(graph.dfs('A'))