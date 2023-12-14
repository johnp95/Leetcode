class TreeNode:
    def __init__(self,val):
        self.left,self.right,self.val = None,None,val

def maxDepth(root):
    if not root : return 0
    return 1 + max( maxDepth(root.left),maxDepth(root.right))
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth(root))