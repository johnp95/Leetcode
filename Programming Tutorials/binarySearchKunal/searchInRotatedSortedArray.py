def search(nums,target):
    n = len(nums)-1
    def pivot(nums,start,end):
        while start < end:
            mid = (start + end) // 2
            # if nums[mid] < nums[end] then pivot must be on the left side
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return start
    def binarySearch(nums,start,end,target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid]==target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1                
    # Find the Pivot. aka the index of the min(arr)
    p = pivot(nums,0,n)
    # Check if target is in left sorted list
    left = binarySearch(nums,0,p-1,target)
    # Check if target is in right sorted list
    right = binarySearch(nums,p,n,target)
    return max(left,right)

if __name__ == '__main__':
    nums,target = [4,5,6,7,0,1,2], 7
    # nums,target = [8,1,2,3,4], 8
    # nums,target = [8,10,11,12,13,14,7], 8
    # nums,target = [1], 0
    

    print(search(nums,target))
    