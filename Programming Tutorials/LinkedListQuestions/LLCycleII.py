class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def detectCycle(head):
    slow = head
    fast = head
    meeting_point = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            meeting_point = slow
            break
    if not meeting_point:
        return None
    pointer1 = head
    pointer2 = meeting_point
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

def Print(head):
    curr = head
    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next
    print()
if __name__ =='__main__':
    lst = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    lst.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    res = detectCycle(lst)
    print(res.val)