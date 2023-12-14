def minCostClimbingStairs(cost):
    table = [float('inf')] * (len(cost)+2)
    table[-1] = 0
    table[-2] = 0
    for i in range(len(table)-1,-1,-1):
        if i-1 >= 0 and i+1 < len(table):
            table[i-1] = cost[i-1] + min(table[i], table[i+1])        
    return min(table[0],table[1])
    
if __name__ == '__main__':
    print(minCostClimbingStairs([10,15,20]))