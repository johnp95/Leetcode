class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


    def maxDepth(self,node):
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left),self.maxDepth(node.right))


if __name__ == '__main__':

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(root.maxDepth(root))