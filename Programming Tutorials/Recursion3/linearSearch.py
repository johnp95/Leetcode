def linearSearch(arr,target,idx=0):
    if idx > len(arr)-1 : return False
    return arr[idx] == target or linearSearch(arr,target,idx+1)
def linearSearchMultipleOccurence(arr,target,idx=0,ans=[]):
    if idx > len(arr)-1 : return ans
    if arr[idx] == target:
        ans += [idx]
    return linearSearchMultipleOccurence(arr,target,idx+1)

if __name__ == '__main__':
    arr,target = [3,2,1,18,9], 18
    arr,target = [2,3,1,4,4,5], 4
    print(linearSearchMultipleOccurence(arr,target))