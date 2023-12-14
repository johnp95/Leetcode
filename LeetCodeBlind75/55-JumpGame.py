def canJump(nums):
    if nums[0] >= len(nums)-1:
        return True
    for idx in range(len(nums[:nums[0]+1])):
        if idx+nums[idx] >= len(nums[:nums[0]+1]):
            return canJump(nums[idx:])
       
    return False

if __name__ == '__main__':
    tests = [[2,3,1,1,4], [3,2,1,0,4], [2,0,0],[2,5,0,0],[3,0,8,2,0,0,1],[1,1,1,0],[1,1,2,2,0,1,1],[5,9,3,2,1,0,2,3,3,1,0,0],[4,2,0,0,1,1,4,4,4,0,4,0]]
    

    for test in tests:
        print(canJump(test),test)
