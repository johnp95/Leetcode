from collections import deque
class Node:
    def __init__(self,val,left=None,right=None,next=None):
        self.val = val
        self.left = left
        self.right = right        
        self.next = next
def connect(root):
    if not root : return None
    leftMost = root
    while leftMost.left:
        curr = leftMost
        print(curr.val)
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        leftMost = leftMost.left
    return root
def Print(root):
    curr = root.left
    while curr:
        print(curr.val,end=' -> ')
        curr = curr.next

if __name__ == '__main__':
    root = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))
    res = connect(root)
    Print(res)