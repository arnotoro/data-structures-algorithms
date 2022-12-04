class Graph:
    def __init__ (self, gMatrix):
        self.adjMatrix = gMatrix
        self.adjList = {vertex : list() for vertex in range(len(gMatrix))} # adjacency matrix to adjacency list using python dictionary

        # creating edges for the adjacency list
        for row in range(len(gMatrix)):
            for column in range(len(gMatrix)):
                if gMatrix[row][column] != 0:
                    self.adjList[row].append(column)


    def df_print(self, start):
        visited = list()

        self.df_printHelp(start, visited)
        print("\t")
            
    def df_printHelp(self, start, visited):
        if start not in visited:
            print(start, end=" ")
            visited.append(start)

            for vertex in self.adjList[start]:
                self.df_printHelp(vertex, visited)

    def bf_print(self, start):
        visited = list()
        queue = []

        self.bf_printHelp(start, visited, queue)

        print("\t")

    def bf_printHelp(self, start, visited, queue):
        visited.append(start)
        queue.append(start)

        while queue:
            XD = queue.pop(0)
            print(XD, end=" ")

            for vertex in self.adjList[XD]:
                if vertex not in visited:
                    visited.append(vertex)
                    queue.append(vertex)

    def weight(self, vertex1, vertex2):
        if self.adjMatrix[vertex1][vertex2] == 0:
            return -1
        else:
            return self.adjMatrix[vertex1][vertex2]


if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 1, 0, 0, 2, 0], # 0
        [1, 0, 0, 0, 0, 2], # 1
        [0, 0, 0, 0, 4, 0], # 2
        [0, 0, 0, 0, 4, 5], # 3
        [2, 0, 4, 4, 0, 1], # 4
        [0, 2, 0, 5, 1, 0]  # 5   
    ]
    graph = Graph(matrix)

    for i in range(0,5):
        graph.df_print(i)
    print()
    for j in range(0,5):
        graph.bf_print(j)

    # graph.df_print(0)           # 0 2 1 3 5 4 
    # graph.df_print(1)
    # graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1