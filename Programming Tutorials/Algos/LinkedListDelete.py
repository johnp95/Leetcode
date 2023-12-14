class Node:
    def __init__(self,val):
        self.val, self.next = val, None

def deleteValue(head,target):
    if head.val == target:
        return head.next
    prev = None
    curr = head
    while curr:
        if curr.val == target:
            prev.next = curr.next
        prev = curr
        curr = curr.next
    return head
def deleteValueRecursive(head,target):
    if head.val == target:
        return head.next
    _deleteValueRecursive(head,None,target)
    return head
def _deleteValueRecursive(curr,prev,target):
    if not curr : return

    if curr.val == target:
        prev.next = curr.next
        return
    _deleteValueRecursive(curr.next,curr,target) # curr = curr.next, prev = curr
    


def Print(head):
    if not head : return 
    print(head.val, end= ' -> ')
    Print(head.next)
if __name__ == '__main__':
    a = Node(4)
    b = Node(3)
    c = Node(2)
    d = Node(1)
    a.next = b
    b.next = c
    c.next = d
    Print(a)
    print()
    newHead = deleteValueRecursive(a,3)
    Print(newHead)
