from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def levelOrder(root):
    if not root: return []
    q = deque([root])

    ans = []
    while q:
        subList = []
        for _ in range(len(q)):
            curr = q.popleft()
            subList += [curr.val]
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
        ans += [subList]
    return ans


        


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))