class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:

        slow,fast = head, head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast : return True
        return False
        
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

print(Solution().hasCycle(l))