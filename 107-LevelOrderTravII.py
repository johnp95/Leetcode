from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def leverOrderBooom(root):
    q = deque([root])
    ans = []
    while q:
        currentLevel = []
        size = len(q)
        for _ in range(size):
            curr = q.popleft()
            currentLevel += [curr.val]
            if curr.left : q += [curr.left]
            if curr.right : q += [curr.right]
        ans += [currentLevel]
    return ans[::-1]
if __name__ == '__main__':
    root = Node(3,Node(9),Node(20,Node(15),Node(7)))
    # root = Node(1,Node(2,Node(4)),Node(3,None,Node(5)))
    print(leverOrderBooom(root))
