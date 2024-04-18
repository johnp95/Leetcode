class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)
        for i,t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:
                stackIndex = stack.pop()
                ans[stackIndex] = i - stackIndex
            
            stack += [i]
        return ans

temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
res = solution.dailyTemperatures(temperatures)
print(res)