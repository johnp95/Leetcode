from collections import deque


class Graph:
    def __init__(self, num_nodes,edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return '\n'.join([f'{n}: {neighbors}' for n,neighbors in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()
def bfs(graph,root):
    # queue = []
    queue = deque()
    # visited = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None]* len(graph.data)
    # visited[root] = True
    visited = [root]
    queue.append(root)
    distance[root] = 0
    ans = []
    while queue:
        current = queue.popleft()
        ans += [current]
        for node in graph.data[current]:
            if node not in visited:
                distance[node] = 1 + distance[current]
                parent[node] = current
                # visited[node] = True
                visited.append(node)
                queue.append(node)
            
    return ans,distance,parent
def dfs(graph,root):
    visited = []
    stack = []

    visited.append(root)
    stack.append(root)
    ans = []
    while stack:
        current = stack.pop()
        ans += [current]
        for node in reversed( graph.data[current]):
            if node not in visited:
                visited.append(node)
                
                stack.append(node)
    return ans


num_nodes = 5
edges = [(0,1),(0,4),(1,2), (1,3), (1,4), (2,3), (3,4)]

graph1 = Graph(num_nodes,edges)
# print(graph1)
# print(bfs(graph1,3))
# print(dfs(graph1,3))
# Graph with weights



