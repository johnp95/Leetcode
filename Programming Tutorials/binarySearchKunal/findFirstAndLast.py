#mine
def searchRange(nums,target):
    def binarySearch(nums,target,last=False):
        start, end = 0,len(nums)-1
        n = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if last:
                if mid+1 <= n-1 and nums[mid] == target and nums[mid] != nums[mid+1]:
                    return mid
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:

                if mid-1 >= 0 and target==nums[mid] and nums[mid]!= nums[mid-1]:
                    return mid
                if target <= nums[mid] and mid-1 >= 0:
                    end = mid - 1
                else:
                    start = mid + 1

        return end 
    first = binarySearch(nums,target)
    last = binarySearch(nums,target,last=True)

    return [first] + [last] if target in nums else [-1,-1]
#Kunal
def searchRange(nums,target):
    def binarySearch(nums,target,findStartIndex=False):
        start, end = 0,len(nums)-1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if findStartIndex:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans 
    start = binarySearch(nums,target,findStartIndex=True)
    end = binarySearch(nums,target)
    return [start] + [end]

if __name__ == '__main__':
    # print(searchRange([5,7,7,8,8,10],8))
    # print(searchRange([5,7,7,8,8,10],6))
    # print(searchRange([1],1))
    # print(searchRange([2,2],2))
    print(searchRange([1,2,3,4,5,3,1],3))