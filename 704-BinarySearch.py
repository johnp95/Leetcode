def binary_search(nums,target):
    start = 0
    end = len(nums) -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
   
        if target > nums[mid]:
            start = mid +1
        else:
            end = mid - 1
    return -1



nums = [1,2,3,4,5]
target = 2

print(binary_search(nums,target))