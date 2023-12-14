def connectedComponentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph,node,visited):
            count += 1
    return count
def explore(graph,curr,visited):
    if curr in visited : return False
    visited.add(curr)
    for neighbor in graph[curr]:
        explore(graph,neighbor,visited)
    return True
if __name__ == '__main__':
    graph = {
        3: [],
        4: [6],
        6: [4,5,7,8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }
    print(connectedComponentsCount(graph))
    