def maxProfit(prices):
        
    min_val = prices[0]
    max_profit = 0

    for p in prices:
        if p < min_val:
            min_val = p
        max_profit = max(max_profit,p-min_val)
    return max_profit
prices = [7,1,5,3,6,4]

print(maxProfit(prices))