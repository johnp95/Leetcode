class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def populateSorted(nums):
    def helper(nums,start,end):
        if start <= end:
            mid = (start+end)//2
            root = Node(nums[mid])
            root.left = helper(nums,start,mid-1)
            root.right = helper(nums,mid+1,end)
            return root
    return helper(nums,0,len(nums)-1)

def bstPrint(root):
    if not root : return []
    return  [root.val] + bstPrint(root.left) + bstPrint(root.right)
if __name__ == '__main__':
    nums = [0,1,2,3,4,5]
    res = populateSorted(nums)
    print(bstPrint(res))
 