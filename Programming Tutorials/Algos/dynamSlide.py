arr = [2,3,4,2,1,7]
x = 7
min_length = float('inf')

start = 0
end = 0
current_sum = 0

while end < len(arr):
   
    current_sum = current_sum + arr[end]
    end = end + 1
    
    while start < end and  current_sum >= x:
        current_sum = current_sum - arr[start]
        start = start + 1

        min_length = min(min_length, end-start+1)
        # print(start,end,current_sum,min_length)
   
print(min_length)