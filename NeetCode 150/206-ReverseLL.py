class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):

        prev = None

        curr = head

        while curr:

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def printLL(self,head):

        curr = head    
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print()
ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

res = Solution().reverseList(ll)
Solution().printLL(res)