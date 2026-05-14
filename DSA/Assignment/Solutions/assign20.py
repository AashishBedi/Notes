class Graph:
    def __init__(self, vertex_cnt):
        self.vertex_cnt = vertex_cnt
        self.adj_mat = [[0]*vertex_cnt for _ in range(vertex_cnt)]
    
    def add_edge(self, u, v, weight = 1):
        if u < 0 or v < 0 or u >= self.vertex_cnt or v >= self.vertex_cnt:
            print("Invalid Vertex")
            return
        #Undirected Graph -> Symmetric entries
        self.adj_mat[u][v] = weight
        self.adj_mat[v][u] = weight
    
    def remove_edge(self, u, v):
        if u < 0 or v < 0 or u >= self.vertex_cnt or v >= self.vertex_cnt:
            print("Invalid Vertex")
            return
        
        self.adj_mat[u][v] = 0
        self.adj_mat[v][u] = 0
    
    def has_edge(self, u, v):
        if u < 0 or v < 0 or u >= self.vertex_cnt or v >= self.vertex_cnt:
            return False
        return self.adj_mat[u][v] != 0
    
    def print_adj_mat(self):
        print("Adjacency Matrix:")
        for row in self.adj_mat:
            for val in row:
                print(val, end = ' ')
            print()

g = Graph(4)

g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 2)

g.print_adj_mat()

print("Edge between 0 and 1:", g.has_edge(0, 1))
print("Edge between 2 and 3:", g.has_edge(2, 3))

g.remove_edge(0, 1)
g.print_adj_mat()
