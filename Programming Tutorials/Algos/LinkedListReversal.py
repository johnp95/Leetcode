class Node:
    def __init__(self,val):
        self.val,self.next = val,None


def reverse(head):
    prev = None
    curr = head
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseRecursive(curr,prev=None):
    
    if not curr: return prev
    next = curr.next
    curr.next = prev
    return reverseRecursive(next,curr)
def lPrint(head):
    if not head : return
    print(head.val, end= ' -> ')
    lPrint(head.next)

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    a.next = b
    b.next = c
    c.next = d
    lPrint(a)
    print()
    newHead = reverseRecursive(a)
    lPrint(newHead)