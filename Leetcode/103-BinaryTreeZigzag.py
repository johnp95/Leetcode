from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def zigzag(root):
    if not root : return []
    q = deque([root])
    ans = []
    level = 0
    while q:
        currentLevel = []
        for _ in range(len(q)):
            curr = q.popleft()
            currentLevel += [curr.val]
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        if level % 2:
            ans += [currentLevel[::-1]]
        else:
            ans += [currentLevel]
        
        level += 1
    return ans
    

if __name__ == '__main__':
    root = Node(1,Node(2,Node(4)),Node(3,None,Node(5)))

    print(zigzag(root))