from collections import deque
from collections import defaultdict
def createGraph(edges):
    graph = defaultdict(list) 
    for u,v in edges:
        graph[u] += [v]
        graph[v] += [u]
    for key,value in graph.items():
        print(f'{key }: {value}')
    return graph
def shortestPath(edges,src,dst):
    graph = createGraph(edges)
    visited = set([src])
    q = deque([[src,0]])
    while q:
        curr,distance = q.popleft()
        if curr == dst : return distance
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append([neighbor,distance+1])
    return -1
if __name__ == '__main__':
    edges = [
        ['w','x'],
        ['x','y'],
        ['z','y'],
        ['z','v'],
        ['w','v']
    ]
    print(shortestPath(edges,'w','z'))