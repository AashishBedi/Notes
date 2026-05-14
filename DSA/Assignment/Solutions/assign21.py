class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        # Adjacency list:
        # key   -> vertex
        # value -> list of (adjacent_vertex, weight)
        self.adj_list = {i: [] for i in range(vertex_count)}
    
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
    
    def remove_edge(self, u, v):
        #Remove edge u -> v
        self.adj_list[u] = [(node, w) for node, w in self.adj_list[u] if node != v]
        #Remove edge v -> u
        self.adj_list[v] = [(node, w) for node, w in self.adj_list[v] if node != u]
    
    def has_edge(self, u, v):
        # Check if v exists in u's adjacency list
        for node, _ in self.adj_list[u]:
            if node == v:
                return True
        return False
    
    def print_adj_list(self):
        print("Adjacency list: ")
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 7)
    g.add_edge(2, 4, 3)

    g.print_adj_list()

    print("Edge between 0 and 1:", g.has_edge(0, 1))
    print("Edge between 1 and 4:", g.has_edge(1, 4))

    g.remove_edge(0, 1)
    g.print_adj_list()