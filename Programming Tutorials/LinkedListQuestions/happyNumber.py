class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def isHappy(n):
    def getNextNum(n):
        res = 0
        while n > 0:
            x = n%10
            res +=  x**2 
            n //= 10
        return res
    
    fast = n
    slow = n
    
    while True:
        slow = getNextNum(slow)
        fast = getNextNum(getNextNum(fast))
        if fast == 1: return True
        if fast == slow : return False




if __name__ == '__main__':
    print(isHappy(19))
    