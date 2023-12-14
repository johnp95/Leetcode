class ListNode:
    def __init__(self,val=0,next=None):
        self.next = next
        self.val = val

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def Print(head):
    curr = head
    while curr:
        print(curr.val, end = ' -> ')
        curr = curr.next
    print()
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    Print(head)
    res = middleNode(head)
    Print(res)