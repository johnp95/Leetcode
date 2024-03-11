class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first,second = head,prev

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
        return head
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
res = Solution().reorderList(head)
printLL(res)
