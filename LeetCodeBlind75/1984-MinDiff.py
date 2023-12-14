nums = [9,4,1,7]
nums = [87063,61094,44530,21297,95857,93551,9918]
nums = sorted(nums,reverse=True)
k = 6
min_ = float('inf')
for i in range(len(nums)-k+1):
    min_ = min(min_, (nums[i] - nums[i+k-1]))
print(min_)