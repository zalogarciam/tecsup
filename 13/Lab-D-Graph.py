import heapq


class Node:
    def __init__(self, label) -> None:
        self.label = label
    def __str__(self) -> str:
        return f"{self.label}"

class Edge:
    def __init__(self, source, destination, weight) -> None:
        self.source = Node(source)
        self.destination = Node(destination)
        self.weight = weight

class WeightedGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

    def add_node(self, label):
        self.nodes[label] = Node(label)
        self.edges[label] = []
 
    def add_edge(self, source, destination, weight):
        self.edges[source].append(Edge(source, destination, weight))
        self.edges[destination].append(Edge(destination, source, weight))

    def dijkstra(self, source, destination):
        distances = {}

        for node in self.nodes:
            distances[node] = float('inf')
        distances[source] = 0

        previous_nodes = {}
        visited = []
        queue = [(0, source)]

        while len(queue) > 0:
            current = heapq.heappop(queue)[1]
            visited.append(current)

            for edge in self.edges[current]: 
                if edge.destination.label in visited:
                    continue 
                new_distance = distances[current] + edge.weight
                if new_distance < distances[edge.destination.label]:
                    distances[edge.destination.label] = new_distance
                    previous_nodes[edge.destination.label] = current
                    queue.append((new_distance, edge.destination.label))
            
        return self.build_path(destination, previous_nodes)
    
    def build_path(self, destination, previous_nodes):
        stack = [self.nodes[destination].label]
        previous = previous_nodes[destination]
        while previous is not None:
            stack.append(previous)
            if previous not in previous_nodes: break
            previous = previous_nodes[previous]

        path = []
        while len(stack) > 0:
            path.append(stack.pop())
        print(path)

graph = WeightedGraph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'C', 5)
graph.add_edge('A', 'B', 40)
graph.add_edge('A', 'D', 20)
graph.add_edge('B', 'D', 10)
graph.add_edge('B', 'E', 50)
graph.add_edge('C', 'D', 30)
graph.add_edge('D', 'E', 100)

graph.dijkstra('A', 'E')

