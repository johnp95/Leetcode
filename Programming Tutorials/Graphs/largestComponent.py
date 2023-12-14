#Mine
def largestComponentIterative(graph):
    longest = 0
    for node in graph:
        visited = set()
        stack = [node]
        count = 0
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    count += 1
                    stack.append(neighbor)
        longest = max(count,longest)
    return longest
def largestComponent(graph):
    visited = set()
    longest = 0
    # for node in graph:
    #     size = exploreSize(graph,node,visited)
    #     if size > longest:
    #         longest = size
    print(exploreSize(graph,0,visited))
    # return longest
def exploreSize(graph,node,visited):
    if node in visited : return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph,neighbor,visited)
    return size
    
if __name__ == '__main__':
    graph = {
        0: [8,1,5],
        1: [0],
        5: [0,8],
        8: [0,5],
        2: [3,4],
        3: [2,4],
        4: [3,2]
    }
    print(largestComponent(graph))