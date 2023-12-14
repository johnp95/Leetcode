def infinite(arr,target):
    start = 0
    end = 1

    while target > arr[end]:
        temp = end + 1
        end = end + (end - start + 1) * 2
        start = temp
    # def binarySearch(arr,target,start,end):
    #     while start <= end:
    #         mid = start + (end-start) // 2
    #         if target < arr[mid]:
    #             end = mid  - 1
    #         elif target > arr[mid]:
    #             start = mid + 1
    #         else:
    #            return mid

    # return binarySearch(arr,target,start,end)



if __name__ == '__main__':

    target = 15
    arr = [2,3,5,6,7,8,10,11,12,15,20,23,30]
    print(infinite(arr,target))