class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverseList(head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
def Print(head):
    while head:
        print(head.val,end= ' -> ')
        head = head.next

if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    res = reverseList(a)
    print(Print(res))