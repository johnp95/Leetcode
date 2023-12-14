class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
        
    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end = ' -> ')
            curr = curr.next
        print("None")
    def contains(self,target):
        curr = self.head
        while curr:
            if target == curr.val:
                return True
            curr = curr.next
        return False

lst = LinkedList()
lst.append('a')
lst.append('b')
lst.append('c')
lst.append('d')
lst.print()
# print(lst.head.next.val)
# print(lst.contains('a'))