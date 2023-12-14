from collections import deque
class Node:
    def __init__(self,val,left=None,right=None,next=None):
        self.val = val
        self.left = left
        self.right = right        
        self.next = next
def rightSideView(root):
    q = deque([root])
    ans = []
    while q:
        levelSize = len(q)
        for i in range(levelSize):
            curr = q.popleft()
            if i == levelSize-1:
                ans += [curr.val]
            if curr.left : 
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
       

    return ans

if __name__ == '__main__':
    root = Node(1,Node(2,None,Node(5)),Node(3,None,Node(4)))
    print(rightSideView(root))