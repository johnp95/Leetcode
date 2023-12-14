class Dynamic:
    def fib(self,num,memo={}):
        if num in memo: return memo[num]
        if num <= 2: return 1 
        memo[num] = self.fib(num-2,memo) + self.fib(num-1,memo)
        return memo[num]
    def gridTraveler(self,m,n,memo={}): 
        if (m,n) in memo:return memo[(m,n)]
        if (n,m) in memo:return memo[(n,m)]
        if m==0 or n==0: return 0
        if m==1 or n == 1: return 1
        down = self.gridTraveler(m-1,n,memo)
        right =  self.gridTraveler(m,n-1,memo) 
        memo[(m,n)] = down + right
        return memo[(m,n)]
    def canSum(self,targetSum, numbers,memo={}):
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return True
        if targetSum < 0: return False
        for num in numbers:
            remainder = targetSum - num
            if self.canSum(remainder,numbers,memo) == True:
                print(f'\tif memo {memo}')
                memo[targetSum] = True
                return True

        memo[targetSum] = False
        return False
    def howSum(self,targetSum,numbers,memo={}):

        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0: return None
        
        for num in numbers:
            remainder = targetSum - num
            remainderResult = self.howSum(remainder,numbers,memo)
            if remainderResult is not None:
                memo[targetSum] = remainderResult + [num]
                return memo[targetSum]
        memo[targetSum] = None
        return None
    def bestSum(self,targetSum,numbers,memo={}):
        if targetSum in memo : return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0 : return None

        shortestCombination = None

        for num in numbers:
            remainder = targetSum - num
            remainderCombination = self.bestSum(remainder,numbers,memo)
            if remainderCombination:
                combination = remainderCombination + [num]
                if shortestCombination == None or len(combination) < len(shortestCombination):
                    shortestCombination = combination
                    
        # return shortestCombination
        memo[targetSum] = shortestCombination
        return shortestCombination
    def canConstruct(self,target,wordBank,memo={}):
        if target in memo : return memo[target]
        if target == '' : return True

        for word in wordBank:
            if target.startswith(word):
                suffix = target.replace(word,'',1)
                if self.canConstruct(suffix,wordBank,memo):
                    memo[target] = True
                    return True
        memo[target] = False
        return False
    def countConstruct(self,target,wordBank,memo={}):
        if target in memo : return memo[target]
        if target == '' : return 1
        totalCount = 0
        for word in wordBank:
            if target.startswith(word):
                suffix = target.replace(word,'')
                numWaysForRest = self.countConstruct(suffix,wordBank)
                totalCount += numWaysForRest

        memo[target] = totalCount
        return totalCount
    def allConstruct(self,target,wordBank,memo = {}):
        if target in memo: return memo[target]
        if target == '' : return [[]]
        result = []
        for word in wordBank:
            if target.startswith(word):
                suffix = target.replace(word,'',1)
                # suffix = target[len(word):]
                suffixWays = self.allConstruct(suffix,wordBank,memo)
                targetWays = [[word] + s for s in suffixWays]
                result += targetWays
                # result.append(targetWays)
        memo[target] = result
        return result
    def fibTab(self,n):

        table = [0]*(n+1)
        table[1] = 1  
        for i in range(len(table)):
            if i+1 <= n:
                table[i+1] += table[i]
            if i+2 <= n:
                table[i+2] += table[i]
        return table[n]
    def gridTab(self,m,n):
        table = [[0]*(n+1) for _ in range(m+1)]
        table[1][1] = 1
        for row in range(len(table)):
            for col in range(len(table[0])):
                if row+1 <= m:
                    table[row+1][col] += table[row][col]    
                if col+1 <= n:
                    table[row][col+1] += table[row][col]
        return table[m][n]
    def canSumTab(self,targetSum, numbers):
        table = [False]*(targetSum+1)
        table[0] = True
        for i in range(len(table)):
            if table[i]==True:
                for num in numbers:
                    if i+num <= targetSum:
                        print(i,num,i+num)
                        table[i+num] = True
        return table[targetSum]
    def howSumTab(self,targetSum,numbers):
        table = [None]*(targetSum+1)
        table[0] = []
        for i in range(len(table)):
            if table[i] is not None:
                for num in numbers:
                    if i+num <= targetSum:
                        table[i+num] = table[i] + [num]
        return table
    def bestSumTab(self,targetSum,numbers):
        table = [None]*(targetSum+1) 
        table[0] = []
        for i in range(len(table)):
            if table[i] is not None:
                for num in numbers:
                    if i+num <= targetSum:
                        shortest = table[i]+[num]
                        if table[i+num] is not None and len(table[i+num]) < len(shortest):
                            shortest = table[i+num]
                        table[i+num] = shortest
                    
        return table
    def canConstructTab(self,target,wordBank):
        table = [False]* (len(target)+1)
        table[0] = True
        for i in range(len(table)):
            if table[i]==True:
                for word in wordBank:
                    if word==target[i:i+len(word)]:
                        table[i+len(word)] = True
        return table[len(target)]
    def countConstruct(self,target,wordBank):
        table = [0]*(len(target)+1)
        table[0] = 1
        for i in range(len(table)):
            curr = table[i]
            for word in wordBank:
                if word==target[i:i+len(word)]:
                    table[i+len(word)] += curr

        return table
    def allConstructTab(self,target,wordBank):
        table = [[] for _ in range(len(target)+1)]
        table[0] = [[]]
        for i in range(len(table)):
            for word in wordBank:
                if word == target[i:i+len(word)]:
                    table[i+len(word)] += [subList+[word] for subList in table[i]]
                    print(i,i+len(word))
            if i == 2:
                break
        return table
        # return table[len(target)]
if __name__ == '__main__':

    dynamic = Dynamic() 
    fibTab = dynamic.bestSum(6,[8,3,1,2])
    print(fibTab)
    