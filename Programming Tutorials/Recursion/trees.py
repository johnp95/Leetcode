from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def breadthFirstPrint(root):
    q = deque([root])
    while q:
        # for _ in range(len(q)):
        curr = q.popleft()
        print(curr.val)
        if curr.left : q.append(curr.left)
        if curr.right : q.append(curr.right)
def breadthFirstSearch(root,target):
    q = deque([root])
    inTree = False
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr.val == target:
                inTree = True
            
            # print(curr.val)
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
    return inTree
def sumTree(root):
    q = deque([root])
    _sum = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            _sum += curr.val
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
        
    return _sum
def depthFirstPrint(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr.val)
        if curr.right : stack.append(curr.right)
        if curr.left : stack.append(curr.left)
def depthFirstPrintRecursive(root):
    if not root: return 
    print(root.val)
    depthFirstPrintRecursive(root.left) 
    depthFirstPrintRecursive(root.right) # same as pre-order traversal
def preOrder(root):
    if not root: return 
    print(root.val)
    preOrder(root.left) 
    preOrder(root.right)
def inOrder(root):
    if not root: return 
    inOrder(root.left) 
    print(root.val)
    inOrder(root.right)
def postOrder(root):
    if not root: return 
    postOrder(root.left) 
    postOrder(root.right)
    print(root.val)
def sumTreeDFS(root):
    stack = [root]
    _sum = 0
    while stack:
        curr = stack.pop()
        _sum += curr.val
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return _sum
       
def sumTreeDFSRecursive(root):
    if not root: return 0

    return  sumTreeDFSRecursive(root.left) + root.val +sumTreeDFSRecursive(root.right)
       



 
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(4)
e = TreeNode(-2)
f = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# breadthFirstPrint(a)
# depthFirstPrint(a)
print(sumTreeDFSRecursive(a))