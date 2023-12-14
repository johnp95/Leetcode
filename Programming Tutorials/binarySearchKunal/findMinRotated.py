def findMin(nums):
    
    start,end = 0, len(nums)-1
    while start < end:
        mid = (start + end) // 2

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid 
    return start
            

if __name__ == '__main__':
    nums = [3,4,5,1,2] # ans = 1
    nums = [4,5,6,7,0,1,2] # ans = 0
    nums = [11,13,15,17] # ans = 11
    nums = [15,18,2,3,6,12] # ans = 11
    print(findMin(nums))