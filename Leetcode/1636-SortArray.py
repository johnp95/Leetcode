nums = [-1,1,-6,4,5,-6,1,4,1]
nums = sorted(nums,reverse=True)
lis = []
for i in nums:
    lis.append([i,nums.count(i)])
lis = sorted(lis,key=lambda x: x[1])
ans =[]
for i,j in lis:
    ans += [i]
print(ans)
    