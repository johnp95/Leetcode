arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
curr_sum = 0
start = 0
output = 0
for end in range(len(arr)):
    curr_sum += arr[end]

    if end - start + 1 == k:
        if curr_sum / k >= threshold:
            output += 1
        curr_sum -= arr[start]
        start +=1
print(output)