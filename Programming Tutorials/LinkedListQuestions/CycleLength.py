class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def cycleLength(head):
    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return 0  # No cycle, length is 0

    # Calculate the length of the cycle
    current = slow
    cycle_length = 0
    while current:
        current = current.next
        cycle_length += 1
        if current == slow:
            break

    return cycle_length
def Print(head):
    curr = head
    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next
    print()
if __name__ =='__main__':
    head = ListNode(1)
    head.next = ListNode(2,ListNode(3,ListNode(4,ListNode(5,head))))
    print(cycleLength(head))