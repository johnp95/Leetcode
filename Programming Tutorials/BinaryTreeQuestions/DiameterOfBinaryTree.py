from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None        
def find_diameter(root):

    def helper(node):
        if not node:
            return 0  # Height of an empty tree is 0
        
        # Calculate the height of the left and right subtrees
        left_height = helper(node.left)
        right_height = helper(node.right)
        
        # Update the diameter (if needed)
        # The diameter could be the path that doesn't pass through the root, or it could be in the left or right subtree.
        # So, we take the maximum of the following three values:
        # 1. Diameter in the left subtree.
        # 2. Diameter in the right subtree.
        # 3. Length of the path that passes through the current root (left_height + right_height).
        nonlocal diameter
        diameter = max(diameter, left_height + right_height)
        
        # Return the height of the current node's subtree (including the current node).
        return 1 + max(left_height, right_height)
    diameter = 0  # Initialize diameter to 0
    
    helper(root)
    return diameter



if __name__ == '__main__':
    root  = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node (5)

    print(find_diameter(root))