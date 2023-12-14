class Node:
    def __init__(self,val=0,next=None):
        self.val = val 
        self.next= next

def lstPrint(head):
    while head:
        print(head.val,end= ' -> ')
        head = head.next
    print()

def cycle(head):
    fast = head.next
    slow = head

    while fast and fast.next:
        if fast.val == slow.val : return True

        slow = slow.next
        fast = fast.next.next
    return False

if __name__ == '__main__':

    lst1 = Node(3, Node(2, Node(0,Node(4,Node(2)))) )

    lstPrint(lst1)
    res = cycle(lst1)
    print(res)