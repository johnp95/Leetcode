def rob(nums):
    memo = {}
    def helper(idx):
        if len(nums)==1:return nums[-1]
        if len(nums)==2:return max(nums)
        if idx in memo: return memo[idx]
        
        if idx >= len(nums):
            return 0
        two = nums[idx] + helper(idx+2)
        three = nums[idx] +  helper(idx+3)
        memo[idx] = max(three,two)


        return memo[idx]


    return max(helper(0),helper(1))


if __name__ == '__main__':
    nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    nums = [200,3,140,20,10]
    result = rob(nums)
    print(result)