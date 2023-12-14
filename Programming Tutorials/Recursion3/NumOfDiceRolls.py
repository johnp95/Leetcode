def numRollsToTarget(n,k,target):
    memo = {}
    def helper(n,k,target,curr):
        if (n,target) in memo : return memo[(n,target)]
        if target == 0 and n == 0: 
            return 1 
        if n == 0 or target < 0: return 0
        count = 0
        for num in range(1,k+1):
                count += helper(n-1,k,target-num,curr+str(num))
        memo[(n,target)] = count
        return count
    ans = helper(n,k,target,'')
    return int(ans % (10**9+7))
if __name__ == '__main__':
    n = 30
    k = 30
    target = 500
    print(numRollsToTarget(n,k,target))