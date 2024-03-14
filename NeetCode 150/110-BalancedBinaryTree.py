class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):

        res = True
        def dfs(root):
            nonlocal res
            if not root : return 0
            left,right = dfs(root.left),dfs(root.right)
            if abs(left - right) > 1:
                res = False
            return 1 + max(left,right)
        dfs(root)
        return res
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(Solution().isBalanced(root))