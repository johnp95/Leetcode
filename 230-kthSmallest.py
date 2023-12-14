from collections import deque
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def kthSmallest(root,k):
    def helper(root):
        if not root:
            return []
        x =  helper(root.left) + [root.val] + helper(root.right)

        return x
    x =  helper(root)
    return x[k-1]
    

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)
print(kthSmallest(root,1))