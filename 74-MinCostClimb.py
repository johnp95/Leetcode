def minCostClimbingStairs(cost):
    def helper(idx):
        if idx >= len(cost):
            return 0
        if memo[idx] != -1:
            return memo[idx]
        one_step = cost[idx] + helper(idx + 1)
        two_step = cost[idx] + helper(idx + 2)
        memo[idx] = min(one_step, two_step)
        return memo[idx]

    memo = [-1] * len(cost)
    return min(helper(0), helper(1))  # Starting from indices 0 and 1

if __name__ == '__main__':
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))
