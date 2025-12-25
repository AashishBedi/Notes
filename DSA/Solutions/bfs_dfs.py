from collections import deque
def bfs(self, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in self.adj.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()

def dfs(self, start):
    visited = set()
    print("DFS Traversal:", end=" ")
    self._dfs_util(start, visited)
    print()

def _dfs_util(self, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in self.adj.get(node, []):
        if neighbour not in visited:
            self._dfs_util(neighbour, visited)
