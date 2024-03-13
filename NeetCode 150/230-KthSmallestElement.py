class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root,k):

        def helper(root):
            if not root : return []

            return helper(root.left) + [root.val]  + helper(root.right)
        res  = helper(root)
        return res[k-1]
        
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(Solution().kthSmallest(root,1))
