def twoSum(nums,target):
    hashmap = {}

    for i,n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[n] = i

print(twoSum([2,7,11,15],9))
    