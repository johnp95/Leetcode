def findMin(nums):
    
    lo,hi = 0, len(nums)-1
    # if nums==sorted(nums):
    #     return nums[0]
    while lo < hi:
        mid = (lo+hi)//2
        # print(f'lo: {lo} hi: {hi} mid: {mid} nums[mid]: {nums[mid]}')
        if nums[mid] < nums[mid-1] and mid-1 >= 0:
            return nums[mid] 
        
        if nums[mid] < nums[hi]:
            hi = mid
        elif nums[mid] > nums[hi]:
            lo = mid + 1
    return nums[lo]

tests = []

tests.append({
    # original input  #0
    'input': {
    'nums': [3,4,5,1,2],
    },
    'output': 1
})
tests.append({
    # size 10 rotated 3 time #1
    'input': {
    'nums': [4,5,6,7,0,1,2],
    },
    'output': 0
})
tests.append({
    # never rotated #2
    'input': {
    'nums': [11,13,15,17],
    },
    'output': 11
})
tests.append({
    # rotated once #3
    'input': {
    'nums': [3,1,2],
    },
    'output': 1
})
tests.append({
    # rotated n-1 times #4
    'input': {
    'nums': [2,3,4,5,1],
    },
    'output': 1
})
tests.append({
    # rotated n times #5
    'input': {
    'nums': [2,3,4,5,6],
    },
    'output': 2
})
# tests.append({
#     # empty
#     'input': {
#     'nums': [],
#     },
#     'output': 0
# })
tests.append({
    # one element
    'input': {
    'nums': [1],
    },
    'output': 1
})
print(findMin([1,1]))
# for i,test in enumerate(tests):
#     print(findMin(test['input']['nums'])==test['output'],i)