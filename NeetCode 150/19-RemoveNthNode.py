class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head,n):

        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
def printLL(head):
    curr =head
    while curr:
        print(curr.val,end=' => ')
        curr = curr.next
    print()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

res = Solution().removeNthFromEnd(head,2)
printLL(res)