class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def invert(root):
    if not root : return None

    left = invert(root.left)
    right = invert(root.right)

    root.left = right
    root.right = left
    return root


root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

print(invert(root))