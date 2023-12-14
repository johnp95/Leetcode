def coinChange(coins,amount,memo=None):
    if memo is None: memo = {}
    if amount in memo: return memo[amount]
    if amount == 0: return 0
    if amount < 0: return -1

    _min = float('inf')
    for coin in coins:
        res = coinChange(coins,amount-coin,memo) # -> 0 or None
        if res != -1:
            count = 1 + res 
            _min = min(_min,count)
        

    memo[amount] = _min if _min != float('inf') else -1
    return memo[amount]

if __name__ == '__main__':
    print(coinChange([1,2,5],11))

