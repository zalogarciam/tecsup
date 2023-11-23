class Path:
    def __init__(self) -> None:
        self.list = []

class Node:
    def __init__(self, label) -> None:
        self.label = label

    def __str__(self):
        return f"{self.label}"

class Edge:
    def __init__(self, source, destination, weight) -> None:
        self.source = Node(source)
        self.destination = Node(destination)
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.source} ==> {self.destination} ({self.weight})"

class WeighthedGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

    def add_node(self, label):
        self.nodes[label] = Node(label)
        self.edges[label] = []

    def add_edge(self, source, destination, weight):
        self.edges[source].append(Edge(source, destination, weight))
        self.edges[destination].append(Edge(destination, source , weight))

    def dijkstra(self, source, destination):
        distances = {}

        for node in self.nodes:
            distances[node] = float('inf')
        distances[source] = 0

        previous_nodes = {}
        visited = []
        queue = [(0, source)]

        while(len(queue) > 0):
            queue.sort()
            current = queue.pop(0)[1]
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
        print(previous_nodes)
        stack = [self.nodes[destination].label]
        previous = previous_nodes[destination]
        while previous is not None:
            stack.append(previous)
            if previous not in previous_nodes:
                break
            previous = previous_nodes[previous]

        path = Path()
        while (len(stack) >0):
            path.list.append(stack.pop())
        return path.list
    
graph = WeighthedGraph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'C', 5)
graph.add_edge('A', 'B', 40)
graph.add_edge('A', 'D', 20)
graph.add_edge('D', 'E', 100)
graph.add_edge('B', 'E', 50)
graph.add_edge('C', 'D', 30)
graph.add_edge('B', 'D', 10)
# for edge in graph.edges:
    # print(graph.edges[edge])
print(graph.dijkstra('A', 'E'))
