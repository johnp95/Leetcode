def twoSum(target,nums):
    hm = {}
    for i,num in enumerate(nums):
        if target - num in hm:
            return [hm[target-num],i]
        hm[num] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    result = twoSum(target,nums)
    print(result)