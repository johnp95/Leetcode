nums = [9,6,4,2,1]

k = 2
result = sum(nums[:k])
curr_sum = result

max_ = float('-inf')
 
for i in range(1,(len(nums)-k)+1):
    print(curr_sum)
    curr_sum -= nums[i-1]
    curr_sum += nums[(i+k)-1]
    print(nums[(i+k)-1])
    # max_ = max(curr_sum,max_)
# print(max_)


# v2
# curr_sum = 0
# max_avg = float('-inf')
# max_ = float('-inf')
# start = 0
# for end in range(len(nums)):
#     curr_sum += nums[end]
#     if (end-start + 1 ) == k:
#         # max_avg = max(curr_sum/k,max_avg)
#         max_ = max(curr_sum,max_)
#         curr_sum -= nums[start]
#         start += 1
# print(max_)