from collections import deque
def depthFirstPrint(graph,source):
    stack = [source] 
    ans = []
    while stack:
        curr = stack.pop() 
        ans += [curr]
        for neighbor in graph[curr][::-1]:
            stack.append(neighbor)
    print(ans)
def depthFirstRecursivePrint(graph,source):
    print(source)
    for neighbor in graph[source][::-1]:
        depthFirstRecursivePrint(graph,neighbor)  

def breadthFirstPrint(graph,source):
    q = deque([source])
    ans = []
    while q:
        curr = q.popleft()
        ans += [curr]
        for neighbor in graph[curr]:
            q.append(neighbor)
    print(ans)



if __name__ == '__main__':
    graph = {
        'a': ['b','c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    # depthFirstPrint(graph,'a')
    # depthFirstRecursivePrint(graph,'a')
    breadthFirstPrint(graph,'a')