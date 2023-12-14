def rotated(arr,start,end,target):
    if start > len(arr)-1 or end < 0 : return -1
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    if arr[start] <= arr[mid]:
        if arr[start] <= target <= arr[mid]:
            return rotated(arr,start,mid-1,target)
        else:
            return rotated(arr,mid+1,end,target)
    else:
        if arr[mid] <= target <= arr[end]:
            return rotated(arr,mid+1,end,target)
        else:
            return rotated(arr,start,mid-1,target)
        

if __name__ == '__main__':
    # arr = [5,6,7,8,9,1,2,3]
    arr = [5,1,3]
    start,end,target = 0,len(arr)-1,0
    print(rotated(arr,start,end,target))