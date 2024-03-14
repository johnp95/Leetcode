class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):

        if not root : return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
print(Solution().invertTree(root))