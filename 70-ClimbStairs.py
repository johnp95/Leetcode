def climbStairs(n,memo={}):
    if n in memo: return memo[n]
    if n == 0: return 1
    if n < 0: return 0
    oneStep = climbStairs(n-1)
    TwoStep = climbStairs(n-2)
    memo[n] = oneStep + TwoStep
    return memo[n]

if __name__ == '__main__':
    result = climbStairs(4)
    print(result)