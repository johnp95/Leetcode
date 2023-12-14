def climbStairs(n,memo={}):
    if n in memo : return memo[n]
    if n == 0 : return 1
    if n < 0 : return 0

    one_step = climbStairs(n-1)
    two_step = climbStairs(n-2)
    memo[n] = one_step + two_step
    return memo[n]
        


if __name__ == '__main__':
    print(climbStairs(5))