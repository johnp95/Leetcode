def binarySearch(A,left,right,target):
    if left > right : return -1
    mid = (left+right)//2

    if A[mid] == target:
        return mid
    if target < A[mid]:
        return binarySearch(A,left,mid-1,target)
    else:
        return binarySearch(A,mid+1,right,target)


A = [1,2,3,4,5]

print(binarySearch(A,0,len(A)-1,4))