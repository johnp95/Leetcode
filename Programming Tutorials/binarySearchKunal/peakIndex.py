#Mine
# def peakIndexInMountainArray(arr):
    
#     start,end = 0, len(arr)-1

#     while start <= end:
#         mid = (start + end) // 2

#         if arr[mid-1] < arr[mid] > arr[mid+1]:
#             return mid
 
#         if mid-1 >= 0 and arr[mid] < arr[mid-1]:
#             end = mid - 1
#         else:
#             start = mid + 1
#Kunal            
def peakIndexInMountainArray(arr):
    
    start,end = 0, len(arr)-1

    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] > arr[mid+1]:
            end = mid 
        else:
            start = mid + 1
    return end
if __name__ == '__main__':
    arr = [[0,1,0],[0,2,1,0],[0,10,5,2],[0,2,4,8,6,1],[3,5,3,2,0]]
    ans = [1,1,1,3,1]
    # print(peakIndexInMountainArray([0,2,4,8,6,1]))
    for i in range(len(arr)):
        print(peakIndexInMountainArray(arr[i])==ans[i])
