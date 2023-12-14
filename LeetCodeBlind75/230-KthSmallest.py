from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val,self.left,self.right = val,None,None


def insert(root,val):

    if root is None:
        return TreeNode(val)
    
    else:
        if val < root.val:
            root.left = insert(root.left,val)
        else:
            root.right = insert(root.right,val)
    return root
def kthSmallest(root,k):
    def helper(root):
        if not root : return []    
        return helper(root.left) + [root.val] + helper(root.right)
    return helper(root)[k-1]
        
root = None
root = insert(root,3)
root = insert(root,1)
root = insert(root,4)
root = insert(root,2)
print(kthSmallest(root,1))
