class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracketMap = {')':'(', '}':'{',']':'['}

        for c in s:
            if c in ('(','[','{'):
                stack += [c]
            else:
                if not stack:
                    return False
                check = stack.pop()
                if check != bracketMap[c]:
                    return False
        return len(stack)==0
    
s = '()'
sol = Solution()
print(sol.isValid(s))