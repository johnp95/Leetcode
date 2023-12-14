def search(nums,target):
    start,end = 0, len(nums)-1

    while start <= end:

        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[start]==nums[mid] and nums[mid] == nums[end]:
            start += 1
            end -= 1
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return  False


if __name__ == '__main__':
    nums,target = [2,5,6,0,1,2], 0
    # nums,target = [2,5,6,0,1,2], 4
    # nums,target = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2
    # nums,target = [2,2,2,3,2,2,2], 3
    # nums,target = [1,1,1,1,1,2,1], 3
    # nums,target = [4,5,6,7,0,0,1], 3

    print(search(nums,target))