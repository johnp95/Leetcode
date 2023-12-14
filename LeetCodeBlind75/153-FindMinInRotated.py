# implementation 1
def findMin(nums):
    lo,hi = 0, len(nums)-1
    while lo < hi:
        mid = (lo+hi)//2
        if nums[mid] < nums[mid-1] and mid-1 >= 0:
            return nums[mid] 
        
        if nums[mid] < nums[hi]:
            hi = mid 
        elif nums[mid] > nums[hi]:
            lo = mid + 1
    return nums[lo]

# implementation 2
def findMin2(nums):
    start,end = 0,len(nums)-1
    _min = float('inf')
    while start <= end:
        mid = (start+end)//2
        
        _min = min(_min,nums[mid])
        
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid  - 1
    return _min

if __name__ == '__main__':
    print(findMin([3,4,5,1,2]))
    print(findMin2([3,4,5,1,2]))