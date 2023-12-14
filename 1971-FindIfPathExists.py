from collections import defaultdict

def validPath(edges,source,destination):
    def createGraph(edges):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u] += [v]
            graph[v] += [u]
        return graph
    graph = createGraph(edges)
    visited = set([source])
    stack = [source]
    while stack:
        curr = stack.pop()
        if curr == destination : return True
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False
if __name__ == '__main__':
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    # print(createGraph(edges))
    print(validPath(edges,0,5))