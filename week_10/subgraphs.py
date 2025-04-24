class Graph:
    def __init__(self, n):
        self.n = n
        self.graphEdges = [[] for _ in range(n)]

    def add(self, u, v):
        self.graphEdges[u].append(v)
        self.graphEdges[v].append(u)

    def remove(self, u, v):
        if v in self.graphEdges[u] and u in self.graphEdges[v]:
            self.graphEdges[u].remove(v)
            self.graphEdges[v].remove(u)

    def dfs(self, node, visited):
        visited.add(node)
        for vertex in self.graphEdges[node]:
            if vertex not in visited:
                self.dfs(vertex, visited)

    def subgraphs(self):
        visited = set()
        visitedCounter = 0
        for node in range(self.n):
            if node not in visited:
                self.dfs(node, visited)
                visitedCounter += 1
        return visitedCounter

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1
