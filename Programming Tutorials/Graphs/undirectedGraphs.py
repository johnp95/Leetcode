from collections import defaultdict
def undirectedGraph(edges,nodeA,nodeB):
    graph = buildGraph(edges)
    for key,val in graph.items():
        print(f'{key}: {val}')
    # print(hasPath(graph,nodeA,nodeB))
    print(hasPathRecursive(graph,nodeA,nodeB))
def hasPath(graph,nodeA,nodeB):

    stack = [nodeA]
    visited = set()
    while stack:
        curr = stack.pop()
        visited.add(curr)
        if curr == nodeB : return True
        for neighbor in graph[curr][::-1]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False
def hasPathRecursive(graph,src,dst,visited = set()):
    if src == dst : return True
    visited.add(src)
    for neighbor in graph[src]:
        if neighbor not in visited:
            if hasPathRecursive(graph,neighbor,dst,visited):
                return True
    return False
def buildGraph(edges):
    graph = defaultdict(list)

    for edge in edges:
        a,b = edge
        # if a not in graph:
        #     graph[a] = []
        # if b not in graph:
        #     graph[b] = []
        graph[a] += [b]
        graph[b].append(a)
    return graph
if __name__ == '__main__':
    edges = [
        ['i','j'],
        ['k','i'],
        ['m','k'],
        ['k','l'],
        ['o','n'],
    ]
    graph = {
        'a': ['b','c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    # print(hasPath(graph,'a','z'))
    #54:32
    undirectedGraph(edges,'j','m')