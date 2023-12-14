def arrayList(arr,target,idx=0):
    if idx > len(arr)-1: return []

    if arr[idx] == target:
        return [idx] + arrayList(arr,target,idx+1)
    else:
      return arrayList(arr,target,idx+1)# => []
    
    

if __name__ == '__main__':
    arr,target = [1,2,3,4,4,8], 4
    print(arrayList(arr,target))