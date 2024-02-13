def twoSum(numbers,target):

    l,r = 0, len(numbers)-1

    while l < r:
        if numbers[r] + numbers[l] == target:
            return [l+1,r+1]

        if numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] < target:
            l += 1
            
        
        
numbers = [2,7,11,15]

target = 9
print(twoSum(numbers,target))