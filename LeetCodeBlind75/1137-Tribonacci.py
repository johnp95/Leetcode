def tribonacciMemo(n,memo={}):
    if n in memo: return memo[n]
    if n == 0: return 0    
    if n <= 2: return 1

    memo[n] = tribonacciMemo(n-1)+tribonacciMemo(n-2)+tribonacciMemo(n-3)
    return memo[n]
def tribonacciTab(n):
    table = [0]*(n+1)
    if n >1:
        table[1],table[2]= 1,1
        for i in range(len(table)):
            if i > 1:
                if i +1 <= n:  
                    table[i+1] = table[i]+table[i-2]+table[i-1]
        return table[n]
    else:
        return n
if __name__ == '__main__':
    resultTab = tribonacciTab(25)
    resultMemo = tribonacciMemo(25)
    print(resultTab,resultMemo)