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
        node = self.nodes[label]
        for key in self.adjacency_list:
            if node in self.adjacency_list[key]:
                self.adjacency_list.remove(node)
        del self.adjacency_list[label]
        del self.nodes[label]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(self.nodes[destination])

    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(self.nodes[destination])

    def pprint(self):
        for node in self.adjacency_list:
            print(node, end="-->")
            for conn in self.adjacency_list[node]:
                print(conn.label, end=",")
            print()

    def bfs(self, node):
        queue = [node]
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

    def dfs(self, node):
        stack = [node]
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
graph.add_node('H')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('C', 'E')
graph.add_edge('D', 'B')
graph.add_edge('E', 'G')
graph.add_edge('E', 'H')
graph.add_edge('E', 'D')
graph.add_edge('D', 'G')
graph.add_edge('H', 'F')
graph.add_edge('H', 'G')
# graph.pprint()
print(graph.dfs('A'))
print(graph.bfs('A'))