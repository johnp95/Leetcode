def rob(nums):
    def helper(nums):
        table = [0]*(len(nums))
        table[-2] = nums[-2]
        table[-1] =nums[-1]

        for i in range(len(table)-3,-1,-1):
            table[i] = max(nums[i],nums[i]+max(table[i+2:]))
        return max(table[0],table[1])
    return max(helper(nums[:len(nums)-1]),helper(nums[1:]))
if __name__ == '__main__':
    nums = [200,3,140,20,10]
    nums = [2,3,2]
    nums = [5,1,8,7,4,2,2,8]
    nums = [1,2,1,1]
    nums = [1,2,3]
    nums = [1,2,3,1]
    print(rob(nums))