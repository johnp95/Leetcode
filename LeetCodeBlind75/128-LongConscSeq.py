# O(n * log(n)) solution, sort takes O(n log n) + O(n) = O(n log n)
def longestConsecutive(nums):
    nums.sort()
    start = 0
    long = float('-inf')
    for end in range(1,len(nums)):
        curr = nums[end]
        if curr == nums[end-1]:
            start += 1
        elif curr - nums[end-1] != 1:
            start = end
        
        long = max(long,end - start + 1)
    return len(nums) if len(nums) <= 1 else long
if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    nums = [1,2,0,1]
    nums = [1,2,2,2,2,3]
    # nums = [1]
    # nums = [5]
    print(longestConsecutive(nums))