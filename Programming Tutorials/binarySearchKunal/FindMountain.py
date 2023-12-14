class MountainArray:
    def __init__(self):
        self.arr = [1,2,3,4,5,3,1]
        # self.arr = [0,1,2,4,2,1]
        # self.arr = [3,5,3,2,0]
        # self.arr = [1,5,2]
        self.target = 3
    def get(self,index):
        return self.arr[index]
    def length(self):
        return len(self.arr)
    def Print(self):
        print(self.findInMountainArray(self.target))
    def findInMountainArray(self,target):
        n = self.length()-1
        def binarySearch(start,end,target,findVal=False,isDescending=False):
            while start < end:
                mid = (start + end) // 2
                arrNum = self.get(mid)
                # regular binary search
                if findVal:
                    if target == arrNum:
                        return mid
                    if target < arrNum:
                        end = mid
                    elif target > arrNum:
                        start = mid + 1
                # reverses ordinary binary search
                elif isDescending:
                    if target == arrNum:
                        return mid
                    if target < arrNum:
                        start = mid + 1
                    elif target > arrNum:
                        end = mid
                else:
                    # find peak
                    if arrNum > self.get(mid+1):
                        end = mid
                    else:
                        start = mid + 1
            # returns peak on first call
            if not findVal and not isDescending:
                return end
            # return end because using start < end
            else:
                return end if self.get(end)==target else -1
        
        # peak of array
        peak = binarySearch(0,n,target)
        # ans -> check if target is in ascending part of array
        ans = binarySearch(0,peak+1,target,findVal=True) 
        if ans != -1:
            return ans
        # if target is not found in ascending, check descending
        else:
            return binarySearch(peak,n,target,isDescending=True)

if __name__ == '__main__':
    mountain_arr = MountainArray()
    mountain_arr.Print()