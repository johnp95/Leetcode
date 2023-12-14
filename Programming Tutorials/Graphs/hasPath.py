from collections import deque
def hasPathBfs(graph,src,dst):
    q = deque([src])

    while q:
        curr = q.popleft()
        if curr == dst : return True
        for neighbors in graph[curr]:
            q += [neighbors]
    return False
def hasPathRecursive(graph,src,dst):
    if src == dst : return True
    for neighbor in graph[src]:
        if hasPathRecursive(graph,neighbor,dst):
            return True
    return False




if __name__ == '__main__':
    graph = {
        'f': ['g','i'],
        'g': ['h'],
        'h': [],
        'i': ['g','k'],
        'j': ['i'],
        'k': []
    }
    print(hasPathBfs(graph,'f','k'))
    # print(hasPathRecursive(graph,'g','h'))