class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p,q):

        if not p and not q : return True
        if not p or not q : return False
        if p.val != q.val : return False

        left = self.isSameTree(p.left,q.left)
        right =self.isSameTree(p.right,q.right)
        return left and right

p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(Solution().isSameTree(p,q))