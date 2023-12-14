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
            self._append(val,self.head)
    def _append(self,val,curr):
        if not curr.next:
            curr.next = Node(val)
        else:
            self._append(val,curr.next)
    def print(self):
        output = self._print(self.head)
        print(output)
    def _print(self,curr):
        # if not curr: 
        #     return ''
        # return curr.val + ' -> ' + self._print(curr.next)
        if curr:
            print(curr.val, end=' -> ')
            self._print(curr.next)
       
    def contains(self,target):
        return self._contains(target,self.head)
    def _contains(self,target,curr):
        if not curr:
            return False
        if curr.val == target : return True
        return self._contains(target,curr.next)
   

def sumListIterative(head):
    curr = head
    _sum = 0
    while curr:
        _sum += curr.val
        curr = curr.next
    return _sum
def sumListRecursive(head):
    if not head: return 0
    return head.val + sumListRecursive(head.next)

if __name__ == '__main__':
    lst = LinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.append('d')
    lst.delete('c')
    lst.print()

