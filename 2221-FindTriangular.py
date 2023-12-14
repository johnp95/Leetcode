def triangularSum(nums):
    
    for _ in range(1,len(nums)):
        print('hey')
        # newNums = [0] * (len(nums)-1)
        # newNums = [(nums[i-1]+nums[i])%10 for i in range(1,len(nums))]
        # nums = newNums

    # return sum(nums)    
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    nums = [5]
    # a = [0]* len(nums)-1
    # a = [0] * (len(nums)-1)
    # print(a)
    print(triangularSum(nums))