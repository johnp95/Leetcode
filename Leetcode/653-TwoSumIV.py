from collections import deque
class TreeNode:
    def __init__ (self,val):
        self.val = val 
        self.left = None
        self.right = None
def findTarget(root,k):
    q = deque([root])
    d = []
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr.val in d : return True

            d += [k - curr.val]
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
    return False

root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(7)

print(findTarget(root,9))
print(findTarget(root,28))