nums = [2,7,11,15]
target = 9
# off the top
start, end = 0,len(nums)-1
curr_sum = 0
while start < end:
    curr_sum = nums[start] + nums[end]
    if curr_sum == target:
        print( [start+1,end+1])
        break
    elif curr_sum < target:
        start += 1
    else:
        end -= 1
