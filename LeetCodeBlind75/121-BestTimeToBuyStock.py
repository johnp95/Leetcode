def maxProfit(prices):
    start = 0
    max_profit = 0
    for end in range(len(prices)):
        curr = prices[end]
        if curr < prices[start]:
            start  = end
        max_profit = max(max_profit,curr-prices[start])
    return max_profit
if __name__ == '__main__':
    print(maxProfit([1,6])) # 5
    print(maxProfit([1,2,6])) # 5
    print(maxProfit([2,1,6])) # 5
    print(maxProfit([7,1,5,3,6,4])) # 5
    print(maxProfit([7,6,4,3,2,1])) # 0
    print(maxProfit([2,1,2,1,0,1,2])) # 2