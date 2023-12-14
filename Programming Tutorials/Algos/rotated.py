# from testCases import tests
def binary_count_rotations(nums):
    
    lo,hi = 0, len(nums)-1
    while lo <= hi and nums!=sorted(nums):
        mid = (lo+hi)//2
        # print(f' lo: {lo} hi: {hi} mid: {mid}')
        if nums[mid] < nums[mid-1] and mid-1 >= 0:
            return mid 
        
        if nums[mid] < nums[hi]:
            hi = mid - 1
        elif nums[mid] > nums[hi]:
            lo = mid + 1

    return 0
        

# test0 = tests[0]['input']['nums']
# test1 = tests[1]['input']['nums']
# test2 = tests[2]['input']['nums']
print(binary_count_rotations([4,5,6,7,0,1,2]))
# print(binary_count_rotations(test0) == tests[0]['output'])
# print(binary_count_rotations(test1) == tests[1]['output'])
# print(binary_count_rotations(test2) == tests[2]['output'])
# print(binary_count_rotations(test0) == tests[0]['output'])
# for i,test in enumerate(tests):
    # print(binary_count_rotations(test['input']['nums'])==test['output'],i)