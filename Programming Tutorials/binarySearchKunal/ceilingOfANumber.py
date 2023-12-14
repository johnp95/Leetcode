def ceilingOfNumber(arr,target):
    start,end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid]==target:
            return arr[mid]    

        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return arr[start] 
if __name__ == '__main__':
    arr = [2,3,5,9,14,16,18]
    target = 15
    print(ceilingOfNumber(arr,target))
    